from ninja import NinjaAPI, Swagger
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI


api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)


api.add_router("users/", "apps.users.api.router")
api.add_router("characters/", "apps.characters.api.router")


@api.get("/")
def echo(request):
    return {"msg": "Roll D20!"}
