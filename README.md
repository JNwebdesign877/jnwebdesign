# JN design website

Plain HTML, CSS and JS in three languages. No Lovable, no Node.

- `site/` is the finished website, and the only folder you publish. English (the default) is in `site/`, Finnish in `site/fi/`, Swedish in `site/sv/`.
- `site/demos/g-class/` holds the G-Class demo. Put new demos in `site/demos/<name>/` and add a card for each one to `src/templates/work.html`.
- `src/` holds the page templates (`templates/`) and all the text (`strings/fi.json`, `sv.json`, `en.json`).

## Change text or prices
1. Edit the text in `src/strings/fi.json`, `sv.json` and `en.json`.
2. Rebuild the pages. In PowerShell:

       powershell -ExecutionPolicy Bypass -File "$env:USERPROFILE\jn-design\src\build.ps1"

Styles are in `site/assets/css/style.css` and need no rebuild.

## View it
Double-click `site/index.html`. To see the animations when Windows has "Animation effects" turned off, add `?motion=1` to the end of the address.

## Netlify
The site is the Netlify project **jnwebdesign** (https://jnwebdesign.netlify.app), with form detection on. To publish changes, ask Claude to deploy `site/` to the jnwebdesign project. Or drag the `site` folder (not `jn-design`) onto the project's Deploys page at app.netlify.com/projects/jnwebdesign/deploys.

`site/.netlify/state.json` only holds the project id, which links the folder to the project.

Domain: `jnwebdesign.com` is registered at Name.com. Email runs on Google (MX record), so only change the website records:
- `A` record for `@` pointing to `75.2.60.5`
- `CNAME` record for `www` pointing to `jnwebdesign.netlify.app`
