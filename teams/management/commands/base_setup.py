from django.core.management.base import BaseCommand
from fixtures.set_data import set_data


class Command(BaseCommand):
    help = 'Creates base data'

    def handle(self, *args, **options):
        set_data()

        self.stdout.write(self.style.SUCCESS('Successfully created data'))

        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()
        #
        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
