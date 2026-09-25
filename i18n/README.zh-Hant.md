[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Bunko Books

*支撐 Bunko 的開放、可下載古典書庫。*

[![Reader](https://img.shields.io/badge/Open-Bunko-303F68?style=for-the-badge)](https://lachlan.lazying.art/Bunko/) [![Sponsor](https://img.shields.io/badge/GitHub-Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/lachlanchen)

本儲存庫存放 150 種完整的公版古典版本，以小型 JSON 章節分發，包含注音與經檢查的無文字插畫封面。Bunko 只下載讀者開啟的章節，並將其快取供離線閱讀。應用程式程式碼在 [Bunko](https://github.com/lachlanchen/Bunko)；在此加入審核通過的書籍，不必重新建置應用程式。

<p align="center"><a href="../assets/classics-clean-2026-09-23.png"><img src="../assets/classics-clean-2026-09-23.png" alt="無文字插畫封面" width="300"></a></p>

## 書庫內容

| 路徑 | 說明 |
| --- | --- |
| [`books/`](../books/) | 已發布書籍目錄：元資料、版權與章節 |
| [`reader-index.json`](../reader-index.json) | 供閱讀器使用的生成書目 |
| [`tools/`](../tools/) | 驗證器、書目生成器及測試 |

## 發布與驗證

透過[書庫管理頁面](https://lachlan.lazying.art/Bunko/admin/)準備書籍拉取請求，或使用 Git 編輯 `books/<id>/`。請先閱讀[發布指南](https://github.com/lachlanchen/Bunko/blob/main/docs/library-publishing.md)。工作流程會檢查每章與版權紀錄，合併後自動產生 `reader-index.json`；不要手動修改索引。

```sh
python3 -m unittest discover -s tools -p 'test_*.py'
python3 tools/catalogue.py --write
```

## 版權與相容性

每個書籍包須含 `meta.json`、`rights.json` 與精簡章節檔案；經檢查的無文字封面可選。[版本審核](https://github.com/lachlanchen/Bunko/blob/main/docs/catalogue.md)記錄原著依據。擁有者確認最終譯文由 Codex 產生。請保留以內容命名的舊章節，供已有快取的讀者使用。公版資格可能因地區不同。


## 支持書庫

Bunko Books 是 LazyingArt 的開放書庫。你的支持有助於維護書目與閱讀工具：

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 引用

如在研究中使用 Bunko Books，請引用此儲存庫。GitHub 會讀取 [CITATION.cff](../CITATION.cff) 並提供引用面板。

```bibtex
@software{chen_bunko_books_2026,
  author = {Chen, Lachlan},
  title = {Bunko Books: Downloadable Classics Library},
  year = {2026},
  url = {https://github.com/lachlanchen/bunko-books}
}
```

## 勘誤

如發現正文缺漏、元資料錯誤、封面問題或版權疑慮，請[提交書籍 issue](https://github.com/lachlanchen/bunko-books/issues/new)。審核紀錄並非全球通用的法律認證。
## 在 Bunko 閱讀

書庫現有 150 部公共領域經典與 12 部經作者授權的作品：物理學伴讀筆記、學習指南、財經書籍，以及三本多語旅行指南。每本書可有一種或多種語言，公式與插圖也能在手機上閱讀。

[Apple App Store](https://apps.apple.com/app/id6815137919) · [Google Play · 待上架](https://play.google.com/store/apps/details?id=art.lazying.bunko) · [Web reader](https://lachlan.lazying.art/Bunko/)

六部獨立的物理學伴讀筆記仍遵循 [GPL-3.0](../licenses/GPL-3.0.txt)；各書權利記錄連結至可編輯的原始檔。
