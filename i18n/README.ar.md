[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Bunko Books

*المكتبة المفتوحة القابلة للتنزيل خلف Bunko.*

[![Reader](https://img.shields.io/badge/Open-Bunko-303F68?style=for-the-badge)](https://lachlan.lazying.art/Bunko/) [![Sponsor](https://img.shields.io/badge/GitHub-Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/lachlanchen)

يضم هذا المستودع 185 طبعة معتمدة في فصول JSON مدمجة، مع قراءات روبي وأغلفة مراجعة حيثما توفرت. يحمّل Bunko الفصول المفتوحة فقط ويخزنها للقراءة دون اتصال. يوجد التطبيق في [Bunko](https://github.com/lachlanchen/Bunko)، ولا تتطلب إضافة كتاب معتمد هنا بناء تطبيق جديد.

<p align="center"><a href="../assets/classics-clean-2026-09-23.png"><img src="../assets/classics-clean-2026-09-23.png" alt="غلاف مصور بلا نص" width="300"></a></p>

## داخل المكتبة

| المسار | الوصف |
| --- | --- |
| [`books/`](../books/) | مجلدات الكتب المنشورة: البيانات والحقوق والفصول |
| [`reader-index.json`](../reader-index.json) | الفهرس المشتق الذي يستخدمه القارئ |
| [`tools/`](../tools/) | أداة التحقق وبناء الفهرس والاختبارات |

## النشر والتحقق

استخدم [إدارة المكتبة](https://lachlan.lazying.art/Bunko/admin/) لإعداد طلب إضافة كتاب، أو عدّل `books/<id>/` عبر Git. اقرأ [دليل النشر](https://github.com/lachlanchen/Bunko/blob/main/docs/library-publishing.md) أولاً. تتحقق عملية GitHub من الفصول والحقوق ثم تعيد إنشاء `reader-index.json` بعد الدمج؛ لا تعدّل الفهرس يدوياً.

```sh
python3 -m unittest discover -s tools -p 'test_*.py'
python3 tools/catalogue.py --write
```

## الحقوق والتوافق

تحتاج كل حزمة إلى `meta.json` و`rights.json` وملفات فصول مدمجة؛ والغلاف المراجع الخالي من النص اختياري. يسجل [تدقيق الطبعات](https://github.com/lachlanchen/Bunko/blob/main/docs/catalogue.md) أساس العمل الأصلي. تُسجّل مصادر الترجمات وشروط استخدامها في ملف الحقوق لكل حزمة. احتفظ بالفصول القديمة ذات الأسماء المبنية على المحتوى للقراء ذوي النسخ المخزنة. قد تختلف حالة الملك العام حسب الإقليم.


## ادعم المكتبة

Bunko Books مكتبة عامة من LazyingArt. يساعد الدعم في صيانة الفهرس وأدوات القراءة:

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## الاقتباس

إذا استخدمت Bunko Books في بحثك فاستشهد بهذا المستودع. يقرأ GitHub ملف [CITATION.cff](../CITATION.cff) ويعرض لوحة الاقتباس.

```bibtex
@software{chen_bunko_books_2026,
  author = {Chen, Lachlan},
  title = {Bunko Books: Downloadable Classics Library},
  year = {2026},
  url = {https://github.com/lachlanchen/bunko-books}
}
```

## التصحيحات

للإبلاغ عن نص ناقص أو خطأ بيانات أو مشكلة غلاف أو حقوق، [افتح بلاغاً للكتاب](https://github.com/lachlanchen/bunko-books/issues/new). التدقيق موثق، لكنه ليس شهادة قانونية عالمية.
## اقرأ Bunko

تضم المكتبة 185 طبعة معتمدة، تشمل الكلاسيكيات وملاحظات الفيزياء وكتب التعلم والمال وأدلة السفر متعددة اللغات. تتوفر الكتب بلغة واحدة أو عدة لغات، مع الحفاظ على المعادلات والصور على الهاتف.

[متجر Apple](https://apps.apple.com/app/id6815137919) · [Google Play · النشر قيد الانتظار](https://play.google.com/store/apps/details?id=art.lazying.bunko) · [Web reader](https://lachlan.lazying.art/Bunko/)

تحتفظ كتب الفيزياء التسعة عشر المستقلة بشروط [GPL-3.0](../licenses/GPL-3.0.txt)، وتشير سجلات الحقوق إلى مصادرها القابلة للتحرير.
