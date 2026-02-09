import pytest
import time

from hmi_automation.utils.driver import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from hmi_automation.can_comm.can_sender import send_signal


@pytest.mark.order(1)
def test_verify_home_screen_and_open_navigation():
    driver = get_driver()
    wait = WebDriverWait(driver, 240)

    try:
        # ---------------- STEP 1: Key OFF → ON ----------------
        send_signal("BCM_HMI_StatusCommands_23", {
            "BCM_H_KeyOnoff_Command": 0,
            "BCM_Sw_KIllSwitch_Status": 1,
        })
        time.sleep(3)

        send_signal("BCM_HMI_StatusCommands_23", {
            "BCM_H_KeyOnoff_Command": 1,
            "BCM_Sw_KIllSwitch_Status": 1,
        })
        time.sleep(5)

        # ---------------- STEP 2: Wait for usable UI ----------------
        wait.until(lambda d:
            d.find_elements(AppiumBy.XPATH, '//*[contains(@text,"Press Brake")]') or
            d.find_elements(AppiumBy.XPATH, '//*[@resource-id="benchmark_root"]')
        )
        time.sleep(3)

        # ---------------- STEP 3: Left Brake + Motor ON + Ignition ----------------
        # send_signal("BCM_HMI_StatusCommands_23", {
        #     "BCM_Sw_Leftbrake_status": 1,
        #     "BCM_Sw_KIllSwitch_Status": 1,
        # })
        # time.sleep(3)

        # send_signal("MC_All_Telemetry_1", {
        #     "Motor_OnOff_status": 1,
        # })
        # time.sleep(3)

        # send_signal("BCM_HMI_StatusCommands_23", {
        #     "BCM_Sw_Ignition_Status": 1,
        # })

    finally:
        pass  # ❌ DO NOT quit driver
