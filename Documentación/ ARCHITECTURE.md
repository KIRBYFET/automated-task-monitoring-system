# Architecture

## Components
- **REST API (FastAPI)**  
  Exposes CRUD endpoints for tasks and persists data to SQLite.

- **SQLite Database**  
  Stores tasks and their lifecycle fields (status, priority, due dates).

- **Integration Simulator**  
  Simulates an external system emitting:
  - `CREATE` events: create new tasks via the API
  - `CLOSE` events: mark tasks as `DONE` via the API

- **Automation Runner**
  Periodically:
  - Reads pending tasks
  - Detects overdue tasks (`due_at < now`)
  - Marks them as `OVERDUE`
  - Escalates priority to `HIGH` after a threshold time overdue
  - Generates logs and supports reporting via API endpoints

## Diagram (conceptual)

Client / External System Simulator
            |
            v
        REST API  ----->  SQLite
            ^
            |
     Automation Runner

## Notes
- This is intentionally documentation-first and lightweight.
- The simulator exists to demonstrate integration patterns without external dependencies.

---

# Arquitectura

## Componentes
- **API REST (FastAPI)**  
  Expone endpoints CRUD para tareas y persiste los datos en SQLite.

- **Base de datos SQLite**  
  Almacena las tareas y los campos de su ciclo de vida (estado, prioridad, fechas de vencimiento).

- **Simulador de Integración**  
  Simula un sistema externo que emite:
  - Eventos `CREATE`: crean nuevas tareas a través de la API
  - Eventos `CLOSE`: marcan tareas como `DONE` a través de la API

- **Ejecutor de Automatización**
  De forma periódica:
  - Lee tareas pendientes
  - Detecta tareas vencidas (`due_at < now`)
  - Las marca como `OVERDUE`
  - Escala la prioridad a `HIGH` después de un umbral de tiempo vencido
  - Genera logs y soporta reportes a través de endpoints de la API

## Diagrama (conceptual)

Cliente / Simulador de Sistema Externo
            |
            v
        API REST  ----->  SQLite
            ^
            |
     Ejecutor de Automatización

## Notas
- Este proyecto es intencionalmente *documentation-first* y liviano.
- El simulador existe para demostrar patrones de integración sin dependencias externas.
