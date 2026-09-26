# EARTH NOW — PUBLIC FINISH LINE

EARTH NOW is finished when a stranger can open the public URL on a phone or desktop and immediately understand, explore, trust, and share it.

## Verified now
- GitHub Pages deployment exists and latest observed Pages run succeeded.
- Scheduled public-data ingest is active.
- Archive index is accumulating snapshots.
- Current feeds: USGS earthquakes, NASA EONET natural events, NASA/JPL close approaches.
- THEN timeline, layer controls, source cards, random exploration, mobile CSS exist.
- Principle: **IF IT GLOWS, IT HAPPENED.**

## Release gates
- [x] Fix dynamic snapshot source-object normalization in frontend.
- [ ] Browser smoke test: initial load, globe render, every layer toggle, event card, source link, overview, random, timeline, play/pause, now.
- [ ] Mobile smoke test at narrow viewport and touch interaction.
- [ ] Confirm historical archive path loading from GitHub Pages.
- [x] Add deterministic archived data-contract tests.
- [x] Add ingest validation tests and CI.
- [x] Add accessible loading/error state and no-WebGL fallback.
- [x] Performance pass: bound dense globe rendering while preserving full observation counts.
- [x] Provenance pass: make semantic status obvious for NEO visualization anchors.
- [x] Metadata/share pass: Open Graph/social metadata, canonical URL, favicon.
- [x] Final copy pass: reduce first-screen explanation.
- [ ] Release tag after all gates pass.

## Scope lock
Do not add new layers until the release gates pass. Lightning, raster weather/ocean fields, operational satellite ephemerides, aurora imagery, WINDOW, and other expansions are post-release.

## Definition of done
A public visitor can load EARTH NOW, see authentic observations, inspect provenance, travel through the current observation window, and use the core experience without knowing the project or reading documentation first.

## Automated verification
- Earth Now CI passed after introduction of the release contract checks.
- GitHub Pages successfully deployed the release-checklist revision.
- Archive manifest currently references real snapshot files; CI verifies those referenced files exist in the repository.
