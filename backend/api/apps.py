from django.apps import AppConfig

class ApiConfig(AppConfig):
    name = "api"

    def ready(self):
        from django.contrib.auth.models import User
        if not User.objects.filter(username="user_qRPY").exists():
            User.objects.create_user(
                username="hoang",
                password="123456"
            )