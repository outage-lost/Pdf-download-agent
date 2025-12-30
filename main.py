import time
import logging
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

# =========================
# CONFIGURACIÓN
# =========================
BASE_DIR = Path(__file__).resolve().parent
DOWNLOAD_DIR = BASE_DIR / "downloads"
LOG_DIR = BASE_DIR / "logs"

DOWNLOAD_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================
# DRIVER
# =========================
def create_driver():
    options = Options()

    prefs = {
        "download.default_directory": str(DOWNLOAD_DIR),
        "download.prompt_for_download": False,
        "plugins.always_open_pdf_externally": True
    }

    options.add_experimental_option("prefs", prefs)
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

# =========================
# DETECTOR PDF
# =========================
def is_pdf_url(url):
    if not url:
        return False

    if not isinstance(url, str):
        return False

    url = url.lower()

    if not url.startswith("http"):
        return False

    return ".pdf" in url

# =========================
# MAIN
# =========================
def main():
    try:
        driver = create_driver()
    except WebDriverException as e:
        print("❌ Error iniciando el navegador")
        logging.error(e)
        return

    print("🌐 Navegador abierto")
    print("👉 Inicia sesión y navega normalmente")
    print("📄 Los PDFs se descargarán automáticamente")
    print("⏹️ Cierra el navegador para terminar")

    logging.info("Programa iniciado")

    main_window = driver.current_window_handle
    known_tabs = set(driver.window_handles)

    try:
        while True:
            time.sleep(1)

            try:
                current_tabs = set(driver.window_handles)
            except WebDriverException:
                break

            new_tabs = current_tabs - known_tabs

            for tab in new_tabs:
                try:
                    driver.switch_to.window(tab)
                    time.sleep(1)

                    url = driver.current_url

                    if not url or url == "about:blank":
                        continue

                    logging.info(f"Pestaña detectada: {url}")

                    if is_pdf_url(url):
                        print("📥 PDF detectado, descargando...")
                        logging.info(f"PDF detectado: {url}")

                        time.sleep(4)  # tiempo para descarga
                        driver.close()
                        driver.switch_to.window(main_window)

                except WebDriverException as e:
                    logging.error(e)
                    continue

            known_tabs = current_tabs

    except KeyboardInterrupt:
        logging.info("Programa detenido por el usuario")

    finally:
        try:
            driver.quit()
        except Exception:
            pass

        print("👋 Programa finalizado")
        logging.info("Programa finalizado")

if __name__ == "__main__":
    main()
