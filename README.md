# EARTH NOW 🌎

**What is Earth doing right now?**

A cinematic real-time window into the planet, backed by real observations.

## v0.1
- interactive 3D globe
- live USGS earthquakes from the past 24 hours
- click events for magnitude, place, depth, and time
- **TAKE ME SOMEWHERE** flies to a significant current event
- source and freshness status

## Run
Serve this directory with any static web server:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Principle
**If it glows, it happened.**

Visual activity should correspond to real sourced observations. Simulated or illustrative layers must be explicitly labeled.
