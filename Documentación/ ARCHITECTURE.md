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


```
Cliente / Simulador de Sistema Externo
            |
            v
        API REST  ----->  SQLite
            ^
            |
     Ejecutor de Automatización
```

## Notas
- Este proyecto es intencionalmente *documentation-first* y liviano.
- El simulador existe para demostrar patrones de integración sin dependencias externas.
