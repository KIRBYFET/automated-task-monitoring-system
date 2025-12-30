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

- Architecture: `docs/ARCHITECTURE.md`
- Data model: `docs/DATA_MODEL.md`
- Runbook: `docs/RUNBOOK.md`
- Technical decisions: `docs/DECISIONS.md`

---

## 📌 Project status

✔ Documentation-first  
⏳ Implementation in progress

---

## 👤 Author

**Kirbyfet**  
Backend / Automation / Systems Design
