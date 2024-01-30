from datetime import datetime
from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse, Response
from fastapi.templating import Jinja2Templates

from .repository import CommentsRepository

app = FastAPI()

templates = Jinja2Templates(directory="templates")
repository = CommentsRepository()


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/comments")
def get_cars(request: Request, category: str = "All"):
    comments = repository.get_all()
    if category == "All":
        filtered_comments = comments
    else:
        filtered_comments = [comment for comment in comments if comment["category"] == category]
    return templates.TemplateResponse(
        "comments/index.html",
        {"request": request, "comments": filtered_comments},
    )

@app.post("/comments/new")
def post_car(request: Request, username:str = Form(), commentText:str = Form(...), commentCategory:str = Form(...)):
    repository.save(
        {
            "name": username,
            "comment_date": datetime.now().strftime("%d.%m.%Y"),
            "context": commentText,
            "category": commentCategory
        }
    )
    return RedirectResponse("/comments", status_code=303)
    