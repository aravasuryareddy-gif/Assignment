import pytest
import time

from hmi_automation.utils.driver import get_driver
from hmi_automation.utils.screenshot import take_step_screenshot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import WebDriverException


@pytest.mark.order(2)
def test_open_navigation_and_search():
    driver = get_driver()
    wait = WebDriverWait(driver, 180)

    try:
        # ---------------- STEP 3: Tap Navigation Icon ----------------
        nav_icon = wait.until(EC.visibility_of_element_located((
            AppiumBy.XPATH,
            '//android.view.View[@resource-id="benchmark_root"]/android.view.View[3]/android.view.View[2]',
        )))

        rect = nav_icon.rect
        driver.execute_script("mobile: clickGesture", {
            "x": rect["x"] + rect["width"] // 2,
            "y": rect["y"] + rect["height"] // 2
        })
        print("✅ Navigation icon tapped")
        take_step_screenshot(driver, "01_navigation_icon")
        time.sleep(6)

        # ---------------- STEP 4: Tap Where to ----------------
        where_to = wait.until(EC.visibility_of_element_located((
            AppiumBy.XPATH,
            '//*[contains(@text,"Where to")]',
        )))

        rect = where_to.rect
        driver.execute_script("mobile: clickGesture", {
            "x": rect["x"] + rect["width"] // 2,
            "y": rect["y"] + rect["height"] // 2
        })
        print("✅ Where to? tapped")
        take_step_screenshot(driver, "02_where_to")
        time.sleep(6)

        # ---------------- STEP 5: Tap Search + Type ----------------
        search_box = wait.until(EC.visibility_of_element_located((
            AppiumBy.XPATH,
            '//android.widget.TextView[contains(@text,"Search")]',
        )))

        rect = search_box.rect
        driver.execute_script("mobile: clickGesture", {
            "x": rect["x"] + rect["width"] // 2,
            "y": rect["y"] + rect["height"] // 2
        })
        print("✅ Search box tapped")
        take_step_screenshot(driver, "03_search_box")
        time.sleep(3)

        driver.execute_script("mobile: type", {"text": "Tin Factory"})
        print("✅ Entered: Tin Factory")
        take_step_screenshot(driver, "04_text_entered")
        time.sleep(6)

        # ---------------- STEP 6: Select Tin Factory Result ----------------
        result = wait.until(EC.visibility_of_element_located((
            AppiumBy.XPATH,
            '//android.widget.TextView[contains(@text,"Tin Factory")]',
        )))

        rect = result.rect
        driver.execute_script("mobile: clickGesture", {
            "x": rect["x"] + rect["width"] // 2,
            "y": rect["y"] + rect["height"] // 2
        })
        print("✅ Tin Factory selected")
        take_step_screenshot(driver, "05_result_selected")
        time.sleep(6)

        # ---------------- STEP 7: Start Navigation ----------------
        start_nav = wait.until(EC.visibility_of_element_located((
            AppiumBy.XPATH,
            '//android.view.View[@content-desc="start_navigation"]',
        )))

        rect = start_nav.rect
        driver.execute_script("mobile: clickGesture", {
            "x": rect["x"] + rect["width"] // 2,
            "y": rect["y"] + rect["height"] // 2
        })
        print("🚀 Navigation started")
        take_step_screenshot(driver, "06_navigation_started")
        time.sleep(10)

        # ---------------- STEP 8: End Navigation ----------------
        end_btn = wait.until(EC.visibility_of_element_located((
            AppiumBy.XPATH,
            '//android.widget.Button',
        )))

        rect = end_btn.rect
        driver.execute_script("mobile: clickGesture", {
            "x": rect["x"] + rect["width"] // 2,
            "y": rect["y"] + rect["height"] // 2
        })
        print("🛑 End navigation button tapped")
        take_step_screenshot(driver, "07_end_navigation")
        print("⏳ Waiting for navigation app to close/restart...")
        time.sleep(12)

        # ---------------- STEP 9: Confirm End (SAFE MODE) ----------------
        try:
            end_confirm = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="End"]'))
            )
            rect = end_confirm.rect
            driver.execute_script("mobile: clickGesture", {
                "x": rect["x"] + rect["width"] // 2,
                "y": rect["y"] + rect["height"] // 2
            })
            print("✅ Maps closed")
            take_step_screenshot(driver, "08_end_confirm")
            time.sleep(6)
        except WebDriverException:
            print("⚠️ End confirmation skipped (app already closed)")

        # ---------------- STEP 10: Close Trip Completed ----------------
        try:
            close_trip = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="close"]'))
            )
            rect = close_trip.rect
            driver.execute_script("mobile: clickGesture", {
                "x": rect["x"] + rect["width"] // 2,
                "y": rect["y"] + rect["height"] // 2
            })
            print("✅ Trip completed popup closed")
            take_step_screenshot(driver, "09_trip_completed_closed")
        except WebDriverException:
            print("⚠️ Trip completed popup not shown")

        time.sleep(30)

    finally:
        pass
