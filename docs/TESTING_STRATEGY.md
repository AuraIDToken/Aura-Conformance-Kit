# TESTING STRATEGY

Contract: CONTRACT-002

Cel

Określić rodzaje testów, ich zakres i sposób organizacji, aby zapewnić powtarzalność, deterministyczność i możliwość wykonania TCK (Test Compatibility Kit).

1. Unit tests
- Małe, szybkie testy skupione na pojedynczych funkcjach/klasach.
- Pytest jako runner.
- Testy jednostkowe powinny nie zależeć od środowiska zewnętrznego i być deterministyczne.

2. Integration tests
- Testy łączące kilka komponentów (np. parsowanie + walidacja).
- Mogą używać zasobów (pliki referencyjne) umieszczonych w katalogu tests/resources.

3. Determinism tests
- Testy walidujące deterministyczność krytycznych operacji (np. serializacja) przy stałym seedzie.
- Wymagają kontrolowania generatorów losowych i środowiska wykonania.

4. TCK (Test Compatibility Kit)
- Zestaw testów i zasobów określających minimalne wymagania zgodności implementacji z Aura.
- TCK będzie oddzielnym artefaktem (folder /tck lub oddzielne repo w przyszłości). TCK musi mieć opisany Oracle (patrz punkt Oracle), zestaw testów i oczekiwane wyniki.

5. Oracle
- Oracle definiuje, jak interpretować wyniki testów TCK (co jest poprawne, co nie).
- Na tym etapie Oracle jest koncepcyjnym elementem — nie implementujemy go teraz, ale opisujemy w TCK jak Oracle powinien się zachowywać.

6. CI
- W przyszłości CI będzie uruchamiał: unit, determinism, integration tests i TCK na żądanie.
- Na razie nie dodajemy plików CI do repozytorium.

7. Organizacja testów
- Struktura testów: tests/unit, tests/integration, tests/determinism, tests/tck (wraz z zasobami w tests/resources).
- Standard nazewnictwa: test_*.py dla modułów testowych.

Uwagi końcowe
- Ten dokument jest dokumentem roboczym — będziemy go rozszerzać wraz z rozwojem projektu i potrzebami TCK.