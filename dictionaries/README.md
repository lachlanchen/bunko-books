# Optional offline dictionaries

These packs are downloaded only when a Bunko reader chooses a language. They are not included in the app install or the book bundles. Each pack is split into 16 deterministic gzip shards. `manifest.json` records the source archive checksum, shard checksums, byte counts, and generation version. The reproducible builder is [`tools/build_dictionary_packs.py`](https://github.com/lachlanchen/Bunko/blob/main/tools/build_dictionary_packs.py) in the app repository.

| Pack | Source | License |
| --- | --- | --- |
| Chinese → English | [CC-CEDICT, MDBG](https://www.mdbg.net/chinese/dictionary?page=cc-cedict), download dated 2026-09-25 | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| Japanese → English | [JMdict, Electronic Dictionary Research and Development Group](https://www.edrdg.org/wiki/JMdict-EDICT_Dictionary_Project.html), download dated 2026-09-25 | [CC BY-SA 4.0](https://www.edrdg.org/edrdg/licence.html) |
| English → English | [Open English WordNet 2025](https://en-word.net/downloads) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

The Chinese and Japanese pack data are adaptations shared under CC BY-SA 4.0. The English pack data are adapted under CC BY 4.0. The source archives themselves are not mirrored here. Definitions may contain errors or omit senses; consult the upstream source for corrections. The software in the Bunko app is separate from these data packs.
