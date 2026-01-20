from django.db import migrations

def create_admin(apps, schema_editor):
    User = apps.get_model("auth", "User")

    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@margintradings.in",
            password="Admin@123"
        )

class Migration(migrations.Migration):

    dependencies = [
        ("tables", "0004_depositaccountdetails"),
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]
  
