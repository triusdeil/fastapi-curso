from fastapi import APIRouter, Header
from src.auth.schemas import UserModel
from fastapi.responses import JSONResponse
from src.auth.utils import write_token, validate_token

auth_routes = APIRouter()

@auth_routes.post('/login')
def login(user: UserModel):
    print(user.dict())
    #agregar consulta a la bd si el usuario esta registrado o no
    if user.username == "triusdeil":
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message": "User not found"},status_code=404)
    
@auth_routes.post('/verify/token')
def verify_token(Authorization: str = Header(None)):
    #quitar espacio del token y el bearer
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)

#logout