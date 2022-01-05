from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

class APP_NAMEConfig(AppConfig):
        name = 'APP_NAME'
        icon = 'ICON_CLASS'  # for example: icon = 'fa fa-users'