"""
Orchestrator Modul 1 — manggil semua tools scan buat satu domain,
gabungin hasilnya jadi satu laporan JSON.
"""
import json
from datetime import datetime
from pathlib import Path

from dorking.dork_scanner import scan_domain as run_dorking
from fingerprint.ssl_check import check_ssl
from fingerprint.cms_fingerprint import detect_cms
from recon.shodan_check import check_shodan
from recon.virustotal_check import check_reputation
from screenshots.take_screenshot import take_screenshot


def scan_full(domain: str):
    """Jalanin semua tools Modul 1 buat 1 domain, balikin 1 laporan gabungan"""
    print(f"[1/6] Dorking...")
    dorking_result = run_dorking(domain)

    print(f"[2/6] SSL check...")
    ssl_result = check_ssl(domain)

    print(f"[3/6] CMS fingerprint...")
    fingerprint_result = detect_cms(f"https://{domain}")

    print(f"[4/6] Shodan...")
    shodan_result = check_shodan(domain)

    print(f"[5/6] VirusTotal...")
    vt_result = check_reputation(domain)

    print(f"[6/6] Screenshot...")
    # coba https dulu, kalau gagal fallback ke http
    screenshot_result = take_screenshot(f"https://{domain}")
    if screenshot_result.get("status") == "failed":
        screenshot_result = take_screenshot(f"http://{domain}")

    report = {
        "domain": domain,
        "scanned_at": datetime.now().isoformat(),
        "dorking": dorking_result,
        "ssl": ssl_result,
        "fingerprint": fingerprint_result,
        "shodan": shodan_result,
        "virustotal": vt_result,
        "screenshot": screenshot_result,
    }
    return report


def save_report(report: dict, output_dir: str = "results"):
    """Simpen laporan jadi file JSON, nama file otomatis pake domain + timestamp"""
    Path(output_dir).mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/{report['domain']}_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)
    return filename


if __name__ == "__main__":
    target = "google.com"
    print(f"=== Mulai scan penuh untuk: {target} ===\n")

    result = scan_full(target)
    saved_path = save_report(result)

    print(f"\n=== Selesai. Laporan tersimpan di: {saved_path} ===")
