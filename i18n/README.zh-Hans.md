[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Bunko Books

*支撑 Bunko 的开放、可下载古典书库。*

[![Reader](https://img.shields.io/badge/Open-Bunko-303F68?style=for-the-badge)](https://lachlan.lazying.art/Bunko/) [![Sponsor](https://img.shields.io/badge/GitHub-Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/lachlanchen)

本仓库存放 150 种完整的公版古典版本，按小型 JSON 章节分发，包含注音与经过检查的无文字插画封面。Bunko 只下载读者打开的章节，并将其缓存供离线阅读。应用代码在 [Bunko](https://github.com/lachlanchen/Bunko)；在此添加审核通过的书籍，不必重新构建应用。

<p align="center"><a href="../assets/classics-clean-2026-09-23.png"><img src="../assets/classics-clean-2026-09-23.png" alt="无文字插画封面" width="300"></a></p>

## 书库内容

| 路径 | 说明 |
| --- | --- |
| [`books/`](../books/) | 已发布书籍目录：元数据、版权与章节 |
| [`reader-index.json`](../reader-index.json) | 供阅读器使用的生成书目 |
| [`tools/`](../tools/) | 验证器、书目生成器及测试 |

## 发布与验证

通过[书库管理页面](https://lachlan.lazying.art/Bunko/admin/)准备书籍拉取请求，或使用 Git 编辑 `books/<id>/`。请先阅读[发布指南](https://github.com/lachlanchen/Bunko/blob/main/docs/library-publishing.md)。工作流会检查每章与版权记录，合并后自动生成 `reader-index.json`；不要手动修改索引。

```sh
python3 -m unittest discover -s tools -p 'test_*.py'
python3 tools/catalogue.py --write
```

## 版权与兼容性

每个书籍包须含 `meta.json`、`rights.json` 与精简章节文件；经过检查的无文字封面可选。[版本审核](https://github.com/lachlanchen/Bunko/blob/main/docs/catalogue.md)记录原著依据。所有者确认最终译文由 Codex 生成。请保留以内容命名的旧章节，供已有缓存的读者使用。公版资格可能因地区不同。


## 支持书库

Bunko Books 是 LazyingArt 的开放书库。你的支持有助于维护书目和阅读工具：

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 引用

如在研究中使用 Bunko Books，请引用此仓库。GitHub 会读取 [CITATION.cff](../CITATION.cff) 并提供引用面板。

```bibtex
@software{chen_bunko_books_2026,
  author = {Chen, Lachlan},
  title = {Bunko Books: Downloadable Classics Library},
  year = {2026},
  url = {https://github.com/lachlanchen/bunko-books}
}
```

## 勘误

如发现正文缺漏、元数据错误、封面问题或版权疑虑，请[提交书籍 issue](https://github.com/lachlanchen/bunko-books/issues/new)。审核记录并非全球通用的法律认证。
