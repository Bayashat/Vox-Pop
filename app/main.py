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
def get_cars(request: Request, category: str = "All", page: int = 1, limit: int = 3, sort: str = "desc"):
    comments = repository.get_all()
    start = (page - 1) * limit
    end = start + limit
    filtered_comments = comments[start:end]
    
    if category != "All":
        filtered_comments = [comment for comment in filtered_comments if comment["category"] == category]
    else: 
        filtered_comments = filtered_comments
    if sort == "desc":
        filtered_comments = sorted(filtered_comments, key=lambda comment: comment["comment_date"], reverse=True)
    elif sort == "asc":
        filtered_comments = sorted(filtered_comments, key=lambda comment: comment["comment_date"])
    else:
        raise ValueError("Invalid sort value")
    return templates.TemplateResponse(
        "comments/index.html",
        {
            "request": request, 
            "comments": comments,
            "filtered_comments": filtered_comments,
            "category": category,
            "page": page,
            "limit": limit,
            "sort": sort,
        },
    )
    

@app.post("/comments/new")
def post_car(request: Request, username:str = Form(), commentText:str = Form(...), commentCategory:str = Form(...)):
    current_datetime = datetime.now()
    repository.save(
        {
            "name": username,
            "comment_date": datetime(current_datetime.year, current_datetime.month, current_datetime.day, current_datetime.hour, current_datetime.minute, current_datetime.second),
            "context": commentText,
            "category": commentCategory
        }
    )
    return RedirectResponse("/comments", status_code=303)
    