from http import HTTPStatus
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from ninja import Router

from apps.characters.schemas import (
    CharacterListSchema,
    CharacterDetailSchema,
    CharacterCreateSchema,
)

from apps.characters.models import (
    Character,
)

router = Router()


@router.get(
    "/",
    response={
        HTTPStatus.OK: list[CharacterListSchema],
        HTTPStatus.NOT_FOUND: dict
    },
    summary="Characters List",
    tags=["Characters"],
)
def characters_list(request) -> QuerySet[Character]:
    return Character.objects.all()


@router.get(
    "/{character_id}/",
    response={
        HTTPStatus.OK: CharacterDetailSchema,
        HTTPStatus.NOT_FOUND: dict
    },
    summary="Character Details",
    tags=["Characters"],
)
def characters_retrieve(request, character_id) -> Character:
    return get_object_or_404(Character, id=character_id)


@router.post(
    "/",
    response={
        HTTPStatus.CREATED: CharacterListSchema,
        HTTPStatus.BAD_REQUEST: dict,
    },
    summary="Create Character",
    tags=["Characters"],
)
def create_character(request, character_data: CharacterCreateSchema) -> Character:
    
    character_data = character_data.dict()
    
    for ability in Character.get_abilities():
        ability_coef = (character_data[ability] - 10) // 2
        
        for skill in Character.get_skills(ability):
            character_data[skill] = ability_coef
    
    character = Character.objects.create(**character_data, user_id=1) # Mocked user
    return HTTPStatus.CREATED, character
