from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without GUI
chrome_options.add_argument("--disable-gpu")  # Disable GPU usage
chrome_options.add_argument("--no-sandbox")  # Bypass sandbox restrictions
chrome_options.add_argument("--disable-dev-shm-usage")  # Use /tmp instead of /dev/shm
chrome_options.add_argument("--remote-debugging-port=9222")  # Enable debugging

# Explicitly set the Chrome binary path
chrome_options.binary_location = "/usr/bin/google-chrome"
service = Service("/usr/local/bin/chromedriver")
# Initialize ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Test
driver.get("https://www.google.com")
print(driver.title+"test")
driver.quit()
