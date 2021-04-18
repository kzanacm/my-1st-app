# Generated by Django 3.2 on 2021-04-17 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptg_nm_postagem', models.CharField(max_length=200)),
                ('ptg_ds_postagem', models.TextField()),
                ('ptg_ts_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('ptg_ts_alteracaco', models.DateTimeField(blank=True, null=True)),
                ('ptg_id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]