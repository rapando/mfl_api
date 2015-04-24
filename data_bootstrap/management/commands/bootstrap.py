import os
import glob

from django.conf import settings

from django.core.management import BaseCommand

from ...bootstrap import process_json_file


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        counties = os.path.join(settings.BASE_DIR, 'data/data/counties.json')
        constituencies = os.path.join(
            settings.BASE_DIR, 'data/data/constituencies.json')
        #  wards = os.path.join(settings.BASE_DIR, 'data/data/wards.json')
        owners = os.path.join(
            settings.BASE_DIR, 'data/data/facility_owners.json')

        owners = os.path.join(
            settings.BASE_DIR, 'data/data/service_categories.json')
        job_titles = os.path.join(
            settings.BASE_DIR, 'data/data/job_titles.json')
        args = [
            counties, constituencies, owners, job_titles
        ]

        for suggestion in args:
            # if it's just a simple json file
            if os.path.exists(suggestion) and os.path.isfile(suggestion):
                process_json_file(suggestion)
            else:
                # check if it's a glob
                for filename in glob.glob(suggestion):
                    process_json_file(filename)

        self.stdout.write("Done loading")
