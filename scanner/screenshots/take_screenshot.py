from playwright.sync_api import sync_playwright
from datetime import datetime
from pathlib import Path

def take_screenshot(url: str, output_dir: str = "."):
    """Buka situs pake browser headless, ambil screenshot, simpen ke file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    domain_clean = url.replace("https://", "").replace("http://", "").replace("/", "_")
    filename = f"{output_dir}/{domain_clean}_{timestamp}.png"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            page.goto(url, timeout=15000)
            page.screenshot(path=filename)
            browser.close()
            return {"url": url, "status": "success", "file": filename}
        except Exception as e:
            browser.close()
            return {"url": url, "status": "failed", "error": str(e)}

if __name__ == "__main__":
    result = take_screenshot("http://scanme.nmap.org")
    print(result)
