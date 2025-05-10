from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.characters.choices import AlignmentChoices


class StatsField(models.PositiveSmallIntegerField):
    
    def __init__(self, *args, **kwargs):
        kwargs["validators"] = [MinValueValidator(1), MaxValueValidator(20)]
        super().__init__(*args, **kwargs)
        
        
class SkillField(models.SmallIntegerField):
    
    def __init__(self, *args, **kwargs):
        kwargs["validators"] = [MinValueValidator(-20), MaxValueValidator(20)]
        super().__init__(*args, **kwargs)
        
        
class CharacterRole(models.Model):
    
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = _("Character Role")
        verbose_name_plural = _("Character Roles")


class Character(models.Model):
    
    def avatar_path(instance, filename):
        return f"users/{instance.user}/characters/{filename}"
    
    user = models.ForeignKey(
        "users.User",
        related_name="characters",
        on_delete=models.PROTECT,
    )
    avatar = models.ImageField(
        upload_to=avatar_path,
        null=True,
        blank=True,
    )
    
    first_name = models.CharField(_("First Name"), max_length=150)
    last_name = models.CharField(_("Last Name"), max_length=150)
    
    level = models.PositiveSmallIntegerField(default=1)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    
    role = models.ForeignKey(
        CharacterRole,
        related_name="characters",
        verbose_name=_("Character Role"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    
    alignment = models.CharField(
        max_length=15,
        choices=AlignmentChoices.choices,
        default=AlignmentChoices.TRUE_NEUTRAL,
    )
    
    # organization = 
    # organization_role = 
    
    ########## ABILITIES ##########
    
    strength = StatsField()
    agility = StatsField()
    endurance = StatsField()
    charisma = StatsField()
    intelligence = StatsField()
    wisdom = StatsField()
    
    ########## SKILLS ##########
    
    ##### PHYSICAL #####
    
    acrobatics = SkillField()
    athletics = SkillField()
    weapon_handling = SkillField()
    sleight_of_hand = SkillField()
    stealth = SkillField()
    self_control = SkillField()
    horseback_riding = SkillField()
    velocity = SkillField()
    lockpicking = SkillField()
    unarmed = SkillField()
    resistance = SkillField()
    shot_power = SkillField()
    punch_power = SkillField()
    throwing = SkillField()
    religion = SkillField()
    explosives = SkillField()
    
    ##### COGNITIVE #####
    
    alchemy = SkillField()
    cooking = SkillField()
    occultism = SkillField()
    traps = SkillField()
    politics = SkillField()
    light_magic = SkillField()
    destructive_magic = SkillField()
    animal_handling = SkillField() #
    history = SkillField()
    medicine = SkillField()
    astuteness = SkillField()
    nature = SkillField()
    perception = SkillField()
    survival = SkillField()#
    sailing = SkillField()
    engineering = SkillField()
    tactics = SkillField()
    science = SkillField()
    dark_perception = SkillField()
    psionics = SkillField()
    witchcraft = SkillField()
    craft = SkillField()
    
    ##### SOCIAL #####
    
    deception = SkillField()
    intimidation = SkillField()
    persuasion = SkillField()
    speech = SkillField()
    leadership = SkillField()
    seduction = SkillField()
    trading = SkillField()
    etiquette = SkillField()
    linguistics = SkillField()
    music = SkillField()
    gambling = SkillField()
    
    
    class Meta:
        verbose_name = _("Character")
        verbose_name_plural = _("Characters")
        
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def get_abilities(cls) -> list[str]:
        return ["strength", "agility", "endurance", "charisma", "intelligence", "wisdom",]
    
    @classmethod
    def get_skills(cls, ability: str) -> list[str]:
        match ability:
            case "strength":
                return [
                    "athletics", "punch_power", "throwing",
                ]
            case "agility":
                return [
                    "acrobatics", "weapon_handling", "sleight_of_hand", "stealth",
                    "horseback_riding", "velocity", "lockpicking", "unarmed",
                ]
            case "endurance":
                return [
                    "self_control", "resistance",
                ]
            case "charisma":
                return [
                    "deception", "intimidation", "persuasion", "speech",
                    "leadership", "seduction", "trading", "music",
                ]
            case "intelligence":
                return [
                    "religion", "occultism", "light_magic", "destructive_magic", "history",
                    "nature", "dark_perception", "psionics", "witchcraft",
                    ]
            case "wisdom":
                return [
                    "shot_power", "explosives", "alchemy", "cooking", "traps", 
                    "politics", "animal_handling", "medicine", "astuteness", 
                    "perception", "survival", "sailing", "engineering", 
                    "tactics", "science", "craft", "etiquette", "linguistics", "gambling",
                ]
            case _:
                return []
            
    @classmethod
    def get_skills_by_type(cls, type: str) -> list[str]:
        match type:
            case "physical":
                return [
                    "acrobatics", "athletics", "weapon_handling", "sleight_of_hand", 
                    "stealth", "self_control", "horseback_riding", "velocity", 
                    "lockpicking", "unarmed", "resistance", "shot_power", 
                    "punch_power", "throwing", "religion", "explosives",
                ]
            case "cognitive":
                return [
                    "alchemy", "cooking", "occultism", "traps", "politics", 
                    "light_magic", "destructive_magic", "animal_handling", 
                    "history", "medicine", "astuteness", "nature", "perception", 
                    "survival", "sailing", "engineering", "tactics", "science", 
                    "dark_perception", "psionics", "witchcraft", "craft",
                ]
            case "social":
                return [
                    "deception", "intimidation", "persuasion", "speech", 
                    "leadership", "seduction", "trading", "etiquette", 
                    "linguistics", "music", "gambling",
                ]
            case _:
                return []
