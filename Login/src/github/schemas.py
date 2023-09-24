from pydantic import BaseModel

class UsersGithub(BaseModel):
    country: str
    page: str