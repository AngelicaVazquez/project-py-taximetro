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
```

## 🎮 Guía de Operación

El sistema se controla mediante comandos de una sola letra para agilizar su uso:

- **[ I ] Iniciar carrera:** Abre un nuevo servicio y comienza a tarifar (arranca por defecto en estado PARADO).
- **[ M ] En movimiento:** Cambia al estado de marcha, aplicando la tarifa por segundo correspondiente.
- **[ P ] Parado:** Cambia al estado de detención o baja velocidad (semáforos, atascos).
- **[ F ] Finalizar carrera:** Cierra el servicio actual, muestra el importe total en euros a cobrar al pasajero y registra los datos en el histórico.
- **[ V ] Ver histórico:** Imprime por pantalla un resumen de todas las carreras finalizadas.
- **[ S ] Salir:** Cierra la aplicación de forma segura.

## 📂 Estructura del Proyecto

- `app.py`: Punto de entrada principal. Maneja la interfaz de línea de comandos (CLI) y la interacción con el usuario.
- `taximeter.py`: Núcleo del dominio. Contiene la clase `Taximeter`, la gestión de estados y el motor de cálculo de precios.
- `config.json`: Archivo de configuración externa (tarifas).
- `history.json`: Almacenamiento persistente en formato JSON con los datos de facturación.
- `test_taximeter.py`: Suite de tests unitarios para validar la precisión del taxímetro.
- `taximetro.log`: Archivo autogenerado con los registros de ejecución del sistema.

## 🚧 Roadmap Próximas Versiones

- **Fase 3:** Implementación de interfaz gráfica (GUI) táctil para tablets y sistema de autenticación de seguridad.
- **Fase 4:** Migración a base de datos relacional y exposición de servicios vía API REST.