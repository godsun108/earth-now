import json, urllib.request, datetime, pathlib

UA={"User-Agent":"earth-now/1.0"}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(req,timeout=30) as r:return json.load(r)

def main():
    now=datetime.datetime.now(datetime.timezone.utc)
    events=[]
    q=get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson")
    for f in q.get("features",[]):
        c=f.get("geometry",{}).get("coordinates",[])
        p=f.get("properties",{})
        if len(c)>=3: events.append({"kind":"quake","lat":c[1],"lng":c[0],"depth":c[2],"mag":p.get("mag") or 0,"title":p.get("place") or "Earthquake","time":p.get("time"),"source":"USGS","url":p.get("url") or ""})
    e=get("https://eonet.gsfc.nasa.gov/api/v3/events?status=all&days=7&limit=500")
    for x in e.get("events",[]):
        cats=" ".join((c.get("id","")+" "+c.get("title","")) for c in x.get("categories",[])).lower()
        kind=next((k for term,k in [("wildfire","wildfire"),("storm","storm"),("volcano","volcano"),("iceberg","iceberg"),("dust","dust")] if term in cats),None)
        if not kind: continue
        for g in x.get("geometry",[]):
            c=g.get("coordinates",[])
            if g.get("type")=="Point" and len(c)>=2:
                t=g.get("date"); ms=int(datetime.datetime.fromisoformat(t.replace("Z","+00:00")).timestamp()*1000) if t else None
                events.append({"kind":kind,"lat":c[1],"lng":c[0],"title":x.get("title") or "Natural event","time":ms,"source":"NASA EONET","url":x.get("link") or ""})
    payload={"schema":"earth-now.dynamic.v1","generated_at":now.isoformat(),"events":events}
    root=pathlib.Path("dynamic"); root.mkdir(exist_ok=True)
    text=json.dumps(payload,separators=(",",":"))
    (root/"latest.json").write_text(text)
    a=root/"archive"/now.strftime("%Y/%m/%d"); a.mkdir(parents=True,exist_ok=True)
    (a/(now.strftime("%H")+".json")).write_text(text)
# Dynamic engine marker: production hourly archive
if __name__=="__main__": main()
