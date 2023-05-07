from minio import Minio
from minio.error import S3Error

def upload_to_minio(file_name):
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )

    # Make 'asiatrip' bucket if not exist.
    found = client.bucket_exists("asiatrip")
    if not found:
        client.make_bucket("asiatrip")
    else:
        print("Bucket 'asiatrip' already exists")

    # Upload file to 'asiatrip' bucket with same name as file
    client.fput_object(
        "asiatrip", file_name, file_name,
    )
    print(f"{file_name} successfully uploaded to bucket 'asiatrip'.")

if __name__ == "__main__":
    try:
        upload_to_minio("my_file.txt")
    except S3Error as exc:
        print("An error occurred.", exc)
