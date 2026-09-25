[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Bunko Books

*Bunko를 위한 다운로드 가능한 공개 도서관.*

[![Reader](https://img.shields.io/badge/Open-Bunko-303F68?style=for-the-badge)](https://lachlan.lazying.art/Bunko/) [![Sponsor](https://img.shields.io/badge/GitHub-Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/lachlanchen)

이 저장소에는 공개 도메인 고전의 완결 판본 150종이 작은 JSON 장으로 들어 있습니다. 글자 위 발음과 문자 없는 것으로 검토한 표지도 함께 제공합니다. Bunko는 독자가 여는 장만 내려받아 오프라인에 저장합니다. 앱 코드는 [Bunko](https://github.com/lachlanchen/Bunko)에 있고, 승인된 책을 추가할 때 앱을 다시 빌드할 필요가 없습니다.

<p align="center"><a href="../assets/classics-clean-2026-09-23.png"><img src="../assets/classics-clean-2026-09-23.png" alt="문자 없는 표지 그림" width="300"></a></p>

## 도서관 구성

| 경로 | 설명 |
| --- | --- |
| [`books/`](../books/) | 출판된 책 폴더: 메타데이터, 권리, 장 파일 |
| [`reader-index.json`](../reader-index.json) | 리더가 사용하는 생성 목록 |
| [`tools/`](../tools/) | 검증기, 목록 생성기, 테스트 |

## 게시와 검증

[도서관 관리](https://lachlan.lazying.art/Bunko/admin/)에서 책 풀 리퀘스트를 준비하거나 Git에서 `books/<id>/`를 편집하세요. 먼저 [출판 안내](https://github.com/lachlanchen/Bunko/blob/main/docs/library-publishing.md)를 읽으세요. 워크플로가 장과 권리 기록을 검사하고 병합 후 `reader-index.json`을 다시 만듭니다. 이 파일을 손으로 수정하지 마세요.

```sh
python3 -m unittest discover -s tools -p 'test_*.py'
python3 tools/catalogue.py --write
```

## 권리와 호환성

각 묶음에는 `meta.json`, `rights.json`, 압축된 장 파일이 필요하며 검토된 문자 없는 표지는 선택 사항입니다. [판본 검토 기록](https://github.com/lachlanchen/Bunko/blob/main/docs/catalogue.md)에 원작 근거가 있습니다. 최종 번역은 Codex가 생성했다고 소유자가 확인했습니다. 캐시된 독자를 위해 내용 기반 이름의 이전 장 파일을 유지하세요. 공개 도메인 상태는 지역마다 다를 수 있습니다.


## 도서관 후원

Bunko Books는 LazyingArt의 공개 도서관입니다. 후원은 목록과 읽기 도구의 유지에 도움이 됩니다.

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 인용

연구에 Bunko Books를 사용한다면 이 저장소를 인용하세요. GitHub는 [CITATION.cff](../CITATION.cff)를 읽어 인용 패널을 표시합니다.

```bibtex
@software{chen_bunko_books_2026,
  author = {Chen, Lachlan},
  title = {Bunko Books: Downloadable Classics Library},
  year = {2026},
  url = {https://github.com/lachlanchen/bunko-books}
}
```

## 수정 제안

누락된 본문, 메타데이터나 표지 오류, 권리 문제는 [책 이슈](https://github.com/lachlanchen/bunko-books/issues/new)로 알려 주세요. 검토 기록은 전 세계 법적 보증이 아닙니다.
## Bunko에서 읽기

서재에는 퍼블릭 도메인 고전 150권과 저자가 공개를 허락한 도서 12권이 있습니다. 물리학 해설, 학습 안내서, 금융 도서, 다국어 여행 안내서 세 권을 포함합니다. 한 언어 또는 여러 언어로 읽을 수 있으며 수식과 그림도 모바일에서 표시됩니다.

[Apple App Store](https://apps.apple.com/app/id6815137919) · [Google Play · 출시 대기 중](https://play.google.com/store/apps/details?id=art.lazying.bunko) · [Web reader](https://lachlan.lazying.art/Bunko/)
