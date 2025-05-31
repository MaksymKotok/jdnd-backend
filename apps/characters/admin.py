from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from apps.characters.enums import SkillType
from apps.characters.models import (
    Character,
    Ability,
    Skill,
)


class AbilityInline(admin.TabularInline):
    model = Ability
    extra = 0
    readonly_fields = ("name",)
    fields = ("name", "value",)
    
    def has_delete_permission(self, request, obj=None):
        return False


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0
    readonly_fields = ("name",)
    fields = ("name", "value")
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    
class PhysicalSkillInline(SkillInline):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).filter(type=SkillType.PHYSICAL)
    
    verbose_name_plural = _("Physical Skills")


class CognitiveSkillInline(SkillInline):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).filter(type=SkillType.COGNITIVE)
    
    verbose_name_plural = _("Cognitive Skills")
    
    
class SocialSkillInline(SkillInline):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).filter(type=SkillType.SOCIAL)
    
    verbose_name_plural = _("Social Skills")


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    inlines = (
        AbilityInline,
        PhysicalSkillInline,
        CognitiveSkillInline,
        SocialSkillInline,
    )
    list_display = ("full_name", "user_full_name")
