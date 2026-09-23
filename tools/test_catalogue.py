import json
import tempfile
import unittest
from pathlib import Path

from catalogue import book_row


class PublicationGate(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "test-book"
        self.root.mkdir()
        self.rights = {"id": "test-book", "status": "ship", "basis": "Ancient original; owner-generated translation", "references": ["review"], "checked": "2026-09-23", "langs": ["wenyan", "ja"]}
        self.chapter = {"id": "one", "n": 1, "p": [{"id": "p1", "u": [{"wenyan": ["道"], "ja": ["道"], "src": "道"}]}]}
        self.meta = {"schema": 1, "id": "test-book", "mode": "wenyan_ja_zh", "langs": ["wenyan", "ja"], "primary": "wenyan", "titleText": {"wenyan": "道"}, "chapters": [{"file": "c0001.json", "paras": 1}], "paras": 1}

    def tearDown(self):
        self.temp.cleanup()

    def write(self):
        raw = json.dumps(self.chapter, ensure_ascii=False).encode()
        self.meta["bytes"] = len(raw)
        self.meta["chapters"][0]["bytes"] = len(raw)
        (self.root / "c0001.json").write_bytes(raw)
        for name, data in (("meta", self.meta), ("rights", self.rights)):
            (self.root / f"{name}.json").write_text(json.dumps(data))

    def test_complete_edition_publishes(self):
        self.write()
        self.assertEqual(book_row(self.root)["paras"], 1)

    def test_hold_never_enters_catalog(self):
        self.rights["status"] = "hold"
        self.write()
        (self.root / "meta.json").unlink()
        self.assertIsNone(book_row(self.root))

    def test_missing_translation_rejected(self):
        del self.chapter["p"][0]["u"][0]["ja"]
        self.write()
        with self.assertRaisesRegex(ValueError, "missing/invalid text"):
            book_row(self.root)

    def test_annotations_preserved_without_fabricated_translation(self):
        self.chapter["p"][0]["u"] = [{"ja": ["注終わり。"], "src": "", "annotation": True}]
        self.write()
        self.assertEqual(book_row(self.root)["paras"], 1)
        self.chapter["p"][0]["u"][0]["src"] = "missing original"
        self.write()
        with self.assertRaises(ValueError):
            book_row(self.root)

    def test_uncleared_language_rejected(self):
        self.chapter["p"][0]["u"][0]["en"] = ["uncleared"]
        self.write()
        with self.assertRaisesRegex(ValueError, "uncleared"):
            book_row(self.root)

    def test_path_traversal_rejected(self):
        self.meta["chapters"][0]["file"] = "../c0001.json"
        self.write()
        with self.assertRaisesRegex(ValueError, "chapter path"):
            book_row(self.root)

    def test_corrupt_download_rejected(self):
        self.meta["chapters"][0]["sha256"] = "not-the-checksum"
        self.write()
        with self.assertRaisesRegex(ValueError, "checksum"):
            book_row(self.root)


if __name__ == "__main__":
    unittest.main()
