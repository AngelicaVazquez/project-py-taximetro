# 🚕 TaxiTech Solutions — Sistema de Taxímetro Digital

Sistema de taxímetro 100% software desarrollado en Python para la modernización de la gestión de flotas. Permite a los conductores registrar carreras, calcular tarifas en tiempo real basándose en la cinemática del vehículo (parado o en movimiento) y mantener un registro auditable de toda la actividad operativa.

## 🚀 Funcionalidades (Versión Actual)

- **Interfaz de Consola (CLI):** Menú interactivo optimizado para una operativa rápida por parte del conductor.
- **Cálculo de Tarifas Dinámico:** Transición fluida entre estado "Parado" y "En movimiento", acumulando el importe exacto según el tiempo transcurrido en cada estado.
- **Configuración Desacoplada:** Las tarifas se definen en el archivo `config.json`, permitiendo actualizaciones de precios sin necesidad de tocar el código ni redesplegar el sistema.
- **Persistencia de Datos:** Cada carrera finalizada se guarda automáticamente en un histórico (`history.json`) para facilitar el cuadre de caja al final del turno.
- **Trazabilidad (Observabilidad):** El sistema genera un registro de eventos continuo en `taximetro.log` para facilitar el diagnóstico técnico.
- **Fiabilidad:** Lógica de negocio y cálculo numérico respaldados por pruebas unitarias automatizadas (`test_taximeter.py`).

## 📋 Requisitos

- Python 3.10 o superior.
- No requiere librerías externas (funciona íntegramente con la Standard Library de Python).

## 🛠️ Instalación y Uso

1. Clona el repositorio en tu máquina local.
2. (Opcional) Modifica las tarifas en el archivo `config.json` si necesitas valores distintos a los de por defecto.
3. Ejecuta la terminal del conductor:

```bash
python app.py