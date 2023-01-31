import boto3
from PIL import Image

def move_images(src_bucket, dest_bucket):
    s3 = boto3.client("s3")

    # List all the image files in the source bucket
    result = s3.list_objects_v2(Bucket=src_bucket)
    files = [content["Key"] for content in result.get("Contents", [])]

    # Create a log file to keep track of images with transparent pixels
    log = open("transparent_images.txt", "w")

    # Copy the images to the destination bucket
    for file in files:
        try:
            # Download the image file from the source bucket
            s3.download_file(src_bucket, file, file)

            # Open the image file with Pillow
            image = Image.open(file)

            # Check if the image has transparent pixels
            if "transparency" in image.info:
                log.write(f"{file} has transparent pixels.\n")
            else:
                # Copy the image to the destination bucket
                s3.upload_file(file, dest_bucket, file)

        except Exception as e:
            log.write(f"Error while processing {file}: {e}\n")

    log.close()

# Example usage:
src_bucket = "my-source-bucket"
dest_bucket = "my-destination-bucket"
move_images(src_bucket, dest_bucket)
