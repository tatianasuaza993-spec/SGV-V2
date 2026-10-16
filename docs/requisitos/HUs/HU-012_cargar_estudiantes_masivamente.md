# HU-012 — Cargar estudiantes masivamente

<!--
  ¿Qué? Historia de usuario asociada al requisito RF-012.
  ¿Para qué? Describir la necesidad desde el punto de vista del usuario y sus escenarios de aceptación.
  ¿Impacto? Sin los escenarios no hay criterio objetivo para dar el requisito por cumplido.
-->

| Campo         | Valor                            |
| ------------- | -------------------------------- |
| **ID**        | HU-012                          |
| **Requisito** | [RF-012](../RFs/RF-012_cargar_estudiantes_masivamente.md) |
| **Rol**       | Administrador                           |

## Historia

Como Administrador deseo cargar masivamente estudiantes mediante un archivo Excel o CSV con la finalidad de registrar a los estudiantes de la institución de forma rápida, sin tener que crearlos uno por uno.

## Escenarios

| #   | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
| --- | ------------------- | --------------- | ----------------------------- |
| 1 | El administrador se encuentra en el módulo de gestión de estudiantes | Selecciona la opción “Cargar estudiantes masivamente” | El sistema muestra la pantalla de carga con las instrucciones, los formatos permitidos (Excel/CSV) y la opción de descargar una plantilla de ejemplo |
| 2 | El administrador está en la pantalla de carga masiva | Selecciona un archivo Excel o CSV con la estructura correcta y presiona “Cargar” | El sistema recibe el archivo y comienza la validación del formato y de los datos de cada fila |
| 3 | El administrador está en la pantalla de carga masiva | Intenta subir un archivo que no es Excel ni CSV (por ejemplo PDF o imagen) | El sistema rechaza el archivo y muestra un mensaje indicando que solo se aceptan los formatos .xlsx, .xls y .csv |
| 4 | El administrador sube un archivo al que le faltan columnas obligatorias (nombres, documento, curso, etc.) | Presiona “Cargar” | El sistema cancela la carga e indica cuáles columnas obligatorias no se encontraron, sin registrar ningún estudiante |
