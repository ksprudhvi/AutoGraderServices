from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without GUI
chrome_options.add_argument("--disable-gpu")  # Disable GPU usage
chrome_options.add_argument("--no-sandbox")  # Bypass sandbox restrictions
chrome_options.add_argument("--disable-dev-shm-usage")  # Use /tmp instead of /dev/shm
chrome_options.add_argument("--remote-debugging-port=9222")  # Enable debugging


# Use an existing Chrome profile


# Set the path to Chrome binary and ChromeDriver
chrome_options.binary_location = "/usr/bin/google-chrome"
service = Service("/usr/local/bin/chromedriver")

print("Initializing ChromeDriver service...")
driver = webdriver.Chrome(service=service, options=chrome_options)
js_script = """
window.interactionLogs = window.interactionLogs || [];

// Log Clicks
document.addEventListener('click', function(event) {
    const element = event.target;
    const interaction = {
        type: 'click',
        tagName: element.tagName,
        id: element.id || 'No ID',
        name: element.name || 'No Name',
        className: element.className || 'No Class',
        innerText: element.innerText.trim() || 'No Text',
        timestamp: new Date().toISOString()
    };
    window.interactionLogs.push(interaction);
});

// Log Input Changes
document.addEventListener('input', function(event) {
    const element = event.target;
    const interaction = {
        type: 'input',
        tagName: element.tagName,
        id: element.id || 'No ID',
        name: element.name || 'No Name',
        className: element.className || 'No Class',
        value: element.value || 'No Value',
        timestamp: new Date().toISOString()
    };
    window.interactionLogs.push(interaction);
});

// Log Key Presses
document.addEventListener('keydown', function(event) {
    const interaction = {
        type: 'keydown',
        key: event.key || 'No Key',
        code: event.code || 'No Code',
        timestamp: new Date().toISOString()
    };
    window.interactionLogs.push(interaction);
});

// Log Form Submissions
document.addEventListener('submit', function(event) {
    const form = event.target;
    const interaction = {
        type: 'submit',
        tagName: form.tagName,
        id: form.id || 'No ID',
        name: form.name || 'No Name',
        className: form.className || 'No Class',
        action: form.action || 'No Action',
        method: form.method || 'No Method',
        timestamp: new Date().toISOString()
    };
    window.interactionLogs.push(interaction);
});

// Log Mouse Movements
document.addEventListener('mousemove', function(event) {
    const interaction = {
        type: 'mousemove',
        x: event.clientX,
        y: event.clientY,
        timestamp: new Date().toISOString()
    };
    window.interactionLogs.push(interaction);
});

// Log Focus Events
document.addEventListener('focus', function(event) {
    const element = event.target;
    const interaction = {
        type: 'focus',
        tagName: element.tagName,
        id: element.id || 'No ID',
        name: element.name || 'No Name',
        className: element.className || 'No Class',
        timestamp: new Date().toISOString()
    };
    window.interactionLogs.push(interaction);
}, true);

// Log Blur Events
document.addEventListener('blur', function(event) {
    const element = event.target;
    const interaction = {
        type: 'blur',
        tagName: element.tagName,
        id: element.id || 'No ID',
        name: element.name || 'No Name',
        className: element.className || 'No Class',
        timestamp: new Date().toISOString()
    };
    window.interactionLogs.push(interaction);
}, true);
"""
try:
    # Open the target URL
    driver.get("https://d2l.arizona.edu/d2l/home/1487536")
    print("Page title is:", driver.title)
    try:
    # Wait for the element to be clickable and click it
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ualoginbutton"))
        ).click()
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys("ksprudhvi")
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("Rp@251994Pru02")  # Replace with actual password
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "_eventId_proceed"))
        )
        login_button.click()# Replace with actual username
    except TimeoutException:
        # Gracefully skip if the element is not found or not clickable
        print("ualoginbutton is not clickable or not found, skipping...")
    print("Login step 1")
    #d2l_1_87_314
    # Optional: Wait until the page fully loads after login
    # time.sleep(5)  # Adjust as necessary or use additional waits for specific elements
    # browserPopUp = WebDriverWait(driver, 5).until(
    #     EC.element_to_be_clickable((By.ID, "d2l_1_87_314"))
    # )
    # got_it_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Got It')]"))
    # )
    # got_it_button.click()
    print("Login step 2")
    #browserPopUp.click()
    # Continue with your tasks
    assignments_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Assignments"))
    )
    assignments_button.click()
    print("Login step 3")
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        (() => {
            const originalPolicy = document.securityPolicy;
            Object.defineProperty(document, 'securityPolicy', {
                value: {
                    get: () => ({})
                }
            });
        })();
    """
    })

    #driver.execute_script(js_script)
    print("Logged in successfully.")


    time.sleep(5)
    print("Login step 4")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@title='View Midterm 2 dropbox for online students submissions']")
        )
    )

    # Click the element
    element.click()
    driver.execute_script("UI.GC('z_g').g_sa(true);")

    driver.execute_script('D2L.O("__gctl_23",0)();')
    driver.execute_script("UI.GC('z_g').g_sa(true);")

    driver.execute_script('D2L.O("__gctl_23",0)();')
    try:
        # Wait for the label with id 'z_e' to contain the text "Your file is ready to download."
        # Locate and click the button
        download_button = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'd2l-button') and text()='Download']"))
        )
        download_button.click()
        print("Download button clicked.")
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(1000)
    #driver.execute_script("SetReturnPoint('D2L.LE.Dropbox.EvaluateDropboxSubmission.2217914'); var n=new D2L.NavInfo(); n.action='Custom'; n.actionParam='feedback,409497, 2'; Nav.Go(n, false, false);")
    interaction_logs = driver.execute_script("return window.interactionLogs || [];")

# Save logs to a file
    with open("interaction_logs.txt", "w") as log_file:
        for log in interaction_logs:
            log_file.write(f"{log}\n")
    # Keep browser open for further interactions as needed


finally:
    # Close the browser
    driver.quit()
