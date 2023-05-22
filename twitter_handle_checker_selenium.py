from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Sauce Labs configuration
sauce_username = os.environ.get("SAUCE_USERNAME")
sauce_access_key = os.environ.get("SAUCE_ACCESS_KEY")

options = Options()
options.set_capability('browserName', 'chrome')
options.set_capability('platform', 'Windows 10')
options.set_capability('version', 'latest')

driver = webdriver.Remote(
    "https://" + sauce_username + ":" + sauce_access_key + "@ondemand.saucelabs.com:443/wd/hub",
    options=options,
)

target_handle = "hemanth"

try:
    driver.get("https://twitter.com/{}".format(target_handle))

    try:
        element = driver.find_element_by_xpath('//span[text()="This account '+ "doesn’t" +' exist"]')
        if element:
            print("Handle is available! :)")
        else:
            print("Handle not available :(")
    except:
        print("Handle not available :(")
finally:
    driver.quit()
