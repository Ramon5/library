import csv
import logging

from django.core.management.base import BaseCommand

from author.models import Author

logger = logging.getLogger(__name__)

"""
    This command will be import all data of csv file to Author model
"""


class Command(BaseCommand):

    """
        Add path to csv
    """

    def add_arguments(self, parser):
        parser.add_argument("csvpath", type=str)

    def handle(self, *args, **options):
        try:
            authors_list = []
            with open(options["csvpath"]) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    authors_list.append(Author(name=row["name"]))

            break_size = len(authors_list) / 2
            Author.objects.bulk_create(authors_list, ignore_conflicts=True, batch_size=break_size)
            print("All data have been imported to database")
        except Exception as e:
            logger.error(e)

    def _calculate_better_size(self, sample):
        pass
