from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help = 'Generate random users'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='The number of users to be created')

    def handle(self, *args, **options):
        number = options.get('number')
        if number < 1 or number > 10:
            self.stdout.write(self.style.ERROR('Can not create users'))
            raise ValueError('Number of users should be between 1 and 10')

        users = []
        fake = Faker()
        for i in range(number):
            new_user = fake.simple_profile()
            user = User(username=new_user.get('username'), email=new_user.get('mail'))
            user.set_password(make_password(fake.password()))
            users.append(user)

        User.objects.bulk_create(users)
        return self.stdout.write(self.style.SUCCESS('SUCCESS'))
