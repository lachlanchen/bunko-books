[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Bunko Books

*La biblioteca abierta y descargable de Bunko.*

[![Reader](https://img.shields.io/badge/Open-Bunko-303F68?style=for-the-badge)](https://lachlan.lazying.art/Bunko/) [![Sponsor](https://img.shields.io/badge/GitHub-Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/lachlanchen)

Este repositorio alberga 150 ediciones completas de clásicos de dominio público en capítulos JSON compactos, con lecturas ruby y cubiertas ilustradas revisadas para que no contengan texto. Bunko descarga solo los capítulos abiertos y los guarda sin conexión. La aplicación está en [Bunko](https://github.com/lachlanchen/Bunko); añadir aquí un libro aprobado no exige reconstruirla.

<p align="center"><a href="../assets/classics-clean-2026-09-23.png"><img src="../assets/classics-clean-2026-09-23.png" alt="Cubierta ilustrada sin texto" width="300"></a></p>

## Dentro de la biblioteca

| Ruta | Descripción |
| --- | --- |
| [`books/`](../books/) | Carpetas de libros: metadatos, derechos y capítulos |
| [`reader-index.json`](../reader-index.json) | Catálogo derivado que utiliza el lector |
| [`tools/`](../tools/) | Validador, generador del catálogo y pruebas |

## Publicar y validar

Usa [Gestión de biblioteca](https://lachlan.lazying.art/Bunko/admin/) para preparar una solicitud de cambio, o edita `books/<id>/` con Git. Lee antes la [guía de publicación](https://github.com/lachlanchen/Bunko/blob/main/docs/library-publishing.md). El flujo verifica capítulos y derechos y regenera `reader-index.json` tras la integración; no lo edites a mano.

```sh
python3 -m unittest discover -s tools -p 'test_*.py'
python3 tools/catalogue.py --write
```

## Derechos y compatibilidad

Cada paquete necesita `meta.json`, `rights.json` y capítulos compactos; la cubierta revisada y sin texto es opcional. La [auditoría de ediciones](https://github.com/lachlanchen/Bunko/blob/main/docs/catalogue.md) documenta la obra original. El propietario confirma que Codex generó las traducciones finales. Conserva los capítulos antiguos con nombres basados en su contenido para los lectores con caché. El dominio público puede variar por territorio.


## Apoya la biblioteca

Bunko Books es una biblioteca pública de LazyingArt. Tu apoyo ayuda a mantener el catálogo y las herramientas de lectura:

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Cita

Si usas Bunko Books en investigación, cita este repositorio. GitHub lee [CITATION.cff](../CITATION.cff) y muestra la opción de citarlo.

```bibtex
@software{chen_bunko_books_2026,
  author = {Chen, Lachlan},
  title = {Bunko Books: Downloadable Classics Library},
  year = {2026},
  url = {https://github.com/lachlanchen/bunko-books}
}
```

## Correcciones

Para comunicar texto faltante, metadatos erróneos, problemas de cubierta o derechos, [abre una incidencia](https://github.com/lachlanchen/bunko-books/issues/new). La auditoría documenta una revisión, no una certificación legal mundial.
## Leer en Bunko

La biblioteca reúne 150 clásicos de dominio público y 12 ediciones autorizadas por su autor: apuntes de física, una guía de aprendizaje, libros de finanzas y tres guías de viaje multilingües. Cada libro puede tener uno o varios idiomas; el lector móvil conserva las ecuaciones y figuras.

[App Store de Apple](https://apps.apple.com/app/id6815137919) · [Google Play · publicación pendiente](https://play.google.com/store/apps/details?id=art.lazying.bunko) · [Web reader](https://lachlan.lazying.art/Bunko/)

Los seis volúmenes independientes de física conservan la licencia [GPL-3.0](../licenses/GPL-3.0.txt); sus registros de derechos enlazan las fuentes editables.
