# Cliente y Servidor TCP en Python

Este proyecto contiene una implementación sencilla de un servidor y cliente TCP usando Python.

## Posicionarse en la carpeta del proyecto

Antes de ejecutar los scripts, abre una terminal y navega a la carpeta del proyecto donde están los archivos:

```bash
cd ruta/a/Cliente_Servidor_TCP
```

(En Windows podrías usar: `cd C:\Users\TuNombre\Descargas\Cliente_Servidor_TCP`)

---

## Ejecución

### Servidor

1. Abre una terminal.
2. Ejecuta el servidor con:

```bash
python servidor.py
```

### Cliente

1. Abre otra terminal (nueva ventana).
2. Ejecuta el cliente con:

```bash
python cliente.py
```

---

## Pruebas Manuales

### 1. Mensaje normal
- Desde el cliente, escribe por ejemplo: `hola servidor`
- El servidor responderá: `HOLA SERVIDOR`

### 2. Desconexión
- Escribe `DESCONEXION` desde el cliente.
- Verifica que:
  - El cliente finaliza.
  - El servidor vuelve a quedar disponible para un nuevo cliente.

---
