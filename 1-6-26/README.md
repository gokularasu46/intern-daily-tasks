# Interactive India Map

A single-page interactive India map built with HTML, CSS, JavaScript, and a small Python Flask server.

## Features

- Complete SVG India map with clickable states and union territories
- State names displayed directly on the map
- Hover highlight effects
- Smooth selection animation
- Details panel with 5 key facts for each state/UT
- Simple Flask backend for local hosting

## Files

- `index.html` — main page markup
- `style.css` — application styling
- `script.js` — map interaction and state selection logic
- `states.json` — structured state and union territory data
- `app.py` — Flask server entrypoint
- `requirements.txt` — Python dependency list

## Setup

1. Install Python 3.8+.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Then open the browser at:

```
http://127.0.0.1:8000
```

## Notes

- No external paid APIs are required.
- The site is designed as a single-page experience.
- The SVG map loads immediately on page open.
