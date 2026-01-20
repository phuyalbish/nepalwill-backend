from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.settings import DEFAULT_SUPERUSER_USERNAME, DEFAULT_SUPERUSER_PASSWORD
User = get_user_model()


class Command(BaseCommand):
    help = "Create a default superuser if it does not exist"

    def handle(self, *args, **options):
        username = DEFAULT_SUPERUSER_USERNAME
        password = DEFAULT_SUPERUSER_PASSWORD

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING("Default superuser already exists.")
            )
            return

        User.objects.create_superuser(
            username=username,
            password=password,
        )
        self.stdout.write(
            self.style.SUCCESS("Default superuser created successfully.")
        )