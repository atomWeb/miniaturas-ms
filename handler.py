import boto3
import os
from PIL import Image
from io import BytesIO

SIZEH = int(os.environ['TIMG_HSIZE']) #: "166"
SIZEW = int(os.environ['TIMG_WSIZE']) #: "120"
REGION = os.environ["REGION"]
s3 = boto3.client("s3", region_name=REGION)


def vgame_timg_generator(event, context):
    url = ""
    # print(event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    #print(key)
    #print(bucket)

    #
    if (not key.endswith("_timg.png")):
        image = get_s3_image(bucket, key)
        thumbnail = image_to_thumbnail(image)
        thumbnail_key = new_filename("timg/" + key)
        url = upload_to_s3(bucket, thumbnail_key, thumbnail)

    return url

def get_s3_image(bucket, key):
    response = s3.get_object(Bucket=bucket, Key=key)
    file_byte_string = response['Body'].read()
    img = Image.open(BytesIO(file_byte_string))
    return img


def image_to_thumbnail(image):
    size = SIZEW, SIZEH
    memory_file = BytesIO()
    image.thumbnail(size, Image.ANTIALIAS)    
    image.save(memory_file, format=image.format)
    memory_file.seek(0)
    return memory_file


def new_filename(key):
    key_split = key.rsplit('.', 1)
    return key_split[0] + "_timg.png"


def upload_to_s3(bucket, key, image):

    response = s3.put_object(
        ACL='public-read',
        Body=image,
        Bucket=bucket,
        ContentType='image/png',
        Key=key
    )
    print(response)

    url = f"End point: {s3.meta.endpoint_url}, buket: {bucket}, Key: {key}"    
    return url
