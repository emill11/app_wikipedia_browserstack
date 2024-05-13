import os

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

load_dotenv()
user_name = os.getenv('LOGIN')
access_key = os.getenv('PASSWORD')
url = os.getenv('URL')
time_out = float(os.getenv('TIMEOUT'))

device_name = os.getenv('DEVICE_NAME')
platform_version = os.getenv('PLATFORM_VERSION')
remote_app = os.getenv('REMOTE_APP')

options = UiAutomator2Options().load_capabilities({

    "platformVersion": platform_version,
    "deviceName": device_name,

    "app": remote_app,

    'bstack:options': {
        "projectName": "First Python project",
        "buildName": "browserstack-build-1",
        "sessionName": "BStack first_test",

        "userName": user_name,
        "accessKey": access_key
    }
})
