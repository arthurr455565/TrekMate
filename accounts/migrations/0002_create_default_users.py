from django.db import migrations


def create_default_users(apps, schema_editor):
    User = apps.get_model("accounts", "User")

    users = [
        {"username": "trekker", "password": "trekker123", "role": "trekker", "is_staff": False, "is_superuser": False},
        {"username": "guide", "password": "guide123", "role": "guide", "is_staff": False, "is_superuser": False},
        {"username": "admin", "password": "admin123", "role": "admin", "is_staff": True, "is_superuser": True},
    ]

    for u in users:
        if not User.objects.filter(username=u["username"]).exists():
            User.objects.create_user(
                username=u["username"],
                password=u["password"],
                role=u["role"],
                is_staff=u["is_staff"],
                is_superuser=u["is_superuser"],
            )


def reverse_func(apps, schema_editor):
    User = apps.get_model("accounts", "User")
    for username in ["trekker", "guide", "admin"]:
        User.objects.filter(username=username).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_default_users, reverse_func),
    ]
