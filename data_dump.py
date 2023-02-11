from datafreeze import freeze
import dataset
from sqlalchemy.exc import ProgrammingError
from sys import argv

# This script connects to the database and dumps the table passed via argument to a csv file
# it requires a table name and valid db connection string to be passed to it upon running the script
# its meant to be run on a chron job by a shell script on whatever server is running the data scraper.
# a command to run this script would look like the line below

# python data_dump.py postgresql://seanrogan:password@scraperstorage.cf2k04dkofim.us-east-1.rds.amazonaws.com:5432/scrappeddata financial_assets stock-related-tweets.csv


try:
    db = dataset.connect(argv[1])                   # connect to the database with the connection string passed via the first argument
    result = db[argv[2]].all()                      # pull all info from the table passed by the second argument
    freeze(result, format='csv',                    # freeze saves the info from the table into a CSV file, the name of the file
           filename=argv[3])                        # is passed as the third argument
except ProgrammingError as err:
    print("an error occurred with the database" + err)

