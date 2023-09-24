from fastapi import FastAPI
from dotenv import load_dotenv
from src.auth.router import auth_routes
from src.github.router import users_github_routes

app = FastAPI()

load_dotenv()

app.include_router(auth_routes, prefix='/api')
app.include_router(users_github_routes, prefix='/api')