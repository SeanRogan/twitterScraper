import boto3
import os
import private
# Set the name of the bucket and the file to upload
bucket_name = private.S3_BUCKET

# get all csv files in pwd
csv_files = [f for f in os.listdir(os.getcwd()) if f.endswith(".csv")]
# Create an S3 client
s3 = boto3.client("s3")

for file in csv_files:
    # Read the CSV file into memory
    with open(file, "rb") as f:
        data = f.read()
# Upload the file to the S3 bucket
    try:
        s3.put_object(Bucket=bucket_name, Key=file, Body=data)
        print(f"Successfully uploaded {file} to {bucket_name}")

    except Exception as err:
        print(err)
