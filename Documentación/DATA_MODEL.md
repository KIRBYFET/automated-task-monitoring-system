# Modelo de Datos – Sistema de monitoreo automatizado de tareas

## Entidad: Task

Una **Task** representa una actividad operativa que es monitoreada por el sistema de automatización.

##  Campos
- `id` (int, PK)  
- `title` (string, requerido)  
- `description` (string, opcional)  
- `status` (enum): `PENDING | DONE | OVERDUE`  
- `priority` (enum): `LOW | MEDIUM | HIGH`  
- `due_at` (datetime ISO, opcional): fecha límite  
- `overdue_at` (datetime ISO, opcional): se establece cuando la tarea pasa a `OVERDUE`  
- `source` (string): `manual | simulator | ...`  
- `external_id` (string, opcional): ID proveniente de un sistema externo  
- `created_at` (datetime ISO)  
- `updated_at` (datetime ISO)  

### Reglas de negocio principales
- Una tarea se vuelve **vencida (OVERDUE)** cuando:
  - `status == PENDING`
  - `due_at < now()`
- El **Ejecutor de Automatización (Automation Runner)** es responsable de cambiar el estado de las tareas a `OVERDUE`.
- El **Simulador** puede cerrar tareas estableciendo `status = DONE`.
