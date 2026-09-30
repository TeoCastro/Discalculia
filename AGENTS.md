# AGENTS.md

## Project Overview
Discalculia is a simple interactive UI originally written as a Python tkinter desktop app (`Discalculia.py`). It has been converted to a web app (Vite + vanilla HTML/CSS/JS) so it can run in the Base44 preview.

The original `Discalculia.py` is kept as reference. The web version replicates the same behavior: a top label, a row of six labels, a button, a text entry, and a combobox. Clicking the button copies the entry value into `texto1` and the combobox value into `texto2`.

## Running
- `docker compose -f docker-compose.base44.yml up -d` — starts the Vite dev server on port 3000.
- No external credentials or services are needed.
- Vite serves the source live with HMR; edits appear without rebuilding the image.

## Tech Stack
- Vite 6 (dev server only, no build step required for this simple app)
- Vanilla HTML/CSS/JS — no framework
