# EARTH NOW 🌎

**What is Earth doing right now?**

A cinematic, zero-login window into current planetary activity.

## v1.1
EARTH NOW combines public observation feeds on an interactive 3D globe:
- USGS earthquakes from the past 24 hours
- NASA EONET open wildfire, severe-storm, and volcanic events
- independent layer controls and observation counts
- source, coordinates, observation age, and source links on event cards
- pulsing significant activity
- **TAKE ME SOMEWHERE** chooses from visible real events
- **OVERVIEW** returns to the living globe
- five-minute automatic data refresh
- resilient partial-feed behavior and responsive mobile UI
- keyboard shortcuts: R = take me somewhere, Esc = overview

Live site: https://godsun108.github.io/earth-now/

## Data semantics
“Current” does not mean every feed is second-by-second. USGS and NASA publish on their own observation/update cadences. EARTH NOW displays source and observation time when supplied. NASA EONET is a curated metadata system; an open event can persist beyond its latest geometry timestamp.

## Principle
**If it glows, it happened.**

No decorative event marker is presented as an observation. Simulated or illustrative layers must be explicitly labeled.

## Architecture
Static HTML/CSS/JS using Globe.gl. No accounts, backend, database, API secrets, or analytics are required for this release.
