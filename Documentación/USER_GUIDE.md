# User Guide — Automated Task Monitoring System

Esta guía describe cómo **ejecutar, usar y comprender** el sistema *Automated Task Monitoring System* desde el punto de vista del usuario y del evaluador técnico.

Está pensada para:
- Probar el sistema localmente
- Entender el flujo completo de tareas
- Observar el comportamiento del simulador y el runner
- Evaluar el sistema sin necesidad de leer el código fuente

---

## Objetivo del sistema

El sistema permite:

- Gestionar tareas mediante una API REST
- Simular eventos provenientes de sistemas externos
- Detectar automáticamente tareas vencidas
- Registrar eventos y cambios de estado
- Completar el ciclo de vida de una tarea de forma controlada

---

## ⚙️ Requisitos previos

Antes de comenzar, asegúrate de tener:

- Python **3.10 o superior**
- Git
- Sistema operativo **Windows**
- Entorno virtual creado y dependencias instaladas

---

## 🚀Instalación & Puesta en marcha

## Instalar dependencias 

El archivo requirements.txt contiene la lista de dependencias necesarias para ejecutar el proyecto. 

Su uso principal es garantizar un entorno reproducible, permitiendo instalar todas las librerías requeridas con un solo comando:

```
pip install -r requirements.txt
```

Incluye dependencias como: 

- FastAPI (API REST) 
- Uvicorn (servidor ASGI) 
- Librerías estándar para manejo de fechas, HTTP y automatización 

Este archivo es fundamental para levantar correctamente la API, el simulador y el runner.

---

## Puesta en marcha

### Opción recomendada (automática)

El proyecto incluye un script que levanta todos los componentes automáticamente:

```
powershell -ExecutionPolicy Bypass -File scripts/run_all.ps1
```

Este script abre tres ventanas de terminal y ejecuta:

- La API (FastAPI)

- El simulador de eventos

- El runner de automatización

### Opción manual (avanzada)
Ejecuta cada componente en una terminal distinta.

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
---

## 🌐 Uso de la API
Una vez levantada la API, accede a la documentación interactiva:

```
http://127.0.0.1:8000/docs
```

Desde Swagger UI puedes realizar las siguientes acciones:

- Crear tareas

- Listar tareas

- Consultar tareas por ID

- Cerrar tareas

- Consultar reportes de tareas vencidas



---

## 🧪 Flujo de uso recomendado
Este flujo permite observar el comportamiento completo del sistema.

## 1️⃣ Creación de tareas
- El simulador crea tareas automáticamente

- Las tareas comienzan en estado PENDING

- Se asigna una fecha de vencimiento (due_at)

También es posible crear tareas manualmente desde Swagger UI.

## 2️⃣ Detección de tareas vencidas
El runner se ejecuta periódicamente

- Detecta tareas cuyo vencimiento ha sido superado

- Cambia su estado a OVERDUE

- Registra el momento exacto en el campo overdue_at

## 3️⃣ Consulta de reportes
Desde la API es posible:

- Listar todas las tareas

- Filtrar tareas vencidas

- Consultar tareas por ID

- Revisar cambios de estado

## 4️⃣ Cierre de tareas
- Las tareas pueden cerrarse manualmente

- Al cerrarse, pasan a estado DONE

- Se completa el ciclo de vida de la tarea

## 🔄 Estados de una tarea
Las tareas manejan los siguientes estados:

- PENDING → tarea activa, dentro del plazo

- OVERDUE → tarea vencida detectada automáticamente

- DONE → tarea cerrada manualmente

Campo overdue_at
- Se completa únicamente cuando una tarea pasa a estado OVERDUE

- Permanece null si la tarea nunca estuvo vencida

---

## 🗄️ Persistencia y logs
📦 Base de datos
- Archivo: tasks.db

- Se crea automáticamente al ejecutar la API

- Contiene todas las tareas y sus estados

📄 Logs del sistema
- Ubicación: automation/logs/

- Generados por el runner

Registran:

- detección de tareas vencidas

- cambios de estado

- ejecución de ciclos automáticos

---

## ♻️ Reinicio del entorno (modo desarrollo)
Para reiniciar el sistema desde cero:

```
python scripts/reset_dev.py --force
```

Este comando:

- Elimina la base de datos

- Borra los logs generados

- No elimina el código ni el entorno virtual
