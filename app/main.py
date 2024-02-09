from datetime import datetime
from fastapi import FastAPI, Form, Request, Cookie
from fastapi.responses import RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jose import jwt

from .repository import CommentsRepository, User, UsersRepository

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")


templates = Jinja2Templates(directory="templates")
comment_repo = CommentsRepository()
user_repo = UsersRepository()


# JWT part
def create_jwt(user_id: int) -> str:
    body = {"user_id": user_id}
    token = jwt.encode(body, "voxpop-secret", "HS256")
    return token
    
def decode_jwt(token: str) -> int:
    data = jwt.decode(token, "voxpop-secret", "HS256") # json
    return data["user_id"]

# Home page
@app.get("/")
def index(request: Request, token:str = Cookie(default="")):
    if token == "":
        return RedirectResponse("/login", 303)
    
    user_id = decode_jwt(token)
    user = user_repo.get_by_id(int(user_id))
    return templates.TemplateResponse("index.html", {"request": request, "user": user})


@app.get("/login")
def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
def post_login(
    request: Request, response: Response, login: str = Form(), pwd: str = Form()
):
    user = user_repo.get_by_login(login)
    if not user:
        return Response("Not authorized login", 401)
    if user.password == pwd:
        response = RedirectResponse("/", 303)
        # JWT:
        token = create_jwt(user.id)
        response.set_cookie("token", token)
        
        return response
    return Response("Password Doesn't match", 401)
    

# Read:
@app.get("/comments")
def get_cars(request: Request, category: str = "All", page: int = 1, limit: int = 3, sort: str = "desc"):
    comments = comment_repo.get_all()
    # Filter by category
    if category != "All":
        filtered_comments = [comment for comment in comments if comment["category"] == category]
    else: 
        filtered_comments = comments
        
    # Pagination
    start = (page - 1) * limit
    end = start + limit
    filtered_comments = filtered_comments[start:end]
    
    # Filter by order
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
    

# Create
@app.post("/comments")
def post_car(request: Request, username:str = Form(), commentText:str = Form(...), commentCategory:str = Form(...)):
    current_datetime = datetime.now()
    comment_repo.save(
        {
            "name": username,
            "comment_date": datetime(current_datetime.year, current_datetime.month, current_datetime.day, current_datetime.hour, current_datetime.minute, current_datetime.second),
            "context": commentText,
            "category": commentCategory
        }
    )
    return RedirectResponse("/comments", status_code=303)
    