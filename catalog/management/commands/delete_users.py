from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Delete users by ID'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, nargs='*', help='')

    def handle(self, *args, **options):
        users_id = options.get('user_id')
        User = get_user_model()

        if User.objects.filter(pk__in=users_id, is_superuser=True).exists():
            return self.stdout.write(self.style.ERROR('Cannot delete superuser'))

        user_list = User.objects.filter(pk__in=users_id).exclude(is_superuser=True)
        user_list.delete()
        return self.stdout.write(self.style.ERROR('SUCCESS'))




