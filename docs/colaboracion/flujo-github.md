# 🔁 Flujo de trabajo en GitHub — SGV

<!--
  ¿Qué? Guía del ciclo de colaboración del equipo: issue → rama → commits → pull request → revisión → merge.
  ¿Para qué? Que el trabajo de las dos personas del equipo sea trazable, revisado y verificable.
  ¿Impacto? Sin este flujo, el historial de `main` queda en commits sueltos de una sola cuenta
  y no hay evidencia de revisión (ítem 14 de la lista de chequeo T7).
-->

> Basado en la guía del proyecto de referencia
> [`ergrato-dev/proyecto-be_fastapi-fe_react`](https://github.com/ergrato-dev/proyecto-be_fastapi-fe_react) (CC BY-NC-SA 4.0).

---

## 1. La cadena de trazabilidad

```
RF/HU documentada → Issue → Rama → Commits → Pull Request → Revisión → Merge
```

Cada línea de código debe poder rastrearse hasta el requisito que la motivó. Los requisitos
están en [`docs/requisitos/`](../requisitos/README.md).

## 2. Reglas del equipo

- Somos **dos personas**: Sandy Tatiana Suaza Ramos y Santiago Alejandro Peña Gironza.
- **Cada una trabaja y hace commit desde su propia cuenta de GitHub**, y **la otra revisa y aprueba** cada pull request.
- Nadie sube directo a `main`.
- Cada issue tiene **un solo responsable**, para no tocar los mismos archivos a la vez.

### Proteger `main` (una sola vez, quien administra el repositorio)

En GitHub: *Settings → Rules → Rulesets* sobre `main`:

- ✅ Require a pull request before merging, con **1 aprobación**.
- ✅ Require status checks to pass (los checks `Backend` y `Frontend` de la CI).
- ✅ Require branches to be up to date before merging.

Agregar a la otra persona como colaboradora en *Settings → Collaborators*.

## 3. Ciclo paso a paso

| Paso                | Terminal                                      |
| ------------------- | --------------------------------------------- |
| 1. Crear el issue   | `gh issue create`                             |
| 2. Asignarlo        | `gh issue edit 12 --add-assignee @me`         |
| 3. Crear la rama    | `git switch -c feat/12-election-states`       |
| 4. Trabajar         | `git add -p && git commit`                    |
| 5. Publicar         | `git push -u origin feat/12-election-states`  |
| 6. Abrir el PR      | `gh pr create`                                |
| 7. Ver la CI        | `gh pr checks --watch`                        |
| 8. Revisar          | `gh pr diff` (la otra persona)                |
| 9. Mergear          | `gh pr merge --squash --delete-branch`        |
| 10. Volver a `main` | `git switch main && git pull`                 |

## 4. Ramas

```
<tipo>/<número-de-issue>-<descripción-corta-en-inglés>
```

```bash
feat/12-election-states        # ✅
fix/27-duplicate-vote          # ✅
docs/31-collaboration-guide    # ✅

nueva-rama                     # ❌ no dice nada
feat/estados-eleccion          # ❌ el nombre va en inglés
```

## 5. Commits

Ver [`.github/prompts/commit-message.prompt.md`](../../.github/prompts/commit-message.prompt.md).
Un commit = un cambio con sentido propio. Nunca commitear `.env`.

## 6. Pull requests

- La descripción lleva `Closes #N`: al mergear, GitHub cierra el issue solo.
- Se usa **squash and merge** para dejar un commit por cambio en `main`.
- **Rojo en la CI = no se mergea.**

## 7. Cómo revisar el PR de la otra persona

Qué mirar, en este orden:

1. ¿Hace lo que dice el issue y cumple sus criterios de aceptación?
2. ¿Hay pruebas que lo respalden?
3. ¿Se entiende sin que el autor lo explique?
4. ¿Rompe algo que ya funcionaba? ¿Respeta el aislamiento por institución y el secreto del voto?
5. Estilo y nombres, solo al final.

Comenta el código, no a la persona. Al terminar elige **Comment**, **Approve** o **Request changes**.

## 8. Mantener la rama al día

```bash
git fetch origin
git rebase origin/main
git push --force-with-lease   # solo en tu rama de trabajo, nunca en main
```

Si el rebase se complica: `git rebase --abort`.

## 9. Etiquetas

```bash
gh label create "type:feat"  --color 0E8A16 --description "Funcionalidad nueva"
gh label create "type:bug"   --color D73A4A --description "Algo no funciona"
gh label create "type:docs"  --color 0075CA --description "Documentación o mejora"
gh label create "area:be"    --color 5319E7 --description "Backend (be/)"
gh label create "area:fe"    --color 1D76DB --description "Frontend (fe/)"
gh label create "area:db"    --color 8B4513 --description "Modelos y migraciones"
gh label create "prio:alta"  --color B60205 --description "Prioridad alta"
gh label create "prio:media" --color FBCA04 --description "Prioridad media"
gh label create "prio:baja"  --color C2E0C6 --description "Prioridad baja"
gh label create "bloqueado"  --color 000000 --description "Bloqueado por otra tarea"
```

## 10. Errores comunes

| Error                                 | Por qué duele                                        | Qué hacer                                   |
| ------------------------------------- | ---------------------------------------------------- | ------------------------------------------- |
| Commitear directo en `main`           | Sin PR no hay revisión, CI ni historial de por qué    | Rama siempre; proteger `main`               |
| PR con 40 archivos y varias funciones | Nadie lo revisa de verdad                             | Un issue = un PR                            |
| Mergear con la CI en rojo             | `main` queda roto para las dos                        | Corregir y volver a hacer push              |
| Usar `npm`                            | Genera `package-lock.json` y rompe el lock de `pnpm`  | Siempre `pnpm`                              |
| Commitear el `.env`                   | Filtra credenciales; el historial no olvida           | Solo `.env.example`                         |
| Cerrar el issue a mano                | Se pierde el vínculo issue ↔ PR                       | `Closes #N` en el PR                        |
