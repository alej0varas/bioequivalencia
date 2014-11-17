from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist

import bioeq.apps.medicament.settings as settings
import bioeq.libs.scrapper as scrapper
import sys, os, tempfile, mechanize

from bioeq.apps.medicament.models import * 

debug = False

if debug:
	from tabulate import tabulate

class Command(BaseCommand):
	help = 'download and parse source data'

	def handle(self, *args, **options):
		self.stdout.write('Downloading file from %s' % settings.source_data_url)
		temp_file = tempfile.NamedTemporaryFile(suffix='.pdf', prefix='bioeq_source_data-', delete=False)

		try:

			# Download source
			try: 
				scrapper.download(settings.source_data_url, temp_file)
				temp_file.close()
			except (mechanize.HTTPError,mechanize.URLError) as err:
				self.stderr.write(
					'Download error: %s %s'
					% (err.getcode(), err.reason)
				)
				
				sys.exit(1)

			self.stdout.write('File download as "%s"' % temp_file.name)

			# Parse source
			self.stdout.write('Processing file...')
			data = scrapper.medicament.parse(temp_file.name)		
			self.stdout.write('Processing done')

		finally:
			self.stdout.write('Deleting temporary file "%s"' % temp_file.name)
			temp_file.close()
			os.remove(temp_file.name)

		# Import data
		if debug:
			print tabulate(data)

		# Deleting headers
		del data[0]

		i = len(data)

		while i:
			row = data.pop(0)

			# Treatment
			if row[1]:
				treatment = orm_obj(Treatment, row[1].strip())
				self.debugOutput('Treatment', vars(treatment))

			# Medicinal Ingredient
			if row[2]:
				medicinal_ingredient = orm_obj(MedicinalIngredient, row[2].lower())
				# self.debugOutput('MedicinalIngredient', medicinal_ingredient)

			# Non bioequivalent holder
			if row[4]:
				holder_non_bioeq = orm_obj(Holder, row[4])
				self.debugOutput('Holder', vars(holder_non_bioeq))


			# Non-bioequivalent product
			if row[3]:
				prod_non_bioeq = orm_obj(Product, row[3], False)

				if prod_non_bioeq.pk is None:
					prod_non_bioeq.bioequivalent 		= False
					prod_non_bioeq.holder 				= holder_non_bioeq
					prod_non_bioeq.medicinal_ingredient = medicinal_ingredient
					prod_non_bioeq.save()

				self.debugOutput('Product', vars(prod_non_bioeq))


			# Bioequivalent holder
			if row[7]:
				holder_bioeq = orm_obj(Holder, row[7])

				self.debugOutput('Holder', vars(holder_bioeq))

			# Bioequivalent product
			if row[5]:
				prod_bioeq = orm_obj(Product, row[5], False)

				if prod_bioeq.pk is None:
					prod_bioeq.bioequivalent 		= True
					prod_bioeq.holder 				= holder_bioeq
					prod_bioeq.medicinal_ingredient = medicinal_ingredient
					prod_bioeq.registry 			= row[6]
					prod_bioeq.save()

				self.debugOutput('Product', vars(prod_bioeq));


			i -= 1

		self.stdout.write('')

	def debugOutput(self, *args):	
		if debug:
			self.stdout.write(' '.join(str(arg) for arg in args))


def orm_obj(type, name, auto_create=True):
	try:
		obj = type.objects.get(name=name)
	except ObjectDoesNotExist:
		obj = type(name=name)

		if(auto_create):
			obj.save()

	return obj