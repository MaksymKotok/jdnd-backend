from django.db import models
from django.utils.translation import gettext_lazy as _

        
class AlignmentChoices(models.TextChoices):
    LAWFUL_GOOD = "lawfull_good", _("Lawfull Good")
    NEUTRAL_GOOD = "neutral_good", _("Neutral Good")
    CHAOTIC_GOOD = "chaotic_good", _("Chaotic Good")
    LAWFUL_NEUTRAL = "lawfull_neutral", _("Lawfull Neutral")
    TRUE_NEUTRAL = "true_neutral", _("True Neutral")
    CHAOTIC_NEUTRAL = "chaotic_neutral", _("Chaotic Neutral")
    LAWFUL_EVIL = "lawfull_evil", _("Lawfull Evil")
    NEUTRAL_EVIL = "neutral_evil", _("Neutral Evil")
    CHAOTIC_EVIL = "chaotic_evil", _("Chaotic Evil")
