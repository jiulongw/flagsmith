# Generated by Django 4.2.16 on 2024-11-04 17:09
from django.apps.registry import Apps
from django.db import migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.models import F
from django.db.models.functions import Left


def populate_new_first_name_field(apps: Apps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    FFAdminUser = apps.get_model("users", "FFAdminUser")

    FFAdminUser.objects.update(first_name_v2=F("first_name"))


def populate_old_first_name_field(apps: Apps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    FFAdminUser = apps.get_model("users", "FFAdminUser")

    FFAdminUser.objects.update(first_name=Left("first_name_v2", 30))


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0038_create_hubspot_tracker"),
    ]

    operations = [
        migrations.AddField(
            model_name="ffadminuser",
            name="first_name_v2",
            field=models.CharField(max_length=150, default=""),
        ),
        migrations.RunPython(populate_new_first_name_field, reverse_code=populate_old_first_name_field),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RenameField(
                    model_name="ffadminuser",
                    old_name="first_name",
                    new_name="_first_name_old",
                ),
                migrations.RenameField(
                    model_name="ffadminuser",
                    old_name="first_name_v2",
                    new_name="first_name",
                ),
                migrations.AlterField(
                    model_name="ffadminuser",
                    name="_first_name_old",
                    field=models.CharField(
                        db_column="first_name", max_length=30, verbose_name="first name"
                    ),
                ),
                migrations.AlterField(
                    model_name="ffadminuser",
                    name="first_name",
                    field=models.CharField(
                        db_column="first_name_v2", max_length=150, verbose_name="first name"
                    ),
                ),
            ]
        )
    ]
