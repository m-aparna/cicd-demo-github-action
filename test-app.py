import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# This finds the absolute path of the folder where app.py sits
current_dir = os.path.dirname(os.path.realpath(__file__))
template_path = os.path.join(current_dir, "templates")

templates = Jinja2Templates(directory=template_path)

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "status": "Online", 
        "version": "2.0.0 (FastAPI)"
    })