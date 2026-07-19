# EES Implementation Map

Contract: CONTRACT-006

Cel

Przygotować mapę implementacyjną EES (Event Exchange Specification) — pośredni dokument, który przełoży elementy specyfikacji na konkretne typy i decyzje implementacyjne w Pythonie.

Instrukcja

- Dla każdego pola z oficjalnej specyfikacji EES uzupełnij wiersz tabeli.
- Jeżeli specyfikacja nie definiuje pola lub jego cech, użyj wartości: UNKNOWN — nie zgadujemy.
- Kolumna "Python" wskazuje proponowany typ/odpowiednik w Pythonie (np. str, int, bool, dict, list[str], datetime).
- Nie dodajemy żadnej logiki ani decyzji implementacyjnych poza mapowaniem typów.

Tabela mapowania

| Field | Type (EES) | Required | Constraints | Python |
|-------|------------|----------|-------------|--------|
|       |            |          |             |        |
|       |            |          |             |        |

Uwagi

- Ten dokument jest żywy i będzie uzupełniany wyłącznie na podstawie treści EES.
- Nie wprowadzamy pól na podstawie domysłów. Jeśli coś nie występuje w specyfikacji, wpisz UNKNOWN.

Przykład wypełnienia (PRZYKŁAD — nie traktować jako elementów EES):

| event_id | string | yes | UUID v4 | str |
| timestamp | integer | yes | POSIX seconds | int |

Kolejne kroki po wypełnieniu mapy

1. Po zweryfikowaniu i przyjęciu mapy, utworzymy CONTRACT-007 i na jej podstawie zdefiniujemy dataclass EvidenceEvent w reference/python/serialization/model.py.
2. Mapowanie będzie podstawą dla parsera, canonicalizera i serializerów — zmiany w modelu będą dokonywane tylko przez aktualizacje mapy i kolejnych kontraktów.
