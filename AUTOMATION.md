# InnerWorks Metrics Automation

Automate sending metrics from Chrome, Firefox, and Brave browsers.

## Prerequisites

1. **Python 3.7+** installed
2. **Browsers installed:**
   - Chrome
   - Firefox
   - Brave Browser

3. **Browser Drivers:**
   - ChromeDriver (for Chrome & Brave)
   - GeckoDriver (for Firefox)

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Browser Drivers

**macOS (using Homebrew):**
```bash
brew install chromedriver geckodriver
```

**Linux:**
```bash
# ChromeDriver
wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE
# Follow installation instructions

# GeckoDriver
wget https://github.com/mozilla/geckodriver/releases/latest
# Follow installation instructions
```

**Windows:**
Download and add to PATH:
- [ChromeDriver](https://chromedriver.chromium.org/downloads)
- [GeckoDriver](https://github.com/mozilla/geckodriver/releases)

## Configuration

Edit `automate_metrics.py`:

```python
# Change URL to your deployed URL or ngrok URL
URL = "http://localhost:5173"  # or "https://your-app.netlify.app"

# Change device name
DEVICE_NAME = "LenovoY520Ubuntu"
```

## Usage

### Run Automation

```bash
python3 automate_metrics.py
```

### Run in Headless Mode (Background)

Uncomment the headless option in the script:

```python
options.add_argument('--headless')  # Uncomment this line
```

Then run:
```bash
python3 automate_metrics.py
```

## What It Does

1. **Opens Chrome browser**
   - Fills device name: "LenovoY520Ubuntu"
   - Selects browser: "Chrome"
   - Clicks "Yuborish" button
   - Waits for success message
   - Closes browser

2. **Opens Firefox browser**
   - Same process with Firefox selected

3. **Opens Brave browser**
   - Same process with Brave selected

## Output Example

```
============================================================
🤖 InnerWorks Metrics Automation Started
============================================================
🌐 Target URL: http://localhost:5173
💻 Device Name: LenovoY520Ubuntu
🔧 Browsers: Chrome, Firefox, Brave
============================================================

🌐 Opening Chrome...
✅ Chrome opened: http://localhost:5173
📝 Device Name entered: LenovoY520Ubuntu
🔽 Browser selected: Chrome
🚀 Sending metrics...
✅ Success: Muvaffaqiyatli! Metrikalar yuborildi...
🔒 Chrome closed

🌐 Opening Firefox...
✅ Firefox opened: http://localhost:5173
📝 Device Name entered: LenovoY520Ubuntu
🔽 Browser selected: Firefox
🚀 Sending metrics...
✅ Success: Muvaffaqiyatli! Metrikalar yuborildi...
🔒 Firefox closed

🌐 Opening Brave...
✅ Brave opened: http://localhost:5173
📝 Device Name entered: LenovoY520Ubuntu
🔽 Browser selected: Brave
🚀 Sending metrics...
✅ Success: Muvaffaqiyatli! Metrikalar yuborildi...
🔒 Brave closed

============================================================
✅ Automation Completed Successfully!
============================================================
```

## Troubleshooting

### Brave Browser Not Found
Update the Brave binary path in the script:
```python
# For macOS
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

# For Linux
options.binary_location = "/usr/bin/brave-browser"

# For Windows
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
```

### ChromeDriver Version Mismatch
```bash
# Check Chrome version
chrome --version

# Install matching ChromeDriver version
brew install chromedriver@<version>
```

### Selenium Not Found
```bash
pip install selenium
```
