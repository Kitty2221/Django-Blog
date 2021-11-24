from django.apps import AppConfig


# This allows us to use the AppConfig feature, our users do not need to update the INSTALLED_APPS settings.
# BlogConfig will be used when INSTALLED_APPS contains only 'blog'.
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
