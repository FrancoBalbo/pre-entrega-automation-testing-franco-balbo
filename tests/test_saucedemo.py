from _pytest import warning_types
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import login


def test_login_exitoso(driver):

    login(driver)

    wait = WebDriverWait(driver, 10)

    products_title = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert "/inventory.html" in driver.current_url
    assert "Swag Labs" in driver.title
    assert products_title.text == "Products"

def test_catalogo(driver):

    login(driver)

    wait = WebDriverWait(driver, 10)

    products_title = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert products_title.text == "Products"

    products = driver.find_elements(
        By.CLASS_NAME, "inventory_item"
    )

    assert len(products) > 0

    menu_button = driver.find_element(
        By.ID, "react-burger-menu-btn"
    )

    product_filter = driver.find_element(
        By.CLASS_NAME, "product_sort_container"
    )

    assert menu_button.is_displayed()
    assert product_filter.is_displayed()

    first_product = products[0]

    product_name = first_product.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    product_price = first_product.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    print(f"Primer producto: {product_name}")
    print(f"Precio: {product_price}")

    assert product_name != ""
    assert product_price != ""

def test_agregar_producto_al_carrito(driver):

    login(driver)

    wait = WebDriverWait(driver, 10)

    # Esperar que cargue el catálogo
    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    # Obtener los productos
    products = driver.find_elements(
        By.CLASS_NAME, "inventory_item"
    )

    assert len(products) > 0

    # Obtener el primer producto
    first_product = products[0]

    product_name = first_product.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    # Esperar que el botón de agregar esté disponible
    add_to_cart_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )

    # Agregar producto al carrito
    add_to_cart_button.click()

    # Esperar que el contador indique 1
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "shopping_cart_badge"),
            "1"
        )
    )

    cart_badge = driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge"
    )

    assert cart_badge.text == "1"

    # Ir al carrito
    cart_link = wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    )

    cart_link.click()

    # Esperar cambio de URL
    wait.until(
        EC.url_contains("/cart.html")
    )

    # Esperar que aparezcan productos en el carrito
    cart_items = wait.until(
        EC.visibility_of_all_elements_located(
            (By.CLASS_NAME, "cart_item")
        )
    )

    assert len(cart_items) == 1

    # Obtener nombre del producto del carrito
    cart_product_name = cart_items[0].find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    # Comprobar que sea el mismo producto
    assert cart_product_name == product_name