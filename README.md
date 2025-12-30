# 📄 PDF Download Agent - Automatizador de Descarga de PDFs

Este proyecto automatiza la descarga de archivos PDF mientras navegas en Chrome. Detecta automáticamente cuando se abre una pestaña con un enlace PDF y lo descarga sin intervención manual.

---

## 🚀 **Características Principales**

- ✅ Detección automática de enlaces PDF en nuevas pestañas
- ✅ Descarga silenciosa sin prompts
- ✅ Compatible con **Windows, Linux (Ubuntu)** y **macOS**
- ✅ Manejo automático de múltiples pestañas
- ✅ Logs detallados de actividad
- ✅ Configuración de carpeta de descargas personalizada

---

## 📁 **Estructura del Proyecto**

```
pdf-download-agent/
├── main.py              # Código principal
├── requirements.txt     # Dependencias
├── downloads/          # PDFs descargados (se crea automáticamente)
├── logs/               # Archivos de registro (se crea automáticamente)
└── README.md           # Este archivo
```

---

## ⚙️ **Requisitos Previos**

### **Para Windows/macOS:**
- Python 3.8 o superior
- Google Chrome instalado

### **Para Ubuntu/Linux:**
```bash
sudo apt update
sudo apt install python3 python3-pip chromium-browser -y
```

---

## 📦 **Instalación Paso a Paso**

### **1. Clonar/Descargar el Proyecto**
```bash
git clone <tu-repositorio>
cd pdf-download-agent
```

### **2. Crear Entorno Virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### **3. Instalar Dependencias**
```bash
pip install -r requirements.txt
```

---

## ▶️ **Ejecución del Programa**

### **Ejecución Normal:**
```bash
python main.py
```

### **¿Qué ocurre al ejecutar?**
1. Se abrirá una ventana de Chrome maximizada
2. Navega normalmente, inicia sesión en tus sitios web
3. Cuando abras un enlace PDF en **nueva pestaña**, se descargará automáticamente
4. Los PDFs se guardan en la carpeta `downloads/`
5. Para detener el programa: `Ctrl + C` en la terminal

---

## 🖥️ **Uso Práctico**

1. **Ejecuta el programa:**
   ```bash
   python main.py
   ```

2. **Navega en Chrome normalmente:**
   - Inicia sesión en cualquier sitio web
   - Haz clic en enlaces normalmente

3. **Cuando encuentres un PDF:**
   - Si el PDF se abre en **misma pestaña**: se descarga normalmente
   - Si el PDF se abre en **nueva pestaña**: se detecta, descarga y cierra automáticamente

4. **Encuentra tus archivos:**
   - Todos los PDFs descargados están en `downloads/`
   - Los logs de actividad están en `logs/app.log`

---

## 🔧 **Solución de Problemas**

### **Problema: Chrome no se abre**
```bash
# Actualiza webdriver-manager
pip install --upgrade webdriver-manager
```

### **Problema: Error de permisos (Linux)**
```bash
chmod +x venv/bin/python
```

### **Problema: PDFs no se descargan**
- Verifica que el enlace termine en `.pdf`
- Revisa `logs/app.log` para errores
- Asegúrate de no tener ventanas emergentes bloqueadas

### **Reiniciar desde cero:**
```bash
# Desactivar entorno
deactivate

# Eliminar entorno y reinstalar
rm -rf venv/ downloads/ logs/
# Luego repetir pasos de instalación
```

---

## 📝 **Notas Importantes**

- ⚠️ **No cierres Chrome manualmente** - usa `Ctrl + C` en la terminal
- ⏱️ El programa espera 4 segundos por descarga (ajustable en código)
- 📊 Los logs ayudan a diagnosticar problemas
- 🔒 Usa responsablemente y respeta términos de servicio

---

## 🛠️ **Personalización (Opcional)**

### **Cambiar carpeta de descargas:**
Edita `main.py` línea 12:
```python
DOWNLOAD_DIR = BASE_DIR / "tu_carpeta_personalizada"
```

### **Cambiar tiempo de descarga:**
Edita `main.py` línea 87:
```python
time.sleep(4)  # Cambia 4 por los segundos deseados
```

---

## 📄 **Logs y Monitoreo**

Revisa la actividad del programa en:
```bash
# Ver logs en tiempo real (Linux/macOS)
tail -f logs/app.log

# Ver logs (Windows)
type logs\app.log
```

---

## 📋 **Compatibilidad Confirmada**

| Sistema | Versión | Estado |
|---------|---------|--------|
| Windows 10/11 | Python 3.8+ | ✅ Funciona |
| Ubuntu 20.04+ | Python 3.8+ | ✅ Funciona |
| macOS 12+ | Python 3.8+ | ✅ Funciona |

---

## ⚠️ **Advertencia Legal**

Este software es para **uso educativo y personal**. Asegúrate de:
- Tener permiso para descargar los archivos
- Respetar derechos de autor
- Cumplir con términos de servicio de los sitios web
- No usarlo para actividades ilegales

---

## 🤝 **Contribuir**

1. Haz fork del proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

---

## 📧 **Soporte**

Si encuentras problemas:
1. Revisa `logs/app.log`
2. Verifica que cumples requisitos
3. Abre un issue en GitHub con:
   - Sistema operativo
   - Versión de Python
   - Error completo del log

---

**¡Listo para descargar!** 🚀

Simplemente ejecuta `python main.py` y navega como siempre. Los PDFs se descargarán automáticamente.
