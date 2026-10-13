import os

import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        os.makedirs("reports/screenshots", exist_ok=True)

        test_name = request.node.name

        screenshot_path = f"reports/screenshots/{test_name}.png"

        driver.save_screenshot(screenshot_path)

        print(f"\nScreenshot guardado en: {screenshot_path}")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)