# Gaurab Sharma — IT & Cybersecurity Portfolio

Gaurab Sharma's personal IT and cybersecurity portfolio, built with HTML, CSS, and JavaScript. The source files are available to edit and maintain, with free hosting through a public GitHub Pages repository.

## Your GitHub Pages address

Configured GitHub username: `sharmgaurab-cybersec`.

Required public repository name: `sharmgaurab-cybersec.github.io`.

Website address after successful publication: https://sharmgaurab-cybersec.github.io/

The canonical URL, profile data, robots.txt, and sitemap.xml are already configured for this address. The files have not been uploaded to GitHub or submitted to Google.

## 1. Open it on your computer

Extract this ZIP into a folder and open that folder in VS Code.

Open `index.html` in a browser. For a local preview that includes the clipboard interaction, run this from a terminal in the folder:

```powershell
python -m http.server 8000
```

Visit `http://localhost:8000`. Press Ctrl+C in the terminal to stop the preview.

## 2. Set your real website address

Sign in to your own GitHub account, or create a free account at https://github.com/signup. Find your actual username, then run:

```powershell
python setup_site.py sharmgaurab-cybersec
```

The command uses your supplied GitHub username. The script sets the canonical address, profile structured data, `robots.txt`, and `sitemap.xml` for your GitHub Pages address. It does not publish anything or access your account.

## 3. Publish on GitHub Pages

1. Create a **public** repository named `yourusername.github.io`, replacing `yourusername` with your real GitHub username. If that repository already exists, inspect it before uploading anything; do not overwrite an existing site.
2. Upload the files from this folder into the repository root. Keep `index.html`, `styles.css`, and `script.js` together at the top level, rather than inside another folder.
3. Open the repository's **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**. Select **main** and **/(root)**, then save.
5. Wait for deployment, then use **Visit site** in Pages settings to get the published address. GitHub says publication can take up to 10 minutes after a push.

The website and repository are public. The files include only your portfolio content and professional contact email; they do not include your home address, phone number, student ID, passwords, or access tokens.

## 4. Ask Google to index the published website

1. Open https://search.google.com/search-console and sign in to your Google account.
2. Add a **URL-prefix** property using the actual published homepage, such as `https://yourusername.github.io/`. Do not include `#note-nmap`; that suffix just opens a section of the page.
3. Select **HTML tag** verification and copy the value inside `content="..."` from the tag Google provides.
4. Run the following with your actual username and verification value:

```powershell
python setup_site.py sharmgaurab-cybersec --verification-token YOUR_GOOGLE_VERIFICATION_VALUE
```

5. Upload the updated `index.html`, `robots.txt`, and `sitemap.xml` to the repository. Wait for publication, then click **Verify** in Search Console. Keep the verification tag in the page afterwards.
6. In Search Console, submit `sitemap.xml` under **Sitemaps**.
7. Inspect your homepage with **URL inspection** and, if available, choose **Request indexing**.

Google decides whether and when to index a page. A sitemap and an indexing request do not guarantee inclusion or a high ranking. Crawling can take days or weeks. Link the portfolio from your GitHub profile and LinkedIn profile to help visitors and search engines discover it.

## 5. Make this a project you understand

| File | What you can change |
| --- | --- |
| `index.html` | Your introduction, experience, project descriptions, and learning notes |
| `styles.css` | Colours, type, spacing, and layouts for different screen sizes |
| `script.js` | Email-copy behaviour and opening a linked learning note |
| `setup_site.py` | Canonical address, profile data, sitemap, and optional Google verification |

Start with one small edit: rewrite your introduction in your own words. Then change the `--blue` colour in `styles.css`. Next, add a learning note based on a lab you have actually completed. Commit each change with a short description of what you changed and why.

The current project labels distinguish a working local prototype, ongoing lab practice, and a planned AWS concept. Update those labels only as the actual work progresses.

## Official references

- GitHub Pages and free public repositories: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
- Creating and publishing a GitHub Pages site: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- Google Search Console verification: https://support.google.com/webmasters/answer/9008080?hl=en
- Requesting Google indexing: https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl
