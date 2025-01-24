# SI_T5_P1
## Keylogger y Detector

Este repositorio contiene dos scripts de Python:

## keylogger.py
Un keylogger básico que registra las teclas pulsadas por el usuario y las guarda en un archivo `keylog.txt`. El programa se ejecuta hasta que se presiona la tecla `esc`.

### Cómo ejecutar:
1. Ejecuta el script con `python keylogger.py`.
2. Escribe en cualquier aplicación y presiona `esc` para detenerlo.

## keylogger_detector.py
Un script que detecta y elimina un keylogger básico como el de `keylogger.py`. Este script detiene el proceso que ejecuta el keylogger y elimina el archivo `keylog.txt`.

### Cómo ejecutar:
1. Ejecuta el script con `python keylogger_detector.py`.
2. Verifica que el archivo `keylog.txt` se haya eliminado correctamente.

## Áreas de mejora:
- Implementar un mecanismo de detección más sofisticado para otros keyloggers.
- Añadir protección para evitar la eliminación de archivos importantes.
