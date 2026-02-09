import pytest
import time
from hmi_automation.utils.driver import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from hmi_automation.can_comm.can_sender import send_signal


@pytest.mark.order(1)
def test_vehicle_shutdown_with_side_stand_popup():
    driver = get_driver()
    wait = WebDriverWait(driver, 40)

    # ---- Click Home ----
    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH,
        '//android.view.View[@resource-id="benchmark_root"]/android.view.View[3]/android.view.View[1]/android.view.View'
    ))).click()

    # ---- Click Shutdown ----
    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="shutdown"]'
    ))).click()

    # ---- Verify Side Stand Popup ----
    time.sleep(2)
    popup_found = driver.find_elements(
        AppiumBy.XPATH,
        '//*[contains(@text,"Side Stand") or contains(@content-desc,"Side Stand")]'
    )

    assert len(popup_found) > 0, "❌ Side stand popup not displayed"
    print("✅ Side stand popup displayed successfully")

    # ---- Send side stand open signal ----
    send_signal("BCM_HMI_StatusCommands_23", {"BCM_Sw_Standsensor_status": 1})
    time.sleep(1)
