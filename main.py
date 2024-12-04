from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from colorama import Fore, init

import argparse
import logging
import threading
import time
import sys

init(autoreset=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%H:%M:%S'
)

class EvilKahootFlood:
    def __init__(self):
        self.run = False
        self.url = "https://kahoot.it"

    def setup_browser(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-accelerated-2d-canvas")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-application-cache")
        options.add_argument("--incognito")
        options.add_argument("--disable-default-apps")
        options.add_argument("--log-level=3")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        options.add_argument("--enable-automation")

        if sys.platform == "win32":
            chrome_driver_path = "chromedriver.exe"
        else:
            chrome_driver_path = "chromedriver"

        return webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    def pin_input(self, pin, browser, wait):
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#game-input')))
        browser.find_element(By.CSS_SELECTOR, '#game-input').send_keys(pin)
        browser.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

    def nickname(self, name, browser, wait):
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#nickname')))
        browser.find_element(By.CSS_SELECTOR, '#nickname').send_keys(name)
        browser.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

    def setup_bot(self, pin, name):
        try:

            browser = self.setup_browser()
            browser.get(self.url)

            wait = WebDriverWait(browser, 10)

            self.pin_input(pin, browser, wait)
            self.nickname(name, browser, wait)

            logging.info(Fore.GREEN + f"Bot connected: {name}")

            while self.run:
                time.sleep(1)

            browser.close()
            browser.quit()

        except Exception as e:
            logging.error(Fore.RED + f"Error in bot {name}: {e}")

    def start(self, pin, count, name):
        self.run = True
        for i in range(count):
            print(f"{name}#{i}")
            threading.Thread(target=self.setup_bot, args=(pin, f"{name}#{i}")).start()
            time.sleep(0.1)

    def stop(self):
        self.run = False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Kahoot Bot Flooder: Automate joining Kahoot games with multiple bots.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "-p", "--pin",
        type=int,
        required=True,
        help="The game PIN to join (e.g., 1234567)."
    )
    parser.add_argument(
        "-c", "--count",
        type=int,
        required=True,
        help="Number of bots to create (e.g., 50)."
    )
    parser.add_argument(
        "-n", "--name",
        type=str,
        required=True,
        help="Base name for bots (e.g., BotName)."
    )

    args = parser.parse_args()
    flood = EvilKahootFlood()

    try:
        logging.info(Fore.YELLOW + "Starting bots...")
        flood.start(args.pin, args.count, args.name)
    except KeyboardInterrupt:
        logging.info(Fore.YELLOW + "Stopping bots...")
        flood.stop()