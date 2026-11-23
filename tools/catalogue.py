#!/usr/bin/env python3
"""Validate approved book bundles and derive the schema-1 mobile catalog.

Run after adding books/<slug>/{meta,rights}.json, chapters and optional cover.
No app build is involved. Historical content-addressed chapters may remain.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

LEGACY_LANGS = {"wenyan", "zh_modern", "ja_modern"}
UNIT_FIELDS = {"src", "rich", "annotation"}


def language_valid(value):
    return isinstance(value, str) and value not in UNIT_FIELDS and (
        value in LEGACY_LANGS or (len(value) <= 63 and re.fullmatch(r"[A-Za-z]{2,8}(?:-[A-Za-z0-9]{1,8})*", value)))

SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CHAPTER = re.compile(r"^c[0-9]+(?:p[0-9]+)?(?:-[a-f0-9]+)?\.json$")
COVER = re.compile(r"^cover-[a-f0-9]+\.(?:webp|png|jpg)$")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def line_valid(line):
    return isinstance(line, list) and bool(line) and all(
        isinstance(token, str) or (isinstance(token, list) and 1 <= len(token) <= 3 and
                                  all(isinstance(value, str) for value in token) and
                                  (len(token) < 3 or token[2] in set("spoadctf"))) for token in line)


def sentence_map(directory):
    path = directory / "sentences-v1.json"
    if not path.exists():
        return None, {}
    require(not path.is_symlink() and 0 < path.stat().st_size <= 32 * 1024**2, "Invalid sentence-map file")
    raw = path.read_bytes()
    value = json.loads(raw)
    require(value.get("schema") == 1 and value.get("book") == directory.name and
            isinstance(value.get("chapters"), dict), "Invalid sentence-map header")
    return sha(raw), value["chapters"]


def verify_sentences(entry, paragraphs, langs):
    require(isinstance(entry, dict) and re.fullmatch(r"[a-f0-9]{64}", entry.get("chapterHash", "")) and
            isinstance(entry.get("units"), dict), "Invalid sentence-map chapter")
    for coordinate, layers in entry["units"].items():
        require(re.fullmatch(r"(?:0|[1-9][0-9]{0,6})\.(?:0|[1-9][0-9]{0,6})", coordinate), "Invalid sentence-map coordinate")
        paragraph, offset = map(int, coordinate.split("."))
        require(paragraph < len(paragraphs) and offset < len(paragraphs[paragraph]["u"]), "Unknown sentence-map unit")
        parent = paragraphs[paragraph]
        unit = parent["u"][offset]
        require(parent.get("kind", "text") == "text" and not parent.get("figure") and
                not parent["id"].endswith("-notes") and not unit.get("rich") and not unit.get("annotation"), "Invalid sentence-map passage")
        require(isinstance(layers, dict) and layers and set(layers) <= set(langs) & set(unit), "Invalid sentence-map language")
        for lang, cuts in layers.items():
            line = unit[lang]
            length = 0
            require(isinstance(cuts, list) and cuts and all(type(point) is int for point in cuts) and
                    sorted(set(cuts)) == cuts and cuts[0] > 0, "Invalid sentence-map offsets")
            index = 0
            for token in line:
                text = token if isinstance(token, str) else token[0]
                end = length + len(text.encode("utf-16-le")) // 2
                while index < len(cuts) and cuts[index] <= end:
                    require(cuts[index] == end or isinstance(token, str) or len(token) == 1 or not token[1], "Sentence-map cut divides ruby")
                    index += 1
                length = end
            require(cuts[-1] < length, "Sentence-map offset outside text")


def book_row(directory):
    slug = directory.name
    require(SLUG.fullmatch(slug), "Invalid book id")
    require(not (directory / "rights.json").is_symlink() and not (directory / "meta.json").is_symlink(), f"{slug}: symlink not allowed")
    rights = json.loads((directory / "rights.json").read_text())
    require(rights.get("id") == slug, f"{slug}: rights id mismatch")
    if rights.get("status") == "hold":
        return None
    require(rights.get("status") == "ship", f"{slug}: missing explicit clearance")
    require(bool(rights.get("basis")) and bool(rights.get("references")) and bool(rights.get("checked")), f"{slug}: missing rights evidence")
    raw = (directory / "meta.json").read_bytes()
    meta = json.loads(raw)
    require(meta.get("schema") == 1 and meta.get("id") == slug, f"{slug}: invalid schema/id")
    langs = meta.get("langs", [])
    require(isinstance(langs, list) and langs and all(language_valid(lang) for lang in langs) and len(langs) == len(set(langs)), f"{slug}: invalid languages")
    require(set(langs) == set(rights.get("langs", [])), f"{slug}: languages exceed clearance")
    require(meta.get("primary") in langs and meta.get("titleText", {}).get(meta["primary"]), f"{slug}: missing title/primary")
    require(meta.get("chapters"), f"{slug}: no chapters")
    sentence_hash, sentences = sentence_map(directory)
    require(set(sentences) <= {row["file"] for row in meta["chapters"]}, f"{slug}: unknown sentence-map chapter")
    total_bytes, total_paras, files = 0, 0, set()
    for row in meta["chapters"]:
        name = row.get("file", "")
        require(CHAPTER.fullmatch(name) and name not in files, f"{slug}: invalid/duplicate chapter path")
        files.add(name)
        path = directory / name
        require(not path.is_symlink(), f"{slug}: symlink not allowed")
        data = path.read_bytes()
        require(0 < len(data) < 20_000_000 and len(data) == row.get("bytes"), f"{slug}/{name}: size mismatch")
        if row.get("sha256"):
            require(sha(data) == row["sha256"], f"{slug}/{name}: checksum mismatch")
        chapter = json.loads(data)
        paragraphs = chapter.get("p", [])
        require(paragraphs and len(paragraphs) == row.get("paras"), f"{slug}/{name}: paragraph count mismatch")
        for paragraph in paragraphs:
            require(paragraph.get("u"), f"{slug}/{name}: empty paragraph")
            figure = paragraph.get("figure")
            if figure:
                asset = figure.get("path", "")
                require(re.fullmatch(r"assets/[A-Za-z0-9/_-]+\.(?:png|jpg|jpeg|webp)", asset) and
                        not (directory / asset).is_symlink() and (directory / asset).is_file(),
                        f"{slug}/{name}: invalid figure")
            for unit in paragraph["u"]:
                annotation = unit.get("annotation") is True and not unit.get("src", "").strip()
                present = [lang for lang in langs if lang in unit]
                require(present and (annotation or len(present) == len(langs)) and all(line_valid(unit[lang]) for lang in present), f"{slug}/{name}: missing/invalid text layer")
                require(set(unit) <= set(langs) | UNIT_FIELDS, f"{slug}/{name}: uncleared extra language")
                if unit.get("rich"):
                    require(set(unit["rich"]) <= set(langs) and all(
                        isinstance(part, list) and all(isinstance(item, dict) and
                        ("text" in item or "math" in item) for item in part)
                        for part in unit["rich"].values()), f"{slug}/{name}: invalid rich text")
        if name in sentences:
            verify_sentences(sentences[name], paragraphs, langs)
        total_bytes += len(data)
        total_paras += len(paragraphs)
    require(total_bytes == meta.get("bytes") and total_paras == meta.get("paras"), f"{slug}: totals mismatch")
    row = {"id": slug, "mode": meta["mode"], "langs": langs, "primary": meta["primary"],
           "title": meta["titleText"], "author": meta.get("author", {}).get("name", ""),
           "chapters": len(meta["chapters"]), "paras": total_paras, "bytes": total_bytes + len(raw),
           "sha256": sha(raw), "cat": meta.get("cat", "chinese" if "wenyan" in langs else "world"),
           "edition": meta.get("edition", "multilingual")}
    if sentence_hash:
        row["sentenceSha256"] = sentence_hash
    if meta.get("cover"):
        name = meta["cover"]
        require(COVER.fullmatch(name), f"{slug}: invalid cover path")
        cover = directory / name
        require(not cover.is_symlink() and cover.stat().st_size < 10_000_000, f"{slug}: invalid cover file")
        require(rights.get("cover", {}).get("basis") and (rights["cover"].get("textFree") is True or rights["cover"].get("originalDesign") is True), f"{slug}: cover not reviewed")
        require(sha(cover.read_bytes()).startswith(name.split("-")[1].split(".")[0]), f"{slug}: cover hash mismatch")
        row["cover"] = f"books/{slug}/{name}"
    return row


def build_index(root, new_added_at=None):
    target = root / "reader-index.json"
    prior = {row["id"]: row.get("addedAt") for row in json.loads(target.read_text())["books"]} if target.exists() else {}
    books = []
    for directory in sorted((root / "books").iterdir()):
        require(directory.is_dir() and not directory.is_symlink(), "Only book directories allowed")
        row = book_row(directory)
        if row:
            added_at = prior.get(row["id"]) or new_added_at
            if added_at:
                require(isinstance(added_at, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:Z|[+-]\d{2}:\d{2})", added_at), f"{row['id']}: invalid publication date")
                datetime.fromisoformat(added_at.replace('Z', '+00:00'))
                row["addedAt"] = added_at
            books.append(row)
    return {"schema": 1, "books": books, "bytes": sum(b["bytes"] for b in books), "count": len(books)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    index = build_index(args.root, datetime.now(timezone.utc).isoformat(timespec='seconds') if args.write else None)
    target = args.root / "reader-index.json"
    if args.write:
        temporary = target.with_suffix(".tmp")
        temporary.write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")))
        temporary.replace(target)
    else:
        require(json.loads(target.read_text()) == index, "Index is stale; run tools/catalogue.py --write")
    print(f"Validated {index['count']} books, {index['bytes']/1e6:.1f} MB. Schema 1; no app rebuild.")


if __name__ == "__main__":
    main()
