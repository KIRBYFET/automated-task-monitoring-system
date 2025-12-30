
# Automated Task Monitoring System

Backend en Python para el monitoreo de tareas, desarrollado con **FastAPI** y **SQLite**, que integra un **simulador de eventos** y un **runner automático** para la gestión de tareas vencidas.

## Estado del proyecto
✅ Funcional (API + simulador + runner)

La API REST, el simulador de eventos y el runner de automatización se encuentran completamente operativos y pueden ejecutarse localmente.

---

## 🧠 Descripción general
Este proyecto implementa un sistema backend que permite:
- Gestionar tareas mediante una API REST
- Simular eventos provenientes de sistemas externos
- Automatizar la detección de tareas vencidas
- Generar logs y reportes de estado

Está orientado a **demostrar arquitectura backend**, automatización y buenas prácticas en Python, con fines educativos y de portafolio.

---

## 🧩 Componentes del sistema

### 🔹 API (FastAPI)
- CRUD de tareas
- Persistencia en SQLite
- Documentación interactiva con Swagger UI

### 🔹 Simulador de integraciones
- Simula un sistema externo que:
  - crea tareas (`CREATE`)
  - cierra tareas (`CLOSE`)
- Se comunica con la API vía HTTP

### 🔹 Runner de automatización
- Ejecuta ciclos periódicos
- Detecta tareas vencidas
- Marca tareas como `OVERDUE`
- Registra eventos en archivos de log
- Escala prioridades cuando corresponde

---

## 📁 Estructura del proyecto
automated-task-monitoring-system/
├── app/
├── automation/
├── integrations/
├── scripts/
├── Documentación/
├── README.md
├── requirements.txt
├── LICENSE


---

## ⚙️ Requisitos

- Python **3.10 o superior**
- Git
- Sistema operativo **Windows** (incluye scripts `.ps1`)

---

## 🚀 Instalación
## 1️⃣ Clonar el repositorio

 git clone https://github.com/KIRBYFET/automated-task-monitoring-system.git
 cd automated-task-monitoring-system
---
## 2️⃣ Crear entorno virtual

python -m venv .venv
.\.venv\Scripts\Activate.ps1
---
## 3️⃣ Instalar dependencias
pip install -r requirements.txt
---
## ▶️ Ejecución del sistema

## Opción recomendada (automática) - Levanta API + simulador + runner en ventanas separadas:

### powershell -ExecutionPolicy Bypass -File scripts\run_all.ps1

---
## ▶️Opción manual (avanzada)
## Levantar la API:

uvicorn app.main:
app --reload


## Ejecutar simulador:


ython -m integrations.ingest_simulator

## Ejecutar runner:



python -m automation.runner

---
## 🌐 Uso de la API
Documentación interactiva

Una vez levantada la API:
http://127.0.0.1:8000/docs

Desde Swagger UI puedes:

-Crear tareas

-Listar tareas

-Consultar tareas por ID

-Cerrar tareas

-Consultar reportes de tareas vencidas

---
## 🔄 Estados de una tarea

-PENDING → tarea activa

-OVERDUE → tarea vencida detectada por el runner

-DONE → tarea cerrada

Campo overdue_at

-Se completa solo cuando una tarea pasa a OVERDUE

-Permanece null si la tarea nunca estuvo vencida

---
### 🗄️ Persistencia y logs
Base de datos

-Archivo: tasks.db

-Se crea automáticamente al ejecutar la API

Logs

-Ruta: automation/logs/

-Generados automáticamente por el runner

---
## ♻️ Reset del entorno (modo desarrollo)
## Para borrar la base de datos y los logs y comenzar desde cero:

python scripts\reset_dev.py --force

Este comando no elimina el código ni el entorno virtual.

---
## 🧪 Flujo de demostración recomendado

-Ejecutar run_all.ps1

-Abrir Swagger UI (/docs)

-Observar creación automática de tareas

-Esperar a que algunas pasen a estado OVERDUE

-Consultar reportes y estados

-Cerrar tareas manualmente desde Swagger


---
## 📝 Notas finales

Este proyecto fue desarrollado con fines educativos y de portafolio, demostrando:

-diseño de backend

-automatización de procesos

-integración simulada

-uso correcto de FastAPI y SQLite
