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

- 📘 **[Guía de Usuario](Documentación/USER_GUIDE.md)**  
  Describe cómo ejecutar y utilizar el sistema, incluyendo el flujo completo de demostración.

- 🏗️ **[Arquitectura del Sistema](Documentación/ARCHITECTURE.md)**  
  Explica la arquitectura general, la separación de componentes y las decisiones de diseño.

- 🗃️ **[Modelo de Datos](Documentación/DATA_MODEL.md)**  
  Detalla las entidades, estados y la estructura de datos utilizada por el sistema.

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

## 🚀 Ejecución rápida
Esta sección permite **levantar el sistema de forma inmediata** para probar su funcionamiento.  
La explicación detallada del flujo, comportamiento y uso del sistema se encuentra documentada en la **[Guía de Usuario](Documentación/USER_GUIDE.md)**.

---

## Instalar dependencias:

```
pip install -r requirements.txt
```

## Ejecución:
```
powershell -ExecutionPolicy Bypass -File scripts/run_all.ps1
```

Luego accede a:

API Docs: http://127.0.0.1:8000/docs

---

## 📝 Notas finales
Este proyecto fue desarrollado con fines educativos y de portafolio, demostrando:

- Diseño de backend

- Automatización de procesos

- Integración simulada

- Uso correcto de FastAPI y SQLite
