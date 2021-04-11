from django.core.management.base import BaseCommand, CommandError
import csv
from persons.models import Person
import argparse
import os

class ImportPersons:
    def __init__(self, options):
        self.file_data = options['file']

    def loadcsv(self):
        model_fields = [f.name for f in Person._meta.fields]
        fields_name = []
        with open (self.file_data, 'r') as csvFile:
            reader = csv.reader (csvFile, delimiter=';', quotechar="\"")
            first_line = next(reader)
            fields_name = next(reader)
            for i, _ in enumerate(fields_name):
                fields_name[i] = fields_name[i].lower ()
                fields_name[i] = fields_name[i].replace (' ', '_')
                fields_name[i] = fields_name[i].replace ('-', '')
                if not fields_name[i] in model_fields:
                    raise CommandError ("%s field doesn't exists in %s Model" %(fields_name[i], Person))

            for row in reader:
                print(row)
                try:
                    obj = Person()
                    for i, field in enumerate(row):
                        setattr (obj, fields_name[i], field)
                    obj.save ()
                except Exception as e:
                    raise CommandError(e)


class Command(BaseCommand):
    help = 'python manage.py import_persons_from_csv employees.csv'

    def add_arguments(self, parser):
        parser.add_argument(
            'file',
            help='File path of CSV containing persons list'
        )

    def handle(self, *args, **options):
        importer = ImportPersons(options)
        importer.loadcsv()
