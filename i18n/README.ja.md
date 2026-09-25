[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Bunko Books

*Bunko を支える、ダウンロード可能な公開書庫。*

[![Reader](https://img.shields.io/badge/Open-Bunko-303F68?style=for-the-badge)](https://lachlan.lazying.art/Bunko/) [![Sponsor](https://img.shields.io/badge/GitHub-Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/lachlanchen)

このリポジトリには、パブリックドメインの古典 150 版を、ルビ情報付きの小さな JSON 章と、文字のないことを確認した表紙画像として収めています。Bunko は開いた章だけを取得し、オフライン用に保存します。アプリ本体は [Bunko](https://github.com/lachlanchen/Bunko) にあり、承認済みの本を追加してもアプリの再ビルドは不要です。

<p align="center"><a href="../assets/classics-clean-2026-09-23.png"><img src="../assets/classics-clean-2026-09-23.png" alt="文字のない表紙イラスト" width="300"></a></p>

## 書庫の内容

| パス | 説明 |
| --- | --- |
| [`books/`](../books/) | 公開書籍のフォルダ：メタデータ、権利、章ファイル |
| [`reader-index.json`](../reader-index.json) | リーダーが使う生成済みカタログ |
| [`tools/`](../tools/) | 検証器、カタログ生成器、テスト |

## 公開と検証

[書庫管理ページ](https://lachlan.lazying.art/Bunko/admin/) で本のプルリクエストを用意するか、Git で `books/<id>/` を編集します。まず [公開ガイド](https://github.com/lachlanchen/Bunko/blob/main/docs/library-publishing.md) を読んでください。ワークフローが章と権利記録を検証し、マージ後に `reader-index.json` を再生成します。この索引を手作業で編集しないでください。

```sh
python3 -m unittest discover -s tools -p 'test_*.py'
python3 tools/catalogue.py --write
```

## 権利と互換性

各バンドルには `meta.json`、`rights.json`、圧縮した章ファイルが必要で、審査済みの文字なし表紙は任意です。[版の調査記録](https://github.com/lachlanchen/Bunko/blob/main/docs/catalogue.md) に原著の根拠を記しています。最終訳は Codex が生成したと所有者が確認しています。キャッシュ済みの読者のため、内容に基づく名前の古い章を残してください。パブリックドメインの範囲は地域で異なります。


## 書庫を支援

Bunko Books は LazyingArt の公開書庫です。支援はカタログと読書ツールの維持に役立ちます。

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 引用

研究で Bunko Books を使う場合は、このリポジトリを引用してください。GitHub は [CITATION.cff](../CITATION.cff) を読み、引用パネルを表示します。

```bibtex
@software{chen_bunko_books_2026,
  author = {Chen, Lachlan},
  title = {Bunko Books: Downloadable Classics Library},
  year = {2026},
  url = {https://github.com/lachlanchen/bunko-books}
}
```

## 訂正

本文の欠落、メタデータや表紙の誤り、権利上の懸念は [書籍の issue](https://github.com/lachlanchen/bunko-books/issues/new) で知らせてください。調査記録は世界共通の法的保証ではありません。
## Bunko で読む

書庫には、パブリックドメインの古典150点に加え、権利を確認した著者自身の版12点を収録しています。物理学の伴読ノート、学習ガイド、金融の本、多言語の旅行ガイド3冊です。単言語・多言語に対応し、数式と図もモバイルで表示します。

[Apple App Store](https://apps.apple.com/app/id6815137919) · [Google Play · 公開待ち](https://play.google.com/store/apps/details?id=art.lazying.bunko) · [Web reader](https://lachlan.lazying.art/Bunko/)
