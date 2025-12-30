# Sistema Automatizado de Monitoreo de Tareas

Proyecto de portafolio por **Kirbyfet**.

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

- Arquitectura: `docs/ARCHITECTURE.md`  
- Modelo de datos: `docs/DATA_MODEL.md`  
- Runbook: `docs/RUNBOOK.md`  
- Decisiones técnicas: `docs/DECISIONS.md`  

---

## 📌 Estado del proyecto

- ✔ Enfoque *documentation-first*  
- ⏳ Implementación en progreso  

---

## 👤 Autor

**Kirbyfet**  
Backend / Automatización / Diseño de Sistemas
