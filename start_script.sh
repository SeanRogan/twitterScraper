#!/bin/bash

# Install packages from requirements.txt
pip install -r requirements.txt

# Run scraper.py
python scraper.py

# Cron job to drop last csv file
# into S3 bucket and run data_dump.py
# to create todays csv file.
# runs every day at midnight
echo "0 0 * * * python store_files.py" | crontab -
echo "0 0 * * * python data_dump.py" | crontab -


