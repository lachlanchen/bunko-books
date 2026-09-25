[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Bunko Books

*Открытая загружаемая библиотека для Bunko.*

[![Reader](https://img.shields.io/badge/Open-Bunko-303F68?style=for-the-badge)](https://lachlan.lazying.art/Bunko/) [![Sponsor](https://img.shields.io/badge/GitHub-Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/lachlanchen)

Здесь размещены 150 полных изданий классики общественного достояния: компактные главы JSON с чтениями руби и проверенными иллюстрированными обложками без текста. Bunko загружает только открываемые главы и сохраняет их для чтения без сети. Код приложения находится в [Bunko](https://github.com/lachlanchen/Bunko); добавление одобренной книги не требует новой сборки.

<p align="center"><a href="../assets/classics-clean-2026-09-23.png"><img src="../assets/classics-clean-2026-09-23.png" alt="Иллюстрированная обложка без текста" width="300"></a></p>

## Содержимое библиотеки

| Путь | Описание |
| --- | --- |
| [`books/`](../books/) | Папки книг: метаданные, права и главы |
| [`reader-index.json`](../reader-index.json) | Производный каталог для читалки |
| [`tools/`](../tools/) | Валидатор, сборщик каталога и тесты |

## Публикация и проверка

Подготовьте запрос на добавление книги через [управление библиотекой](https://lachlan.lazying.art/Bunko/admin/) или измените `books/<id>/` в Git. Сначала прочитайте [руководство по публикации](https://github.com/lachlanchen/Bunko/blob/main/docs/library-publishing.md). Процесс проверяет главы и права, затем пересоздаёт `reader-index.json` после слияния; не редактируйте индекс вручную.

```sh
python3 -m unittest discover -s tools -p 'test_*.py'
python3 tools/catalogue.py --write
```

## Права и совместимость

Каждому пакету нужны `meta.json`, `rights.json` и компактные главы; проверенная обложка без текста необязательна. [Проверка изданий](https://github.com/lachlanchen/Bunko/blob/main/docs/catalogue.md) фиксирует сведения об оригинале. Владелец подтверждает, что окончательные переводы создал Codex. Сохраняйте старые главы с именами по содержимому для читателей с кешем. Статус общественного достояния различается по странам.


## Поддержать библиотеку

Bunko Books — открытая библиотека LazyingArt. Поддержка помогает сохранять каталог и инструменты чтения:

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Цитирование

Если вы используете Bunko Books в исследовании, цитируйте этот репозиторий. GitHub читает [CITATION.cff](../CITATION.cff) и показывает панель цитирования.

```bibtex
@software{chen_bunko_books_2026,
  author = {Chen, Lachlan},
  title = {Bunko Books: Downloadable Classics Library},
  year = {2026},
  url = {https://github.com/lachlanchen/bunko-books}
}
```

## Исправления

О пропущенном тексте, ошибках метаданных или обложки, а также о проблемах с правами сообщайте через [issue книги](https://github.com/lachlanchen/bunko-books/issues/new). Проверка задокументирована, но не является юридической гарантией для всех стран.
## Читать в Bunko

В библиотеке теперь 150 классических произведений из общественного достояния и 12 изданий, разрешённых автором: заметки по физике, учебное руководство, книги о финансах и три многоязычных путеводителя. Книги доступны на одном или нескольких языках; формулы и иллюстрации сохраняются в мобильном чтении.

[Apple App Store](https://apps.apple.com/app/id6815137919) · [Google Play · публикация ожидается](https://play.google.com/store/apps/details?id=art.lazying.bunko) · [Web reader](https://lachlan.lazying.art/Bunko/)

На шесть независимых томов по физике по-прежнему распространяется [GPL-3.0](../licenses/GPL-3.0.txt); ссылки на редактируемые исходники приведены в записях о правах.
