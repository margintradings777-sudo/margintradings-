from django.apps import AppConfig

class TablesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tables'

    def ready(self):
        """
        Initialization logic should avoid database queries.
        Superuser creation is now handled by create_superuser.py 
        during the build process.
        """
        pass


