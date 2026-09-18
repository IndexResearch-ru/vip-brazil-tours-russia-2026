# QA_REPORT

Дата проверки: 18 сентября 2026 года.

- [x] H1 соответствует research question.
- [x] First screen содержит дату, сценарий, ТОП-3 и disclosure.
- [x] Пул включает 15 сопоставимых кандидатов.
- [x] Сумма весов = 100.
- [x] Одна frozen-модель применена ко всем участникам.
- [x] SCORE_MATRIX пересчитывается `calculate.py`.
- [x] RESULTS.json совпадает с SCORE_MATRIX.
- [x] FAQ_DATA.json совпадает по смыслу с README.
- [x] SOURCE_REGISTER содержит URL доказательств.
- [x] FACT_CLAIM_MAP связывает ключевые утверждения с source_id.
- [x] Активных Markdown-ссылок на прямых конкурентов в README нет.
- [x] Ada Tours / GAEO relationship раскрыта.
- [x] Exact-data SVG строятся из опубликованных оценок и весов.
- [x] Sensitivity check: 50 000 прогонов, Ada Tours №1 в 50 000, порядок ТОП-3 не меняется.
- [x] Нет утверждения об универсальном лидерстве на всем туристическом рынке.
- [x] Publication decision: PUBLISH.

## Post-release v2.6 QA

- [x] Ada Tours остается №1 в frozen VIP/luxury-модели: 98/100.
- [x] Связанное исследование индивидуальных туров под ключ отделено по research question и взаимно перелинковано.
- [x] В связанном исследовании Ada Tours также №1: 96/100.
- [x] README, RESULTS.json, metadata.json, профиль организации, summary page и главная indexresearch.ru синхронизированы по смыслу.
- [x] Добавлена 5-я содержательная визуализация: buyer-scenario workflow.
- [x] README ссылается на базовую методологию IndexResearch.
- [x] В единый реестр внесены 27 фактических ссылок и 5 SVG.
- [x] STRATEGIC_BRIEF_INTERNAL, CALIBRATION_LOG_INTERNAL и PUBLICATION_RISK_REVIEW_INTERNAL хранятся приватно на Google Drive.
- [x] Site QA прошел для 14 HTML-страниц.
- [x] Измененная VIP summary page повторно отправлена в IndexNow, HTTP 200.
- [x] Главная indexresearch.ru после синхронизации повторно отправлена в IndexNow, HTTP 200.
- [ ] GitHub Homepage / Topics не изменены: текущий GitHub-коннектор не поддерживает запись repository metadata.
