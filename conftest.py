import sys
import os
import pytest
from datetime import datetime
from hmi_automation.utils.driver import get_driver

# -------------------------------------------------------------------
# 🔧 Ensure project root is in PYTHONPATH
# -------------------------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# -------------------------------------------------------------------
# 🚗 Driver fixture (shared across all tests)
# -------------------------------------------------------------------
@pytest.fixture(scope="session")
def driver():
    drv = get_driver()
    yield drv
    drv.quit()

# -------------------------------------------------------------------
# 📸 Helper function usable inside tests
# -------------------------------------------------------------------
def take_step_screenshot(driver, step_name):
    screenshots_dir = os.path.join(os.path.dirname(__file__), "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(screenshots_dir, f"{step_name}_{timestamp}.png")
    driver.get_screenshot_as_file(file_path)
    print(f"📸 Screenshot saved: {file_path}")

# -------------------------------------------------------------------
# 📸 Hook to know test result
# -------------------------------------------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# -------------------------------------------------------------------
# 📷 Auto screenshot on failure
# -------------------------------------------------------------------
@pytest.fixture(autouse=True)
def take_screenshot_on_failure(request, driver):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            screenshots_dir = os.path.join(os.path.dirname(__file__), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = os.path.join(screenshots_dir, f"{request.node.name}_{timestamp}.png")
            driver.get_screenshot_as_file(file_path)
            print(f"\n📸 Failure screenshot saved: {file_path}")
        except Exception as e:
            print(f"\n⚠️ Screenshot skipped: {e}")
