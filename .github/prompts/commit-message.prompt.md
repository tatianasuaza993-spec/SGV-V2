# Mensajes de commit — SGV

<!--
  ¿Qué? Guía corta para escribir mensajes de commit.
  ¿Para qué? Que el historial cuente por qué existe cada cambio.
  ¿Impacto? Con mensajes sueltos, `git log` no sirve para rastrear decisiones.
-->

Formato (en inglés, asunto de máximo 72 caracteres):

```
type(scope): short description

What: what was done
For: why it is needed (reference the RF/HU)
Impact: what it affects
```

**Tipos:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `ci`, `perf`.

**Scopes sugeridos:** `auth`, `user`, `institution`, `election`, `candidacy`, `vote`, `result`,
`notification`, `db`, `api`, `ui`, `config`, `test`, `deps`.

Reglas:

- Un commit = un cambio con sentido propio. Si el mensaje necesita un "y", son dos commits.
- Nunca se commitea directo a `main`.
- Si te equivocaste y aún no hiciste push: `git commit --amend`.
