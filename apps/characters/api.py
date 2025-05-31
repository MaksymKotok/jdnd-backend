from http import HTTPStatus

from django.db import transaction 
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from ninja import Router

from apps.characters.schemas import (
    CharacterListSchema,
    CharacterDetailSchema,
    CharacterCreateSchema,
)

from apps.characters.models import Ability, Character, Skill
from apps.characters.enums import SKILL_MAP, AbilityName

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
def create_character(request, payload: CharacterCreateSchema) -> Character:
    
    with transaction.atomic():
        character = Character.objects.create(
            first_name=payload.first_name,
            last_name=payload.last_name,
            age=payload.age,
            alignment=payload.alignment,
            role=payload.role,
            user_id=1, # Mocked user
        )
        
        abilities = []
        abilities_coefs = {}
        for ability in AbilityName.values:
            name = ability.lower()
            value = getattr(payload, name)
            abilities_coefs[ability] = (value - 10) // 2
            abilities.append(Ability(character=character, name=ability, value=value))
        
        Ability.objects.bulk_create(abilities)
        
        skills = []
        for name, skill in SKILL_MAP.items():
            skills.append(
                Skill(
                    character=character,
                    name=name,
                    type=skill["type"],
                    value=abilities_coefs[skill["ability"]],
                )
            )
            
        Skill.objects.bulk_create(skills)
    
    return HTTPStatus.CREATED, character
