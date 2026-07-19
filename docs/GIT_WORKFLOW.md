# GIT WORKFLOW

Contract: CONTRACT-002

Cel

Ujednolicenie zasad pracy z gałęziami, commitami i przeglądem kodu. Historia projektu powinna być czytelna i powiązana z kontraktami.

1. Branch model
- main — zawsze zawiera działający, wydany kod (lub w naszym wczesnym etapie — punkt odniesienia). Bez bezpośrednich commitów.
- develop — (opcjonalnie) integracyjna gałąź dla bieżącej pracy zespołu.
- feature/CONTRACT-###-short-desc — każda nowa praca musi zaczynać się od gałęzi feature z numerem kontraktu.
- hotfix/CONTRACT-###-short-desc — poprawki krytyczne.
- release/vMAJOR.MINOR.PATCH — przygotowanie wydania.

2. Commit messages
- Format: CONTRACT-###: Krótki opis (opcjonalnie: scope) — przykład: CONTRACT-002: add development standards and testing strategy
- Każdy commit powiązany z pracą powinien zawierać numer kontraktu w wiadomości.

3. Pull Request i Review
- Każdy feature kończy się Pull Requestem do main (lub develop jeśli używamy develop).
- PR musi mieć co najmniej jedną akceptację od innego developera (code review).
- Opis PR musi zawierać: powiązanie z kontraktem, krótkie streszczenie zmian, instrukcje testowe.

4. Merge
- Preferujemy squash merge dla zachowania czytelności historii (jeden commit per kontrakt/PR), jednak dopuszczalne są merge commits dla wieloczęściowych integracji — decyzję podejmuje autor PR w porozumieniu z reviewerami.
- Release tagowane semver (vMAJOR.MINOR.PATCH).

5. Release
- Wydania robimy przez pull request na main z gałęzi release/* i oznaczamy tagiem.
- Changelog generowany ręcznie w początkowej fazie.

6. Inne
- Nie merguj bez numeru kontraktu w commitach.
- Brak bezpośrednich commitów do main.

Uwagi
- Workflow minimalny i dostosowalny. Z czasem dodamy szablony PR i automatyczne kontrole (linters, tests) w CI.