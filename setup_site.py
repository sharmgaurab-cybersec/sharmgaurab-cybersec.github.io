"""Set the real GitHub Pages address and optional Google verification tag.

Usage: python setup_site.py YOUR_ACTUAL_GITHUB_USERNAME
Optional: python setup_site.py USERNAME --verification-token GOOGLE_TOKEN
Uses only the Python standard library. No account credentials are needed.
"""

import argparse
import html
import json
import re
from pathlib import Path


def configure(username, verification_token=None, root=None):
    username = username.lower()
    if not re.fullmatch(r"(?=.{1,39}$)[a-z0-9]+(?:-[a-z0-9]+)*", username):
        raise ValueError("Use your actual GitHub username, with letters, digits, and single hyphens.")
    if verification_token is not None and not re.fullmatch(r"[A-Za-z0-9_-]+", verification_token):
        raise ValueError("Pass only the content value from Google's verification tag.")
    root = Path(root) if root is not None else Path(__file__).resolve().parent
    origin = f"https://{username}.github.io/"
    structured_data = {
        "@context": "https://schema.org",
        "@type": "ProfilePage",
        "url": origin,
        "name": "Gaurab Sharma | IT Support & Cybersecurity Portfolio",
        "mainEntity": {
            "@type": "Person",
            "@id": origin + "#person",
            "name": "Gaurab Sharma",
            "url": origin,
            "jobTitle": "Technical Associate – IT Asset & Deployment",
            "description": "IT deployment professional and Bachelor of IT (Cyber Security) student in Sydney, developing practical defensive cybersecurity skills.",
            "knowsAbout": ["Windows deployment", "IT asset management", "Networking fundamentals", "Vulnerability assessment"],
        },
    }
    identity = [
        '  <link rel="canonical" href="' + html.escape(origin, quote=True) + '">',
        '  <meta property="og:url" content="' + html.escape(origin, quote=True) + '">',
        '  <script type="application/ld+json">',
        json.dumps(structured_data, ensure_ascii=False, indent=2),
        '  </script>',
    ]
    index = root / "index.html"
    source = index.read_text(encoding="utf-8")
    pattern = r"  <!-- SITE-IDENTITY-START -->.*?  <!-- SITE-IDENTITY-END -->"
    if not re.search(pattern, source, flags=re.S):
        raise ValueError("The identity markers are missing from index.html.")
    existing = re.search(r'<meta name="google-site-verification" content="([A-Za-z0-9_-]+)">', source)
    token = verification_token or (existing.group(1) if existing else None)
    if token:
        identity.append('  <meta name="google-site-verification" content="' + token + '">')
    block = "  <!-- SITE-IDENTITY-START -->\n" + "\n".join(identity) + "\n  <!-- SITE-IDENTITY-END -->"
    source = re.sub(pattern, lambda match: block, source, count=1, flags=re.S)
    index.write_text(source, encoding="utf-8")
    (root / "robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: " + origin + "sitemap.xml\n", encoding="utf-8")
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>' + origin + '</loc></url>\n</urlset>\n'
    (root / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    return origin


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("username", help="Your actual GitHub username")
    parser.add_argument("--verification-token", help="The content value from the Google Search Console HTML verification tag")
    args = parser.parse_args()
    try:
        address = configure(args.username, args.verification_token)
    except ValueError as error:
        parser.error(str(error))
    print("Search files configured for " + address)
    print("This prepares the files; it does not create a GitHub repository, publish the website, or submit it to Google.")
