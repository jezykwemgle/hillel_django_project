from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Generate random users'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='The number of users to be created')

    def handle(self, *args, **options):
        number = options.get('number')
        if number < 1 or number > 10:
            raise ValueError('Number of users should be between 1 and 10')

        users = []
        fake = Faker()
        for i in range(number):
            new_user = fake.simple_profile()
            username = new_user.get('username')
            email = new_user.get('mail')
            password = make_password(fake.password())
            user = User(username=username, email=email)
            user.set_password(password)
            users.append(user)

        User.objects.bulk_create(users)
        return self.stdout.write(self.style.ERROR('SUCCESS'))

