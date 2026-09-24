[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Bunko Books

*La bibliothèque ouverte et téléchargeable de Bunko.*

[![Reader](https://img.shields.io/badge/Open-Bunko-303F68?style=for-the-badge)](https://lachlan.lazying.art/Bunko/) [![Sponsor](https://img.shields.io/badge/GitHub-Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/lachlanchen)

Ce dépôt héberge 150 éditions complètes de classiques du domaine public sous forme de petits chapitres JSON, avec lectures ruby et couvertures illustrées vérifiées sans texte. Bunko ne télécharge que les chapitres ouverts et les garde hors ligne. L’application se trouve dans [Bunko](https://github.com/lachlanchen/Bunko) ; ajouter ici un livre approuvé ne demande pas de nouvelle version.

<p align="center"><a href="../assets/classics-clean-2026-09-23.png"><img src="../assets/classics-clean-2026-09-23.png" alt="Couverture illustrée sans texte" width="300"></a></p>

## Dans la bibliothèque

| Chemin | Description |
| --- | --- |
| [`books/`](../books/) | Dossiers des livres : métadonnées, droits et chapitres |
| [`reader-index.json`](../reader-index.json) | Catalogue dérivé utilisé par le lecteur |
| [`tools/`](../tools/) | Validateur, générateur du catalogue et tests |

## Publier et vérifier

Utilisez la [gestion de bibliothèque](https://lachlan.lazying.art/Bunko/admin/) pour préparer une demande de modification, ou modifiez `books/<id>/` avec Git. Lisez d’abord le [guide de publication](https://github.com/lachlanchen/Bunko/blob/main/docs/library-publishing.md). Le workflow vérifie chapitres et droits puis régénère `reader-index.json` après fusion ; ne le modifiez pas à la main.

```sh
python3 -m unittest discover -s tools -p 'test_*.py'
python3 tools/catalogue.py --write
```

## Droits et compatibilité

Chaque lot nécessite `meta.json`, `rights.json` et des chapitres compacts ; une couverture vérifiée sans texte est facultative. L’[audit des éditions](https://github.com/lachlanchen/Bunko/blob/main/docs/catalogue.md) documente l’œuvre originale. Le propriétaire confirme que Codex a produit les traductions finales. Conservez les anciens chapitres nommés selon leur contenu pour les lecteurs avec cache. Le domaine public varie selon les territoires.


## Soutenir la bibliothèque

Bunko Books est une bibliothèque publique LazyingArt. Votre soutien aide à entretenir le catalogue et les outils de lecture :

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Citation

Si vous utilisez Bunko Books dans une recherche, citez ce dépôt. GitHub lit [CITATION.cff](../CITATION.cff) et affiche un panneau de citation.

```bibtex
@software{chen_bunko_books_2026,
  author = {Chen, Lachlan},
  title = {Bunko Books: Downloadable Classics Library},
  year = {2026},
  url = {https://github.com/lachlanchen/bunko-books}
}
```

## Corrections

Pour signaler un texte manquant, une erreur de métadonnées, de couverture ou de droits, [ouvrez un ticket](https://github.com/lachlanchen/bunko-books/issues/new). L’audit est documenté, mais ne vaut pas certification juridique mondiale.
