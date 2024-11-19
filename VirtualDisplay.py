import os
import subprocess
from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Include the noVNC viewer in your HTML

@app.route('/start-selenium')
def start_selenium():
    # Start virtual display
    os.system("Xvfb :99 -screen 0 1920x1080x24 &")
    os.environ["DISPLAY"] = ":99"

    # Start VNC server for interaction
    subprocess.Popen(["x11vnc", "-display", ":99", "-forever", "-shared", "-loop"])

    # Start Selenium browser
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")

    service = Service('/path/to/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://example.com")  # Replace with your target URL

    return "Selenium started and ready for interaction!"

@app.route('/start-stream')
def start_stream():
    # Start websockify for streaming
    subprocess.Popen(["websockify", "5901", "--web", "/path/to/noVNC", "5900"])
    return "Stream started. Open the VNC viewer."

if __name__ == '__main__':
    app.run(debug=True)
