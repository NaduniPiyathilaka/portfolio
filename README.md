# Naduni Piyathilaka — Portfolio Website

A responsive personal portfolio built with plain HTML, CSS, and JavaScript
(no frameworks or build tools required).

## Before you submit — 3 things to fix

1. **Photo**: add your real photo to `assets/profile.jpg` (any image editor/phone
   export works — just keep the filename `profile.jpg`, square photos look best).
   Until you add it, the site shows an "NP" placeholder automatically.
2. **LinkedIn**: open `index.html`, search for `linkedin.com/in/your-profile`
   (appears twice — once in the Contact section, once inside `make_cv.py`'s
   generated PDF), and replace it with your real LinkedIn URL. Then re-run
   `python3 make_cv.py` to regenerate the CV with the correct link, or just
   edit the PDF text directly if you don't have Python set up.
3. **GitHub project links**: replace `https://github.com/yourusername/portfolio`
   with your actual repo link, and add real links for the other two projects
   if you push them to GitHub (currently marked "Repository link coming soon").
4. **Email**: replace `yourname@gmail.com` with your real email address
   (appears in the Contact section and in `make_cv.py`).

## Files

```
portfolio/
├── index.html          → main page
├── style.css            → all styling
├── script.js            → typing effect, scroll reveal, mobile nav
├── make_cv.py            → regenerates the downloadable CV PDF
├── assets/
│   ├── profile.jpg       → ADD YOUR PHOTO HERE
│   └── Naduni_Piyathilaka_CV.pdf → auto-generated downloadable CV
└── README.md
```

## Deploy — Option A: GitHub Pages (recommended, free)

1. Create a new GitHub repository (e.g. `portfolio`).
2. Upload all files in this folder to the repo (keep the folder structure,
   especially the `assets/` folder).
3. Go to **Settings → Pages** in your repo.
4. Under "Build and deployment", set **Source: Deploy from a branch**,
   branch: `main`, folder: `/ (root)`. Click **Save**.
5. Wait 1–2 minutes, then your site will be live at:
   `https://<your-username>.github.io/<repo-name>/`

## Deploy — Option B: Vercel (free)

1. Push this folder to a GitHub repository (same as steps 1–2 above).
2. Go to [vercel.com](https://vercel.com), sign in with GitHub.
3. Click **Add New → Project**, select your repository.
4. Leave all settings as default (no framework/build step needed) and click **Deploy**.
5. Vercel gives you a live URL like `https://portfolio-yourname.vercel.app/`.

## For your CA submission

1. Copy your final live URL (from GitHub Pages or Vercel).
2. Paste it into a Word document.
3. Save/export that Word document as a **PDF**.
4. Upload the PDF to the LMS submission link.

## Customizing later

- Colors and fonts: edit the `:root` variables at the top of `style.css`.
- Add a new project: copy one `<article class="project-card">...</article>`
  block in `index.html` and edit the text.
- Add a real achievement: copy the `.achievement-card` block in the
  Achievements section and fill in a real certificate/award.
