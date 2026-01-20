from django.apps import AppConfig
from django.contrib.auth import get_user_model
import os

class TablesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tables'

    def ready(self):
        if not os.environ.get("RENDER"):
            return

        User = get_user_model()

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                password=os.environ.get("ADMIN_PASSWORD", "admin123"),
                email="admin@margintradings.in",
            )


