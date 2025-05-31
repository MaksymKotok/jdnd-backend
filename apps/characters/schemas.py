from ninja.schema import Schema, Field

from apps.characters.models import Character


class CharacterListSchema(Schema):
    id: int
    full_name: str
    user: str | None = Field(None, alias="user.email")
    level: int
    age: int | None = None
    alignment: str = Field(..., alias="get_alignment_display")


class CharacterAbilitySchema(Schema):
    name: str = Field(..., alias="get_name_display")
    value: int
    
    
class CharacterSkillSchema(Schema):
    name: str = Field(..., alias="get_name_display")
    value: int

    
class CharacterDetailSchema(Schema):
    id: int
    full_name: str
    user: str | None = Field(None, alias="user.email")
    level: int
    age: int | None = None
    alignment: str = Field(None, alias="get_alignment_display")
    role: str | None = Field(None, alias="role.name")
    abilities: list[CharacterAbilitySchema] = Field(..., alias="abilities")
    skills: list[CharacterSkillSchema] = Field(..., alias="skills")

    
class CharacterCreateSchema(Schema):
    first_name: str
    last_name: str
    age: int | None = None
    alignment: str
    role: str | None = None
    strength: int
    agility: int
    endurance: int
    charisma: int
    intelligence: int
    wisdom: int
