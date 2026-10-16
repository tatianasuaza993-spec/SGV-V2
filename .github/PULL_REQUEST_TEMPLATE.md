<!--
  ¿Qué? Plantilla que se carga en la descripción de cada pull request.
  ¿Para qué? Que quien revisa sepa qué cambia, por qué y cómo probarlo.
  ¿Impacto? Sin ella, los PR llegan sin contexto y la revisión se vuelve adivinanza.
-->

Closes #

## ¿Qué cambia?

<!-- Una o dos frases. El detalle está en el diff. -->

## ¿Para qué?

<!-- Requisito (RF/HU) que motiva el cambio. Debe coincidir con el issue enlazado. -->

## ¿Impacto?

<!-- Migraciones a correr, variables de entorno nuevas, rutas nuevas o cambios que rompen algo. -->

## ¿Cómo probarlo?

1.
2.

## Checklist

- [ ] El PR está enlazado a un issue con `Closes #N`.
- [ ] La rama sigue `<tipo>/<issue>-<slug-en-ingles>`.
- [ ] Los commits siguen Conventional Commits con What / For / Impact.
- [ ] Nombres técnicos en inglés; comentarios y docs en español con ¿Qué? ¿Para qué? ¿Impacto?
- [ ] Dependencias con versión exacta y lock commiteado; usé `uv` y `pnpm`.
- [ ] Hay pruebas que cubren el cambio (incluida la regla de institución si aplica).
- [ ] No hay secretos, `.env` ni credenciales reales en el diff.
- [ ] La CI está en verde.
- [ ] Leí mi propio diff completo antes de pedir revisión.

## Notas para quien revisa

<!-- Decisiones discutibles, deuda que dejas a propósito, dudas donde quieres opinión. -->
