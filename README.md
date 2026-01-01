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

## 🎯 Alcance y no-alcance del proyecto

Este proyecto fue diseñado con un **alcance claramente delimitado**, orientado a demostrar conceptos de **arquitectura backend, automatización e integración simulada**, y **no** como un sistema listo para producción.

### ✅ Alcance del proyecto


## El sistema cubre los siguientes aspectos:

- Implementación de una API REST para gestión de tareas
- Simulación de eventos provenientes de sistemas externos
- Automatización de detección de tareas vencidas mediante un runner
- Persistencia de datos en una base SQLite
- Registro de eventos en archivos de log
- Exposición de reportes mediante endpoints REST
- Ejecución local y demostrable de extremo a extremo

### 🚫 No-alcance del proyecto


## De forma intencional, este proyecto **no incluye**:

- ❌ Un sistema distribuido real (microservicios, colas, mensajería)
- ❌ Autenticación o autorización de usuarios
- ❌ Gestión de roles o permisos
- ❌ Manejo de alta concurrencia o escalabilidad horizontal
- ❌ Integraciones reales con sistemas externos
- ❌ Configuración orientada a producción
- ❌ Persistencia en bases de datos empresariales (PostgreSQL, MySQL, etc.)
- ❌ Despliegue en entornos cloud o contenedores

El **simulador de integraciones** reemplaza de manera controlada a sistemas externos reales, permitiendo reproducir flujos de negocio sin dependencias externas ni complejidad adicional.

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
│   └── ARCHITECTURE.md
│   └── DATA_MODEL.md
├── README.md
├── requirements.txt
├── LICENSE
```
## 📚 Documentación del proyecto

Este repositorio incluye documentación adicional que explica en detalle el uso, la arquitectura y el modelo de datos del sistema. Estos archivos están pensados tanto para usuarios como para revisores técnicos.

---
## 🏗️ Arquitectura del sistema (ARCHITECTURE.md)

El archivo Documentación/ARCHITECTURE.md describe la arquitectura general del sistema.

Detalla:

- Separación por capas (API, automatización, integraciones)

- Flujo de comunicación entre componentes

- Rol del simulador como sistema externo

- Rol del runner como proceso automático

- Decisiones de diseño y responsabilidades de cada módulo

Este documento está orientado a revisores técnicos y entrevistas, explicando el por qué de la estructura del proyecto.

---

## 🗃️ Modelo de Datos (DATA_MODEL.md)

El archivo Documentación/DATA_MODEL.md documenta el modelo de datos utilizado por el sistema. 

Incluye:

- Entidad principal Task

- Campos y tipos de datos

- Estados posibles (PENDING, OVERDUE, DONE)

- Campo overdue_at y su comportamiento

- Relación entre fechas, estados y automatización

Este documento permite comprender cómo se persisten las tareas y cómo el runner interactúa con los datos. 

---

## 📘 Guía de Usuario (USER_GUIDE.md)

El archivo Documentación/USER_GUIDE.md contiene una guía paso a paso orientada al uso del sistema.

Incluye:

- Ejecución del proyecto

- Flujo completo de demostración

- Uso de Swagger UI

- Estados de las tareas

- Comportamiento del simulador y del runner

- Reinicio del entorno de desarrollo

Este documento está pensado para usuarios funcionales, evaluadores o personas que desean probar el sistema sin profundizar en el código.

---

## ⚙️ Requisitos

- Python 3.10 o superior

- Git

- Sistema operativo Windows (incluye scripts .ps1)

---

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
El archivo `requirements.txt` contiene la lista de dependencias necesarias para ejecutar el proyecto.

Su uso principal es garantizar un entorno reproducible, permitiendo instalar todas las librerías requeridas con un solo comando:

```
pip install -r requirements.txt
```

Incluye dependencias como:

- FastAPI (API REST)

- Uvicorn (servidor ASGI)

- Librerías estándar para manejo de fechas, HTTP y automatización

Este archivo es fundamental para levantar correctamente la API, el simulador y el runner.


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

- Archivo: tasks.db

- Se crea automáticamente al ejecutar la API


📄 Logs

- Ruta: automation/logs/

- Generados automáticamente por el runner

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
