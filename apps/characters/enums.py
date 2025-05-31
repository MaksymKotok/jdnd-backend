from django.db.models import TextChoices

from enum import auto


class AbilityName(TextChoices):
    STRENGTH = auto()
    AGILITY = auto()
    ENDURANCE = auto()
    CHARISMA = auto()
    INTELLIGENCE = auto()
    WISDOM = auto()


class SkillName(TextChoices):
    ACROBATICS = auto()
    ALCHEMY = auto()
    ANIMAL_HANDLING = auto()
    ASTUTENESS = auto()
    ATHLETICS = auto()
    COOKING = auto()
    CRAFT = auto()
    DARK_PERCEPTION = auto()
    DECEPTION = auto()
    DESTRUCTIVE_MAGIC = auto()
    ENGINEERING = auto()
    ETIQUETTE = auto()
    EXPLOSIVES = auto()
    GAMBLING = auto()
    HISTORY = auto()
    HORSEBACK_RIDING = auto()
    INTIMIDATION = auto()
    LEADERSHIP = auto()
    LIGHT_MAGIC = auto()
    LINGUISTICS = auto()
    LOCKPICKING = auto()
    MEDICINE = auto()
    MUSIC = auto()
    NATURE = auto()
    OCCULTISM = auto()
    PERCEPTION = auto()
    PERSUASION = auto()
    POLITICS = auto()
    PSIONICS = auto()
    PUNCH_POWER = auto()
    RELIGION = auto()
    RESISTANCE = auto()
    SAILING = auto()
    SCIENCE = auto()
    SEDUCTION = auto()
    SELF_CONTROL = auto()
    SHOT_POWER = auto()
    SLEIGHT_OF_HAND = auto()
    SPEECH = auto()
    STEALTH = auto()
    SURVIVAL = auto()
    TACTICS = auto()
    THROWING = auto()
    TRADING = auto()
    TRAPS = auto()
    UNARMED = auto()
    VELOCITY = auto()
    WEAPON_HANDLING = auto()
    WITCHCRAFT = auto()


class SkillType(TextChoices):
    COGNITIVE = auto()
    PHYSICAL = auto()
    SOCIAL = auto()
    
    
