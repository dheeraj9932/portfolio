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

The site is deployed from the root of the `main` branch in `dheeraj9932/portfolio`.

Live URL: <https://dheeraj9932.github.io/portfolio/>

GitHub Pages serves `index.html`, `styles.css`, `script.js`, and `assets/` directly. All asset paths are relative to the project root.
