# bunko-books

**The reader data for [Bunko](https://github.com/lachlanchen/Bunko): public-domain classics in English, Chinese and Japanese, with a reading for every character.**

JSON only. No PDFs (those live in [LinguaLeaf](https://github.com/lachlanchen/LinguaLeaf)), no images, no binaries, so the tree stays light and the CDN stays fast.

## Layout

```
reader-index.json        every published book: id, titles, languages, mode, chapters, bytes, sha256
books/<id>/meta.json     titles and author with readings, language list, chapter table
books/<id>/cNNN.json     one chapter
```

Fetch over jsDelivr, which is free, global and CORS-open:

```
https://cdn.jsdelivr.net/gh/lachlanchen/bunko-books@main/reader-index.json
https://cdn.jsdelivr.net/gh/lachlanchen/bunko-books@main/books/daodejing/meta.json
https://cdn.jsdelivr.net/gh/lachlanchen/bunko-books@main/books/daodejing/c0001.json
```

## The token format

A line of text is an array of tokens. A token is a bare string when it has no reading, `[text, reading]` when it has one, and `[text, reading, role]` when the generator also labelled its grammatical role.

```json
["道", "dào", "s"], ["可", "kě", "s"], ["道", "dào", "a"], "，"
```

Roles are one letter: `s` subject, `p` predicate, `o` object, `a` attributive, `d` adverbial, `c` complement, `t` topic, `f` function.

That compaction is most of why a book here is about a sixth of the size of the pipeline's assembled output.

## Rights

Every book in this repository has a row saying `ship` in [Bunko's rights audit](https://github.com/lachlanchen/Bunko/blob/main/docs/catalogue.md), with the reason and the date. The originals are out of copyright; the modern Chinese, Japanese and English renderings were generated from those public-domain texts by the PocketPolyglot pipeline and are owned by LazyingArt LLC.

**Missing a book?** [Open an issue](https://github.com/lachlanchen/bunko-books/issues/new) and say which one. Public-domain titles only, please.
