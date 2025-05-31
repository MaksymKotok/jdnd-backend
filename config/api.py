from ninja import NinjaAPI, Swagger

api = NinjaAPI()

api.add_router("users/", "apps.users.api.router")
api.add_router("characters/", "apps.characters.api.router")


@api.get("/")
def echo(request):
    return {"msg": "Roll D20!"}
