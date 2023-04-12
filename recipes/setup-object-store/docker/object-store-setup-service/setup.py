import os
import boto3


def create_bucket(s3, bucket_name: str):
    if s3.Bucket(bucket_name) in s3.buckets.all():
        print("bucket already exists")
        return s3.Bucket(bucket)
    else:
        s3.create_bucket(Bucket=bucket)
        print("bucket created")
        return s3.Bucket(bucket)


if __name__ == "__main__":
    bucket = os.getenv("BUCKET")
    s3 = boto3.resource("s3", endpoint_url=os.getenv("OBJECT_STORE_ENDPOINT"))
    bucket = create_bucket(s3, os.getenv("BUCKET"))

    bucket.upload_file(
        Filename="/data/sample.txt",
        Key="prefix/sample.txt",
    )
    print("object loaded")
