import webtech

def detect_cms(url: str):
    """Deteksi CMS/teknologi suatu situs, termasuk versi kalau kedeteksi"""
    wt = webtech.WebTech(options={'json': True})
    try:
        report = wt.start_from_url(url)
        seen = {}
        for tech in report.get('tech', []):
            name = tech.get('name')
            version = tech.get('version')  # bisa None kalau gak kedeteksi
            # kalau nama sama udah pernah masuk, cuma update kalau versi baru ini lebih lengkap
            if name not in seen or (version and not seen[name]):
                seen[name] = version

        technologies = [
            {"name": name, "version": version if version else "unknown"}
            for name, version in seen.items()
        ]

        return {
            "url": url,
            "technologies": technologies,
            "count": len(technologies)
        }
    except Exception as e:
        return {"url": url, "error": str(e)}

if __name__ == "__main__":
    result = detect_cms("https://wordpress.org")
    print(result)
