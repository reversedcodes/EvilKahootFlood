# Kahoot Bot Flooder 🎉

A powerful Kahoot bot flooder that allows you to join a Kahoot game with multiple bots. This script requires you to manually download and configure ChromeDriver for your system.

---

## 📋 Features

- **Multi-bot Support**: Add any number of bots to a Kahoot game.
- **Custom ChromeDriver Setup**: Use your own ChromeDriver installation.
- **Headless Execution**: Bots run entirely in the background.
- **Name Validation**: Automatically shortens bot names if they exceed Kahoot's character limit.
- **Simple Command-Line Interface (CLI)**: Configure the game PIN, bot count, and base name directly from the terminal.

---

## 🚀 Installation

### Prerequisites

1. **Python**: Version 3.8 or higher.
2. **Google Chrome**: Latest version.
3. **ChromeDriver**: Match the version of your Chrome browser.

---

### Step 1: Clone the Repository

```bash
git clone https://github.com/reversedcodes/EvilKahootFlood.git
cd kahoot-bot-flooder
```

### Step 2: Install Dependencies

Install the required Python libraries:
```bash
pip install -r requirements.txt
```

---

## ⚙️ Setting Up ChromeDriver

1. **Check Your Chrome Version**:
   - Open Chrome and go to `chrome://settings/help`.
   - Note the version number (e.g., `116.0.5845.96`).

2. **Download ChromeDriver**:
   - Visit [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).
   - Download the version that matches your Chrome browser.

3. **Place ChromeDriver**:
   - Move the `chromedriver` executable to the same directory as the `main.py` script.

---

## 🔧 Usage

Run the script directly from the terminal:

```bash
python main.py -p <PIN> -c <Bot-Count> -n <Bot-Name>
```

### Arguments

- **`-p`** or `--pin`: The game PIN for the Kahoot game.
- **`-c`** or `--count`: The number of bots to create.
- **`-n`** or `--name`: The base name for bots (e.g., `BotMaster`).

### Example

```bash
python main.py -p 1234567 -c 50 -n BotMaster
```

This will create 50 bots with names like `BotMaster#0`, `BotMaster#1`, ..., `BotMaster#49`.

---

## 🖥️ Development Environment

This project was built with:

- **Python**: Core programming language.
- **Selenium**: Browser automation.
- **Colorama**: Colored console outputs.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🛡️ Disclaimer

This script is for educational purposes only. Use it responsibly.