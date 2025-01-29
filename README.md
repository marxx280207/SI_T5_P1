# SI_T5_P1
## Keylogger

## keylogger.py
Un keylogger básico que registra las teclas pulsadas por el usuario y las guarda en un archivo `keylog.txt`.

## Cómo ejecutar:
1. Ejecuta el script con `python keylogger.py`.
2. Escribe en cualquier aplicación y se registrara automaticamente.

## Áreas de mejora:
- Eficiencia en la escritura del archivo: Abrir y cerrar el archivo constantemente puede ser ineficiente, especialmente con muchas teclas. Se podría optimizar este proceso.
- Filtrar teclas no relevantes: El código actual registra todas las teclas, incluidas las de control (como shift, ctrl, etc.), lo cual no siempre es necesario. Podrías filtrar las teclas que no quieras registrar..
