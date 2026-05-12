# API Status - Trabajo Práctico

El proyecto implementa distintos endpoints HTTP para simular respuestas de estado, manejo de errores, guardado de datos en memoria y sistema de logs.

---

# Requisitos

Antes de ejecutar el proyecto es necesario tener instalado:
- Node.js + npm
- Python 3 + pip

Extensión utilizada para pruebas:

- Thunder Client

---

# Versión Node.js

## Instalación

Entrar a la carpeta del proyecto:

```bash
cd api-status
```

Instalar dependencias:

```bash
npm install
```

---

## Ejecutar proyecto

```bash
npm start
```

El servidor va a iniciar en:

```text
http://localhost:3000
```

---

# Versión Python

## Instalación

Entrar a la carpeta del proyecto:

```bash
cd api-status-python
```

---

## Crear entorno virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Instalar dependencias

```bash
pip install flask
```

---

## Ejecutar proyecto

### Windows

```bash
python app.py
```

### Linux/Mac

```bash
python3 app.py
```

El servidor iniciará en:

```text
http://localhost:5000
```

---

# Endpoints disponibles

## GET /status/200

Devuelve:

```json
{
  "message": "hola mundo"
}
```

---

## GET /status/500

Devuelve:

```json
{
  "message": "internal server error"
}
```

---

## GET /status/429

Devuelve:

```json
{
  "message": "too many requests"
}
```

---

## POST /status/save

Recibe un JSON y lo guarda en una base de datos simulada.

Ejemplo:

```json
{
  "nombre": "Fabrizio",
  "edad": 20
}
```

El endpoint tiene un 50% de probabilidad de devolver un error 500 simulando un fallo de base de datos.

---

## GET /status/save

Devuelve todos los registros guardados.

---

# Logs

## Node.js

La versión Node.js utiliza Winston para registrar:

- Fecha
- Nivel del log
- Mensaje

Ejemplo:

```text
[2026-05-05 15:30:00] INFO: Servidor ejecutándose en http://localhost:3000
```

---

## Python

La versión Python utiliza logging para registrar:

- Fecha
- Nivel del log
- Mensaje

Ejemplo:

```text
[2026-05-07 17:06:05] INFO: Servidor ejecutándose en http://localhost:5000
```

---

# Testing

Los endpoints fueron probados utilizando:

- Navegador web
- Thunder Client

---

# Funcionalidades implementadas
- API REST
- Endpoints GET y POST
- Base de datos simulada en memoria
- Manejo de errores
- Simulación de error 500
- Logging en consola
- Manejo de excepciones