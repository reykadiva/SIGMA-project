import os
import shodan
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).resolve().parents[2] / ".env")
SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")

def check_shodan(ip_or_domain: str):
    """Nanya ke database Shodan: port apa aja yang kebuka & service apa yang jalan"""
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        # Shodan butuh IP, bukan domain langsung — kalau lo kasih domain,
        # perlu resolve ke IP dulu (kita handle simpel di sini)
        import socket
        ip = socket.gethostbyname(ip_or_domain)

        result = api.host(ip)
        open_ports = result.get("ports", [])
        services = [
            {"port": item["port"], "product": item.get("product", "unknown")}
            for item in result.get("data", [])
        ]

        return {
            "domain": ip_or_domain,
            "ip": ip,
            "open_ports": open_ports,
            "services": services
        }
    except shodan.APIError as e:
        return {"domain": ip_or_domain, "error": str(e)}

if __name__ == "__main__":
    result = check_shodan("scanme.nmap.org")
    print(result)
