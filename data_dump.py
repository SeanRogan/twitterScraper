from datafreeze import freeze
import dataset
import settings
# connects to database and dumps table to a csv file
# todo create a way to dump these files to an s3 bucket?
db = dataset.connect(settings.CONNECTION_STRING)

result = db[settings.TABLE_NAME].all()
freeze(result, format='csv', filename=settings.CSV_NAME)
