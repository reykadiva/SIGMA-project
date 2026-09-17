import os
import vt
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).resolve().parents[2] / ".env")
VT_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

def check_reputation(domain: str):
    """Nanya ke VirusTotal: domain ini pernah dilaporin berbahaya sama vendor antivirus mana aja"""
    client = vt.Client(VT_API_KEY)
    try:
        obj = client.get_object(f"/domains/{domain}")
        stats = obj.last_analysis_stats
        # stats itu dictionary isinya jumlah vendor yang bilang: malicious, suspicious, harmless, undetected
        return {
            "domain": domain,
            "malicious": stats.get("malicious", 0),
            "suspicious": stats.get("suspicious", 0),
            "harmless": stats.get("harmless", 0),
            "undetected": stats.get("undetected", 0),
            "reputation_score": obj.reputation  # angka, makin negatif makin buruk reputasinya
        }
    except Exception as e:
        return {"domain": domain, "error": str(e)}
    finally:
        client.close()

if __name__ == "__main__":
    result = check_reputation("scanme.nmap.org")
    print(result)
