import ssl
import socket
from datetime import datetime

def check_ssl(domain: str, port: int = 443):
    """Cek kapan sertifikat SSL suatu domain expired"""
    context = ssl.create_default_context()
    try:
        with socket.create_connection((domain, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                expire_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                days_left = (expire_date - datetime.now()).days
                return {
                    "domain": domain,
                    "ssl_valid": days_left > 0,
                    "expires_in_days": days_left
                }
    except Exception as e:
        return {"domain": domain, "ssl_valid": False, "error": str(e)}

if __name__ == "__main__":
    print(check_ssl("google.com"))