SKILL_MAP = {
    SkillName.ACROBATICS: {
        "ability": AbilityName.AGILITY,
        "type": SkillType.PHYSICAL,
    },
    SkillName.ATHLETICS: {
        "ability": AbilityName.STRENGTH,
        "type": SkillType.PHYSICAL,
    },
    SkillName.WEAPON_HANDLING: {
        "ability": AbilityName.AGILITY,
        "type": SkillType.PHYSICAL,
    },
    SkillName.SLEIGHT_OF_HAND: {
        "ability": AbilityName.AGILITY,
        "type": SkillType.PHYSICAL,
    },
    SkillName.STEALTH: {
        "ability": AbilityName.AGILITY,
        "type": SkillType.PHYSICAL,
    },
    SkillName.SELF_CONTROL: {
        "ability": AbilityName.ENDURANCE,
        "type": SkillType.PHYSICAL,
    },
    SkillName.HORSEBACK_RIDING: {
        "ability": AbilityName.AGILITY,
        "type": SkillType.PHYSICAL,
    },
    SkillName.VELOCITY: {
        "ability": AbilityName.AGILITY,
        "type": SkillType.PHYSICAL,
    },
    SkillName.LOCKPICKING: {
        "ability": AbilityName.AGILITY,
        "type": SkillType.PHYSICAL,
    },
    SkillName.UNARMED: {
        "ability": AbilityName.AGILITY,
        "type": SkillType.PHYSICAL,
    },
    SkillName.RESISTANCE: {
        "ability": AbilityName.ENDURANCE,
        "type": SkillType.PHYSICAL,
    },
    SkillName.SHOT_POWER: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.PHYSICAL,
    },
    SkillName.PUNCH_POWER: {
        "ability": AbilityName.STRENGTH,
        "type": SkillType.PHYSICAL,
    },
    SkillName.THROWING: {
        "ability": AbilityName.STRENGTH,
        "type": SkillType.PHYSICAL,
    },
     SkillName.RELIGION: {
        "ability": AbilityName.INTELLIGENCE,
        "type": SkillType.PHYSICAL,
    },
    SkillName.EXPLOSIVES: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.PHYSICAL,
    },
    SkillName.ALCHEMY: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.COGNITIVE,
    },
    SkillName.COOKING: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.COGNITIVE,
    },
    SkillName.OCCULTISM: {
        "ability": AbilityName.INTELLIGENCE,
        "type": SkillType.COGNITIVE,
    },
    SkillName.TRAPS: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.COGNITIVE,
    },
    SkillName.POLITICS: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.COGNITIVE,
    },
    SkillName.LIGHT_MAGIC: {
        "ability": AbilityName.INTELLIGENCE,
        "type": SkillType.COGNITIVE,
    },
    SkillName.DESTRUCTIVE_MAGIC: {
        "ability": AbilityName.INTELLIGENCE,
        "type": SkillType.COGNITIVE,
    },
    SkillName.ANIMAL_HANDLING: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.COGNITIVE,
    },
    SkillName.HISTORY: {
        "ability": AbilityName.INTELLIGENCE,
        "type": SkillType.COGNITIVE,
    },
    SkillName.MEDICINE: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.COGNITIVE,
    },
    SkillName.ASTUTENESS: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.COGNITIVE,
    },
    SkillName.NATURE: {
        "ability": AbilityName.INTELLIGENCE,
        "type": SkillType.COGNITIVE,
    },
    SkillName.PERCEPTION: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.COGNITIVE,
    },
    SkillName.SURVIVAL: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.COGNITIVE,
    },
    SkillName.SAILING: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.COGNITIVE,
    },
    SkillName.ENGINEERING: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.COGNITIVE,
    },
    SkillName.TACTICS: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.COGNITIVE,
    },
    SkillName.SCIENCE: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.COGNITIVE,
    },
    SkillName.DARK_PERCEPTION: {
        "ability": AbilityName.INTELLIGENCE,
        "type": SkillType.COGNITIVE,
    },
    SkillName.PSIONICS: {
        "ability": AbilityName.INTELLIGENCE,
        "type": SkillType.COGNITIVE,
    },
    SkillName.WITCHCRAFT: {
        "ability": AbilityName.INTELLIGENCE,
        "type": SkillType.COGNITIVE,
    },
    SkillName.CRAFT: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.COGNITIVE,
    },
    SkillName.DECEPTION: {
        "ability": AbilityName.CHARISMA,
        "type": SkillType.SOCIAL,
    },
    SkillName.INTIMIDATION: {
        "ability": AbilityName.CHARISMA,
        "type": SkillType.SOCIAL,
    },
    SkillName.PERSUASION: {
        "ability": AbilityName.CHARISMA,
        "type": SkillType.SOCIAL,
    },
    SkillName.SPEECH: {
        "ability": AbilityName.CHARISMA,
        "type": SkillType.SOCIAL,
    },
    SkillName.LEADERSHIP: {
        "ability": AbilityName.CHARISMA,
        "type": SkillType.SOCIAL,
    },
    SkillName.SEDUCTION: {
        "ability": AbilityName.CHARISMA,
        "type": SkillType.SOCIAL,
    },
    SkillName.TRADING: {
        "ability": AbilityName.CHARISMA,
        "type": SkillType.SOCIAL,
    },
    SkillName.ETIQUETTE: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.SOCIAL,
    },
    SkillName.LINGUISTICS: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.SOCIAL,
    },
    SkillName.MUSIC: {
        "ability": AbilityName.CHARISMA,
        "type": SkillType.SOCIAL,
    },
    SkillName.GAMBLING: {
        "ability": AbilityName.WISDOM,
        "type": SkillType.SOCIAL,
    },
}
