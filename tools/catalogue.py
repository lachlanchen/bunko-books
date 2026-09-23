#!/usr/bin/env python3
"""Validate approved book bundles and derive the schema-1 mobile catalog.

Run after adding books/<slug>/{meta,rights}.json, chapters and optional cover.
No app build is involved. Historical content-addressed chapters may remain.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

LANGS = {"en", "zh", "ja", "wenyan", "zh_modern", "ja_modern"}
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
    require(langs and set(langs) <= LANGS and len(langs) == len(set(langs)), f"{slug}: invalid languages")
    require(set(langs) == set(rights.get("langs", [])), f"{slug}: languages exceed clearance")
    require(meta.get("primary") in langs and meta.get("titleText", {}).get(meta["primary"]), f"{slug}: missing title/primary")
    require(meta.get("chapters"), f"{slug}: no chapters")
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
            for unit in paragraph["u"]:
                annotation = unit.get("annotation") is True and not unit.get("src", "").strip()
                present = [lang for lang in langs if lang in unit]
                require(present and (annotation or len(present) == len(langs)) and all(line_valid(unit[lang]) for lang in present), f"{slug}/{name}: missing/invalid text layer")
                require(not (set(unit) & (LANGS - set(langs))), f"{slug}/{name}: uncleared extra language")
        total_bytes += len(data)
        total_paras += len(paragraphs)
    require(total_bytes == meta.get("bytes") and total_paras == meta.get("paras"), f"{slug}: totals mismatch")
    row = {"id": slug, "mode": meta["mode"], "langs": langs, "primary": meta["primary"],
           "title": meta["titleText"], "author": meta.get("author", {}).get("name", ""),
           "chapters": len(meta["chapters"]), "paras": total_paras, "bytes": total_bytes + len(raw),
           "sha256": sha(raw), "cat": meta.get("cat", "chinese" if "wenyan" in langs else "world"),
           "edition": meta.get("edition", "multilingual")}
    if meta.get("cover"):
        name = meta["cover"]
        require(COVER.fullmatch(name), f"{slug}: invalid cover path")
        cover = directory / name
        require(not cover.is_symlink() and cover.stat().st_size < 10_000_000, f"{slug}: invalid cover file")
        require(rights.get("cover", {}).get("textFree") is True and rights["cover"].get("basis"), f"{slug}: cover not reviewed")
        require(sha(cover.read_bytes()).startswith(name.split("-")[1].split(".")[0]), f"{slug}: cover hash mismatch")
        row["cover"] = f"books/{slug}/{name}"
    return row


def build_index(root):
    books = []
    for directory in sorted((root / "books").iterdir()):
        require(directory.is_dir() and not directory.is_symlink(), "Only book directories allowed")
        row = book_row(directory)
        if row:
            books.append(row)
    return {"schema": 1, "books": books, "bytes": sum(b["bytes"] for b in books), "count": len(books)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    index = build_index(args.root)
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
