from pydantic import BaseModel, EmailStr
#pydantic models

class UserModel(BaseModel):
    username: str
    email: EmailStr