from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ability',
            options={'verbose_name': 'Ability', 'verbose_name_plural': 'Abilities'},
        ),
        migrations.AddConstraint(
            model_name='character',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name', 'user'), name='unique_user_character'),
        ),
    ]
