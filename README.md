# Automated Task Monitoring System

Backend en Python para el monitoreo de tareas, desarrollado con **FastAPI** y **SQLite**, que integra un **simulador de eventos** y un **runner automático** para la gestión de tareas vencidas.

---

## 📌 Estado del proyecto

✅ Funcional (API + simulador + runner)

La API REST, el simulador de eventos y el runner de automatización se encuentran completamente operativos y pueden ejecutarse localmente.

---

## 🧠 Descripción general

Este proyecto implementa un sistema backend que permite:

- Gestionar tareas mediante una API REST
- Simular eventos provenientes de sistemas externos
- Automatizar la detección de tareas vencidas
- Escalar prioridades automáticamente
- Registrar eventos en logs
- Consultar reportes de tareas vencidas

El objetivo principal del proyecto es **demostrar arquitectura backend, automatización e integración simulada**, con fines educativos y de portafolio profesional.

---

## 🧩 Componentes del sistema

### 🔹 API (FastAPI)

- CRUD completo de tareas
- Persistencia en **SQLite**
- Documentación interactiva mediante **Swagger UI**

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
- Escala la prioridad cuando corresponde

---

## 📁 Estructura del proyecto

```
automated-task-monitoring-system/
├── app/
├── automation/
├── integrations/
├── scripts/
├── Documentación/
│   └── USER_GUIDE.md
├── README.md
├── requirements.txt
├── LICENSE
```

## ⚙️ Requisitos

- Python 3.10 o superior

- Git

- Sistema operativo Windows (incluye scripts .ps1)

## 🚀 Instalación
## 1️⃣ Clonar el repositorio
Clona el repositorio y accede al directorio del proyecto:

```
git clone https://github.com/KIRBYFET/automated-task-monitoring-system.git
cd automated-task-monitoring-system
```

## 2️⃣ Crear y activar entorno virtual (PowerShell)
Crea un entorno virtual para aislar las dependencias del proyecto y actívalo:


```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
## 3️⃣ Instalar dependencias
Instala todas las dependencias necesarias utilizando el archivo requirements.txt:


```
pip install -r requirements.txt
```
## ▶️ Ejecución del sistema
El sistema puede ejecutarse de forma automática o manual, dependiendo del nivel de control deseado.

✅ Opción recomendada (automática)
Levanta la API, el simulador y el runner en ventanas separadas automáticamente:


```
powershell -ExecutionPolicy Bypass -File scripts\run_all.ps1
```
## 🧪 Opción manual (avanzada)
Ejecuta los componentes en tres terminales separadas.

Terminal 1 — API

```
uvicorn app.main:app --reload
```


Terminal 2 — Simulador

```
python -m integrations.ingest_simulator
```

Terminal 3 — Runner
```
python -m automation.runner
```

## 🌐 Uso de la API

Una vez levantada la API, accede a la documentación interactiva:
http://127.0.0.1:8000/docs


Desde Swagger UI puedes realizar las siguientes acciones:

- Crear tareas

- Listar tareas

- Consultar tareas por ID

- Cerrar tareas

- Consultar reportes de tareas vencidas

---
## 🔄 Estados de una tarea
Las tareas pueden encontrarse en los siguientes estados:

- PENDING → tarea activa

- OVERDUE → tarea vencida detectada por el runner

- DONE → tarea cerrada

Campo overdue_at
- Se completa solo cuando una tarea pasa a estado OVERDUE

- Permanece null si la tarea nunca estuvo vencida

---

## 🗄️ Persistencia y logs

📦 Base de datos

Archivo: tasks.db

Se crea automáticamente al ejecutar la API


📄 Logs

Ruta: automation/logs/

Generados automáticamente por el runner

---

## ♻️ Reset del entorno (modo desarrollo)
Permite reiniciar el entorno de pruebas eliminando la base de datos y los logs:


```
python scripts/reset_dev.py --force
```

Este comando no elimina el código ni el entorno virtual.

---

## 🧪 Flujo de demostración recomendado
Ejecutar scripts/run_all.ps1

- Abrir Swagger UI (/docs)

- Observar creación automática de tareas

- Esperar detección de tareas vencidas

- Consultar reportes

- Cerrar tareas manualmente

---

## 📝 Notas finales
Este proyecto fue desarrollado con fines educativos y de portafolio, demostrando:

- Diseño de backend

- Automatización de procesos

- Integración simulada

- Uso correcto de FastAPI y SQLite
