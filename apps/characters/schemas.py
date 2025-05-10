from ninja.schema import Schema, Field

from apps.characters.models import Character


class CharacterListSchema(Schema):
    id: int
    full_name: str
    user: str | None = Field(None, alias="user.email")
    level: int
    age: int | None = None
    alignment: str = Field(..., alias="get_alignment_display")
    
    
class CharacterDetailSchema(Schema):
    id: int
    full_name: str
    user: str | None = Field(None, alias="user.email")
    level: int
    age: int | None = None
    alignment: str = Field(None, alias="get_alignment_display")
    role: str | None = Field(None, alias="role.name")
    
    abilities: list[dict[str, str | int]]
    skills: dict[str, list[dict[str, str | int]]]
    
    @staticmethod
    def resolve_abilities(obj) -> dict[str, int]:
        return [
            { 
                "name": key,
                "value": getattr(obj, key)
            }  
            for key in Character.get_abilities()
        ]
        
    @staticmethod
    def resolve_skills(obj) -> dict[str, int]:
        return {
            type: [
                { 
                    "name": key,
                    "value": getattr(obj, key)
                } 
                for key in Character.get_skills_by_type(type)
            ]
            for type in ["physical", "cognitive", "social"]
        }
    
    
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
