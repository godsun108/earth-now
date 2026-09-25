# EARTH NOW 🌎

**What is Earth doing right now?**

A cinematic, zero-login window into current Earth systems and near-Earth space.

## v2
Live layers:
- USGS earthquakes — past 24 hours
- NASA EONET open wildfires
- NASA EONET severe storms
- NASA EONET volcanic events
- NASA EONET icebergs
- NASA EONET dust/haze events
- NASA/JPL CNEOS close approaches within 10 lunar distances over the next 7 days

The interface includes independent layer controls, event provenance, timestamps, coordinates, source links, significant-event pulses, five-minute refresh, graceful partial-feed failure, mobile support, **TAKE ME SOMEWHERE**, and **OVERVIEW**.

Live site: https://godsun108.github.io/earth-now/

## Important spatial semantics
Earth-event markers use observed geographic coordinates. Close-approach objects do **not** have an Earth surface latitude/longitude in the JPL close-approach feed; their globe positions are deterministic visualization anchors at orbital altitude, not claimed geographic positions. Their real close-approach distance, time, and relative velocity are shown from JPL data.

## Still outside the zero-key static architecture
Some parts of the larger vision need a backend, credentials, specialized raster/stream infrastructure, or a different visualization model before they can be represented truthfully: global lightning, continuous weather/ocean fields, full satellite ephemerides, auroral ovals, and historical time-scrubbing. They should not be faked merely to fill the globe.

## Principle
**If it glows, it happened.**

Observed events are never replaced with decorative fake activity. Any illustrative geometry is explicitly described as such.
