from fastapi import Request
from src.auth.utils import validate_token
from fastapi.routing import APIRoute

class VerifyTokenRoute(APIRoute):
    def get_route_handler(self):
        original_route = super().get_route_handler()

        async def verify_token_middleware(request:Request):
            token = request.headers['Authorization'].split(" ")[1]

            validate_response = validate_token(token, output=False)

            if validate_response == None:
                return await original_route(request)
            else:
                return validate_response
            
        return verify_token_middleware