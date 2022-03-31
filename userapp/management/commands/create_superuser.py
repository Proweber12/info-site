from django.core.management.base import BaseCommand

from userapp.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()

        User.objects.create_superuser(
            username="admin", first_name="Руслан", last_name="Цурук", email="admin@gmail.com", password="admin"
        )
