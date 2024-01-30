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
def get_cars(request: Request, category: str = "Positive"):
    comments = repository.get_all()
    if category == "All":
        filtered_comments = comments
    else:
        filtered_comments = [comment for comment in comments if comment["category"] == category]
    return templates.TemplateResponse(
        "comments/index.html",
        {"request": request, "comments": filtered_comments},
    )

@app.get("/cars/new")
def new_car(request: Request, response: Response):
    return templates.TemplateResponse("cars/new.html", {"request": request})
    
@app.post("/cars/new")
def post_car(request: Request, car_name:str = Form(...), year:str = Form(...)):
    repository.save(
        {
            "name": car_name,
            "year": year
        }
    )
    return RedirectResponse("/cars", status_code=303)
    