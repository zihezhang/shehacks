import os, io
from numpy import random
from google.cloud import vision
from formatingFunc import draw_borders, Image
import pandas as pd


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'VisionApiProject.json'
client = vision.ImageAnnotatorClient()

file_name = 'dog.jpg'
image_path = os.path.join(file_name)
image_source = None 

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)
response = client.object_localization(image=image)
localized_object_annotations = response.localized_object_annotations

pillow_image = Image.open(image_path)
df = pd.DataFrame(columns=['name', 'score'])
for obj in localized_object_annotations:
    df = df.append(
        dict(
            name=obj.name,
            score=obj.score
        ),
        ignore_index=True)
    
    r, g, b = random.randint(150, 255), random.randint(
        150, 255), random.randint(150, 255)

    draw_borders(pillow_image, obj.bounding_poly, (r, g, b),
                 pillow_image.size, obj.name, obj.score)

print(df)
pillow_image.show()