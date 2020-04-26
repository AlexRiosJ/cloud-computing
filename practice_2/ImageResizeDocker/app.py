from PIL import Image
from resizeimage import resizeimage
import sys
import boto3

s3 = boto3.client('s3')
s3.download_file('resize-image-bucket-p2', sys.argv[1], 'temp.' + sys.argv[1].split('.')[1])

with open('temp.' + sys.argv[1].split('.')[1],'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image,[150,150])
        cover.save(sys.argv[2],image.format)
        s3.upload_file(sys.argv[2], 'resize-image-bucket-p2', sys.argv[2])


