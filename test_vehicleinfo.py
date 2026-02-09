import pytest
from hmi_automation.utils.driver import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy


@pytest.mark.order(1)
def test_vehicle_info_cancel():
    driver = get_driver()
    wait = WebDriverWait(driver, 40)

    # ---- Click Home ----
    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH,
        '//android.view.View[@resource-id="benchmark_root"]/android.view.View[3]/android.view.View[1]/android.view.View'
    ))).click()

    # ---- Click Vehicle Number ----
    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Right Icon"]'
    ))).click()

    # ---- Click Cancel Button ----
    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Cancel button"]'
    ))).click()

    print("✅ Vehicle info popup closed successfully")
