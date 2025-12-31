# Sistema automatizado de monitoreo de tareas

Proyecto de portafolio - **Kirbyfet**.

Un sistema backend liviano que demuestra cómo las tareas operativas pueden ser ingeridas desde un sistema externo, monitoreadas automáticamente, escaladas cuando están vencidas y reportadas a través de una API REST.

---

## 🎯 Propósito del proyecto

Este proyecto simula un servicio backend interno del mundo real utilizado para:

- Rastrear tareas operativas  
- Integrarse con sistemas externos vía API  
- Detectar automáticamente trabajo vencido  
- Escalar prioridades según reglas de negocio  
- Generar reportes y registros (logs)

El enfoque está en la **arquitectura backend, patrones de integración y automatización**, no en la interfaz de usuario.

---

## 🧩 Componentes del sistema

### 1. API REST
- Operaciones CRUD para tareas  
- Endpoints de reportes  
- Persistencia en SQLite  

### 2. Simulador de Integración
- Simula un sistema externo  
- Emite eventos de tareas `CREATE` y `CLOSE` vía API  

### 3. Ejecutor de Automatización
- Monitorea tareas periódicamente  
- Marca tareas como `OVERDUE`  
- Escala la prioridad  
- Escribe logs de automatización  

---

## 🏗️ Arquitectura y diseño

La documentación del diseño del sistema se encuentra en el directorio `docs/`:

- Arquitectura: `Documentación/ARCHITECTURE.md`  
- Modelo de datos: `Documentación/DATA_MODEL.md`  

---

## 📌 Estado del proyecto

- ✔ Enfoque *documentation-first*  
- ✅ Funcional (API + simulador + runner)

---

## 👤 Autor

**Kirbyfet**  
---
---

# Automated Task Monitoring System

Portfolio project by **Kirbyfet**.

A lightweight backend system that demonstrates how operational tasks can be ingested from an external system, monitored automatically, escalated when overdue, and reported through a REST API.

---

## 🎯 Project purpose

This project simulates a real-world internal backend service used to:
- Track operational tasks
- Integrate with external systems via API
- Automatically detect overdue work
- Escalate priority based on business rules
- Generate reports and logs

The focus is on **backend architecture, integration patterns, and automation**, not on UI.

---

## 🧩 System components

1. **REST API**
   - CRUD operations for tasks
   - Reporting endpoints
   - SQLite persistence

2. **Integration Simulator**
   - Simulates an external system
   - Emits `CREATE` and `CLOSE` task events via API

3. **Automation Runner**
   - Periodically monitors tasks
   - Marks tasks as `OVERDUE`
   - Escalates priority
   - Writes automation logs

---

## 🏗️ Architecture & design

- Architecture: `Documentación/ARCHITECTURE.md`
- Data model: `Documentación/DATA_MODEL.md`

---

## 📌 Project status

✔ Documentation-first  
✅ Functional (API + simulator + runner)

---

## 👤 Author

**Kirbyfet**  

