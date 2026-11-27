# Dheeraj Tippani — Portfolio

Personal portfolio for computer vision, robot perception, 3D understanding, and physical AI. Built with plain HTML, CSS, and JavaScript; no build step or runtime dependencies.

## Run locally

From this directory, run:

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

## Test

Run the dependency-free structural checks:

```bash
python3 -m unittest discover -s tests -v
```

The checks cover real contact links, internal navigation targets, project statuses, and local image assets with alternative text.

## Update content

- Edit page content and project links in `index.html`.
- Edit colors, layout, and responsive rules in `styles.css`.
- Keep local images in `assets/images/` and include useful `alt` text.
- Future work uses `data-status="planned"`; change its visible status and add a repository link only when work begins.

## Deploy with GitHub Pages

Publish `index.html`, `styles.css`, `script.js`, and `assets/` from the root of the `main` branch.

Repository naming determines the public URL:

- A repository named `dheeraj9932.github.io` publishes the user site at `https://dheeraj9932.github.io/`.
- The current `dheeraj.github.io` repository can publish a project site at `https://dheeraj9932.github.io/dheeraj.github.io/` when GitHub Pages is enabled.

All site assets use relative paths, so both deployment styles work.
