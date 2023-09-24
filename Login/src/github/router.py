from fastapi import APIRouter
from src.github.schemas import UsersGithub
from requests import get
from src.middlewares.verify_token_route import VerifyTokenRoute

users_github_routes = APIRouter(route_class=VerifyTokenRoute)

@users_github_routes.post("/users/github")
def github_users(github: UsersGithub):
    return get(f'https://api.github.com/search/users?q=location:"{github.country}"&page={github.page}').json()