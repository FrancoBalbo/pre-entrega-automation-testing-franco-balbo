# Pre-entrega - QA Automation Testing

Proyecto de automatizacion de pruebas desarrollado con Python, Selenium WebDriver y Pytest sobre el sitio SauceDemo.

## Sitio utilizado

SauceDemo

https://www.saucedemo.com/

## Tecnologias utilizadas

- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Google Antigravity
- Google Chrome
- VS Code

## Estructura del proyecto

pre-entrega-automation-testing-franco-balbo/

    tests/
        __init__.py
        conftest.py
        test_saucedemo.py

    utils/
        __init__.py
        helpers.py

    reports/
        report.html

    .gitignore
    README.md
    requirements.txt

## Casos automatizados

### TC01 - Login exitoso

Se valida el inicio de sesion utilizando credenciales validas.

Validaciones:

- Redireccion a `/inventory.html`.
- Titulo del sitio `Swag Labs`.
- Visualizacion de la seccion `Products`.

### TC02 - Verificacion del catalogo

Se valida la correcta visualizacion del catalogo de productos.

Validaciones:

- Titulo `Products`.
- Existencia de productos.
- Visualizacion del menu.
- Visualizacion del selector de ordenamiento.
- Obtencion del nombre y precio del primer producto.

### TC03 - Agregar producto al carrito

Se agrega un producto al carrito y se valida el resultado.

Validaciones:

- Existencia de productos en el catalogo.
- Contador del carrito igual a `1`.
- Navegacion a `/cart.html`.
- Existencia de un producto en el carrito.
- El producto del carrito coincide con el producto seleccionado.

## Instalacion

Crear un entorno virtual:

    python -m venv .venv

Activar el entorno virtual en Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

Si PowerShell bloquea la ejecucion del script, ejecutar:

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Luego volver a activar:

    .\.venv\Scripts\Activate.ps1

Instalar las dependencias:

    python -m pip install -r requirements.txt

## Ejecutar los tests

Desde la raiz del proyecto:

    python -m pytest tests/test_saucedemo.py -v -s

## Generar reporte HTML

Ejecutar:

    python -m pytest -p pytest_html tests/test_saucedemo.py -v --html=reports/report.html --self-contained-html

El reporte generado estara disponible en:

    reports/report.html

## Evidencias de errores

Si un test falla durante su ejecucion, se genera automaticamente una captura de pantalla dentro de:

    reports/screenshots/

## Caracteristicas implementadas

- Selenium WebDriver.
- Localizadores mediante `By`.
- Esperas explicitas con `WebDriverWait`.
- Expected Conditions.
- Assertions.
- Fixtures de Pytest.
- Setup y teardown del navegador.
- Funciones auxiliares reutilizables.
- Tests independientes.
- Screenshots automaticos ante fallos.
- Reporte HTML de ejecucion.