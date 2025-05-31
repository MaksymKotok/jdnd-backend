from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.characters.choices import AlignmentChoices
from apps.characters.enums import (
    AbilityName,
    SkillType,
    SkillName,
)


class Ability(models.Model):
    
    name = models.CharField(max_length=30, choices=AbilityName.choices)
    value = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    character = models.ForeignKey(
        "Character",
        related_name="abilities",
        on_delete=models.CASCADE,
    )
    
    class Meta:
        verbose_name = _("Ability")
        verbose_name_plural = _("Abilities")
        
        constraints = [
            models.UniqueConstraint(fields=["name", "character"], name="unique_character_ability")
        ]
        
    def __str__(self) -> str:
        return self.name
    
    
class Skill(models.Model):
    
    name = models.CharField(max_length=30, choices=SkillName.choices)
    type = models.CharField(max_length=30, choices=SkillType.choices)
    value = models.SmallIntegerField(validators=[MinValueValidator(-20), MaxValueValidator(20)])
    character = models.ForeignKey(
        "Character",
        related_name="skills",
        on_delete=models.CASCADE,
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "character"], name="unique_character_skill")
        ]
        
    def __str__(self) -> str:
        return self.name


class CharacterRole(models.Model):

    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = _("Character Role")
        verbose_name_plural = _("Character Roles")
    
    def __str__(self) -> str:
        return self.display_name


class Character(models.Model):
    
    def avatar_path(instance, filename):
        return f"users/{instance.user.id}/characters/{instance.id}/{filename}"
    
    user = models.ForeignKey(
        "users.User",
        related_name="characters",
        on_delete=models.CASCADE,
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
    
    class Meta:
        verbose_name = _("Character")
        verbose_name_plural = _("Characters")
        
        constraints = [
            models.UniqueConstraint(fields=["first_name", "last_name", "user"], name="unique_user_character")
        ]
        
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    @property
    def user_full_name(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
    
    def __str__(self) -> str:
        return self.full_name
