# Natillera

## Desarrollo

### Abrir el designer integrado de QT

En la ruta "venv/Lib/site-packages/PySide2" hay que crear una carpeta llamada "bin" y en esta se tiene que poner una copia del archivo "uic.exe" que se encuentra en la ruta anterior.

```bash
pyside2-designer
```

Despues de generar el codigo de una ventana, cambiar la importacion de "resources_rc" por lo siguiente:

```python
import gui.resources_rc
```

### Compilar archivo de recursos de QT

Sin este archivo compilado a python el programa no va a funcionar.

```bash
cd gui
pyside2-rcc resources.qrc -o resources_rc.py
```
