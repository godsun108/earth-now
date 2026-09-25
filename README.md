# EARTH NOW 🌎

**What is Earth doing right now?**

A cinematic, zero-login window into current planetary activity.

## Complete v1
EARTH NOW combines public observation feeds on an interactive 3D globe:
- USGS earthquakes from the past 24 hours
- NASA EONET open wildfire events
- NASA EONET open severe-storm events
- NASA EONET open volcanic events
- layer toggles, source/freshness details, pulsing significant activity
- **TAKE ME SOMEWHERE** chooses from currently visible real events
- automatic refresh every five minutes
- responsive mobile interface

Live site: https://godsun108.github.io/earth-now/

## Data semantics
“Current” does not mean every feed is second-by-second. USGS and NASA publish on their own observation/update cadences. EARTH NOW displays the source and observation time when supplied. EONET is a curated metadata system for natural events; an “open” event can persist beyond its latest geometry timestamp.

## Principle
**If it glows, it happened.**

No decorative event markers are presented as observations. A simulated or illustrative layer must be explicitly labeled before it can be added.

## Architecture
Static HTML/CSS/JS, Globe.gl, no account system, no backend, no API secrets. This keeps the first public release inspectable and inexpensive to operate.
