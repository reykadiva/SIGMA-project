import os
import requests
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).resolve().parents[2] / ".env")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

DORK_KEYWORDS = ["slot gacor", "judi online", "maxwin", "situs togel"]

def search_dork(domain: str, keyword: str):
    """Manggil SerpAPI buat 1 domain + 1 keyword, balikin raw JSON"""
    params = {
        "engine": "google",
        "q": f"site:{domain} {keyword}",
        "api_key": SERPAPI_KEY
    }
    res = requests.get("https://serpapi.com/search", params=params)
    res.raise_for_status()
    return res.json()

def scan_domain(domain: str):
    """Cek 1 domain terhadap SEMUA keyword, balikin hasil ringkas & rapi"""
    findings = []
    for keyword in DORK_KEYWORDS:
        data = search_dork(domain, keyword)
        total_results = data.get("search_information", {}).get("total_results", 0)
        if total_results > 0:
            findings.append({
                "keyword": keyword,
                "total_results": total_results,
                "sample_link": data["organic_results"][0]["link"] if data.get("organic_results") else None
            })
    return {
        "domain": domain,
        "is_suspicious": len(findings) > 0,
        "findings": findings
    }

if __name__ == "__main__":
    result = scan_domain("scanme.nmap.org")
    print(result)
