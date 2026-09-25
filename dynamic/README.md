# EARTH NOW Dynamic Engine

This directory is the server-side ingestion/archive contract for the next generation of EARTH NOW.

## Design
Public sources -> scheduled ingest -> normalized snapshots -> archive -> browser.

The browser can continue to work without the engine. When `dynamic/latest.json` is available it is preferred; otherwise the existing direct public feeds remain the fallback.

## Snapshot contract
```json
{
  "schema": "earth-now.dynamic.v1",
  "generated_at": "ISO-8601",
  "events": []
}
```

Every event carries `kind`, `title`, `time`, `source`, source URL where available, and observed coordinates only when the source supplies geographic coordinates. Non-geographic orbital data must never masquerade as geographic observation.

## Archive
Scheduled snapshots are intended for `dynamic/archive/YYYY/MM/DD/HH.json`. This turns the time control from a seven-day client filter into a durable observation archive as history accumulates.

## Next infrastructure adapters
Raster/stream adapters belong behind the same provenance contract:
- weather/cloud fields
- ocean temperature/current fields
- lightning
- aurora/space weather
- satellite ephemerides

Each adapter must document cadence, license, timestamp semantics, and whether geometry is observed, calculated, or illustrative.
