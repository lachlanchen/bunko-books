[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Bunko Books

*Die offene, herunterladbare Bibliothek hinter Bunko.*

[![Reader](https://img.shields.io/badge/Open-Bunko-303F68?style=for-the-badge)](https://lachlan.lazying.art/Bunko/) [![Sponsor](https://img.shields.io/badge/GitHub-Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/lachlanchen)

Dieses Repository enthält 150 vollständige Ausgaben gemeinfreier Klassiker als kompakte JSON-Kapitel mit Ruby-Lesungen und geprüften textfreien Illustrationscovern. Bunko lädt nur geöffnete Kapitel und speichert sie offline. Die App liegt in [Bunko](https://github.com/lachlanchen/Bunko); ein neues freigegebenes Buch benötigt keinen neuen App-Build.

[![Textfreies illustriertes Cover](../assets/classics-clean-2026-09-23.png)](../assets/classics-clean-2026-09-23.png)

## In der Bibliothek

| Pfad | Beschreibung |
| --- | --- |
| [`books/`](../books/) | Buchordner: Metadaten, Rechte und Kapitel |
| [`reader-index.json`](../reader-index.json) | Abgeleiteter Katalog für den Reader |
| [`tools/`](../tools/) | Validator, Kataloggenerator und Tests |

## Veröffentlichen und prüfen

Bereite über die [Bibliotheksverwaltung](https://lachlan.lazying.art/Bunko/admin/) einen Buch-Pull-Request vor oder bearbeite `books/<id>/` mit Git. Lies zuerst den [Veröffentlichungsleitfaden](https://github.com/lachlanchen/Bunko/blob/main/docs/library-publishing.md). Der Workflow prüft Kapitel und Rechte und erzeugt `reader-index.json` nach dem Merge neu; bearbeite diesen Index nicht manuell.

```sh
python3 -m unittest discover -s tools -p 'test_*.py'
python3 tools/catalogue.py --write
```

## Rechte und Kompatibilität

Jedes Paket braucht `meta.json`, `rights.json` und kompakte Kapiteldateien; ein geprüftes textfreies Cover ist optional. Die [Ausgabenprüfung](https://github.com/lachlanchen/Bunko/blob/main/docs/catalogue.md) dokumentiert das Originalwerk. Laut Eigentümer stammen die endgültigen Übersetzungen von Codex. Behalte ältere inhaltsadressierte Kapitel für Leser mit Cache. Gemeinfreiheit kann je nach Gebiet variieren.


## Bibliothek unterstützen

Bunko Books ist eine öffentliche LazyingArt-Bibliothek. Unterstützung hilft beim Erhalt des Katalogs und der Lese-Werkzeuge:

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Zitieren

Wenn du Bunko Books für Forschung nutzt, zitiere dieses Repository. GitHub liest [CITATION.cff](../CITATION.cff) und zeigt eine Zitierfunktion an.

```bibtex
@software{chen_bunko_books_2026,
  author = {Chen, Lachlan},
  title = {Bunko Books: Downloadable Classics Library},
  year = {2026},
  url = {https://github.com/lachlanchen/bunko-books}
}
```

## Korrekturen

Fehlenden Text, falsche Metadaten, Cover-Probleme oder Rechtebedenken kannst du als [Buch-Issue](https://github.com/lachlanchen/bunko-books/issues/new) melden. Die dokumentierte Prüfung ist keine weltweite Rechtsbescheinigung.
