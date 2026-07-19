# CODING STANDARD

Contract: CONTRACT-002

Cel

Ustalenie podstawowych reguł stylu i praktyk programistycznych obowiązujących w repozytorium aura-conformance-kit. Reguły mają być zwarte, praktyczne i możliwe do automatycznego egzekwowania w dalszym etapie (linter, formatter).

1. Nazewnictwo
- Moduły i pliki: snake_case (np. my_module.py).
- Funkcje i zmienne: snake_case.
- Klasy: PascalCase.
- Stałe modułowe: UPPER_SNAKE_CASE.
- Branch/PR: branch feature powinien zawierać numer kontraktu: feature/CONTRACT-###-short-desc.

2. Dataclasses
- Preferować @dataclass dla prostych struktur danych.
- Dataclass powinny być niemutowalne, gdy to możliwe (frozen=True) — jeśli wymagana mutacja, uzasadnić decyzję.

3. Typing
- Używać pełnego typingu publicznych API (type hints) — mypy/pyright w późniejszym etapie.
- Unikać typu Any w interfejsach; gdy konieczne, dodać komentarz uzasadniający.

4. Enumy
- Używać enum.Enum (lub IntEnum tam gdzie konieczne) dla wartości dyskretnych.
- Enumy definiować w osobnych modu��ach, jeśli są współdzielone między komponentami.

5. Wyjątki
- Definiować własne hierarchie wyjątków bazujące na jednym wyjątku projektu (np. AuraError).
- Nie łapać wyjątku Exception globalnie — obsługiwać konkretne wyjątki.

6. Komentarze i docstringi
- Wszystkie publiczne klasy i funkcje muszą mieć docstring zgodny z Google/NumPy style (dokładny styl do ustalenia później).
- Krótkie komentarze inline tylko gdy wyjaśniają „dlaczego”, nie „co”.

7. Importy
- Importy grupować: standard lib, zewnętrzne, lokalne.
- Używać importów względnych wewnątrz pakietów, gdy to zasadne.

8. Formatowanie
- Formatowanie kodu: Black (ustawienia domyślne) — w przyszłości dodać konfigurację pre-commit.
- Maksymalna długość linii: 88 (domyślne Black).

Uwagi końcowe
- Ten dokument ma charakter żywy — będziemy go rozszerzać i doprecyzowywać podczas pierwszych PR-ów.