import os

_base = os.path.dirname(os.path.abspath(__file__))

def _front(name):
    p1 = os.path.join(_base, name)
    if os.path.isfile(p1):
        return p1
    p2 = os.path.join(_base, "..", "frontend", name)
    if os.path.isfile(p2):
        return p2
    return None

def home_page():
    p = _front("index.html")
    if p:
        return FileResponse(p)
    return {"detail": "Frontend not found"}

@app.get("/index.html")
def index_file():
    p = _front("index.html")
    if p:
        return FileResponse(p)
    raise HTTPException(404, "index.html missing")

@app.get("/app.js")
def app_js_file():
    p = _front("app.js")
    if p:
        return FileResponse(p)
    raise HTTPException(404, "app.js missing")
    import os
_base = os.path.dirname(os.path.abspath(__file__))

def _front(name):
    p1 = os.path.join(_base, name)
    if os.path.isfile(p1):
        return p1
    p2 = os.path.join(_base, "..", "frontend", name)
    if os.path.isfile(p2):
        return p2
    return None

@app.get("/")
def home_page():
    p = _front("index.html")
    if p:
        return FileResponse(p)
    return {"detail": "Frontend not found"}
