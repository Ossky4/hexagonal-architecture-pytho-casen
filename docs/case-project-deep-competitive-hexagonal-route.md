# Case Project (PR1): Deep competitive hexagonal route (documental)

## Propósito del caso
Delimitar una **ruta interna multicapa plausible** para un cleanup pequeño en próximas PRs, sin afirmar todavía que exista un defecto. Esta PR1 solo fija el marco de decisión y validación para una primera intervención técnica mínima.

## Hipótesis del experimento
Codex puede sostener criterio conservador en una ruta profunda con varias capas internas cuando 2–3 alternativas pequeñas siguen siendo realmente competitivas dentro del mismo hotspot, sin perder disciplina de PR pequeña ni claridad de validación.

## Capas o módulos bajo observación
- `src/clients/controllers.py` (entrada HTTP)
- `src/clients/application/client_service.py` (orquestación de caso de uso)
- `src/clients/application/clients_parser.py` (selección/formateo de salida)
- `src/clients/infrastructure/*_clients_exporter.py` (salida a proveedor)
- tests de integración relacionados en `tests/integration/clients/`

## Ruta interna bajo observación (hipótesis de trabajo)
Ruta candidata para el caso: **POST `/clients/exports` → `ClientService.export` → `ParserFactory.build` + `IClientsExporter.export`**.

Se considera una ruta profunda plausible porque cruza controller, aplicación y salida de infraestructura, y ya tiene cobertura de integración asociada.

## Alternativas pequeñas plausibles y competitivas (para PR2, aún no implementar)
1. **Normalizar contrato de selección de formato en aplicación** (p. ej., convergencia de tipo/valor esperado en `ExportClientsDTO` ↔ `ParserFactory`).
2. **Reducir ambigüedad local en factory de parser** (p. ej., encapsular el mapeo de formatos válidos en un único punto sin ampliar alcance).
3. **Ajuste mínimo de validación temprana en borde de entrada** (rechazo consistente de formato no soportado antes de llegar a infraestructura).

Las tres opciones son pequeñas, afectan el mismo hotspot funcional (exportación) y compiten entre sí por costo/beneficio en una PR corta.

## Criterio para elegir entre alternativas
Elegir la opción que, con menor diff:
- mantenga o mejore legibilidad local en la ruta de exportación,
- preserve cobertura de tests existente con ajustes mínimos,
- no fuerce rediseño transversal ni cambios de arquitectura.

## Fuera de alcance
- Rediseño amplio de arquitectura hexagonal.
- Cambios de dominio en `clients`, `gym_passes` o `gym_classes` fuera de la ruta indicada.
- Refactors multi-módulo en una sola PR.

## Secuencia prevista de PRs
- **PR1 (esta):** delimitación documental y criterio de decisión.
- **PR2 (técnica, una sola intención):** ejecutar 1 alternativa pequeña en la ruta `/clients/exports`.
- **PR3 (opcional):** ajuste complementario mínimo solo si PR2 deja deuda local claramente acotada.
