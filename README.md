# EARTH NOW 🌎

**What is Earth doing right now?**

A cinematic public window into Earth systems and near-Earth space.

## v3 — full static vision
Layers:
- USGS earthquakes, with a 7-day source window
- NASA EONET wildfires, severe storms, volcanoes, icebergs, and dust/haze
- NASA/JPL CNEOS close approaches

Experience:
- interactive 3D Earth
- independent layer controls
- event source, timestamp, coordinates, and source link
- **TAKE ME SOMEWHERE**
- **OVERVIEW**
- **TIME** — scrub the observation window backward through the last seven days
- automatic refresh and graceful partial-feed failure
- mobile layout and keyboard controls

Live site: https://godsun108.github.io/earth-now/

## Time-machine semantics
The timeline is an **observation-window explorer**, not a reconstructed satellite movie. At each selected time it shows observations present in the loaded public datasets around that window. EONET can provide multiple dated geometries for an event, while USGS supplies discrete earthquake observations.

## Near-Earth spatial semantics
NASA/JPL close-approach data provides encounter time, distance, and velocity but not an Earth-surface latitude/longitude. Those markers therefore use deterministic visualization anchors above the globe. They are not claimed geographic positions.

## Full-vision boundary
The static, no-secret architecture is complete. Continuous global lightning, raster weather/ocean fields, operational satellite ephemerides, and auroral imagery require external tile/stream services, credentials, a backend, or specialized orbital/raster infrastructure. They are intentionally not fabricated.

## Principle
**If it glows, it happened.**

Observed events are never replaced by decorative fake activity. Any visualization geometry that is not an observed geographic position is explicitly identified.
