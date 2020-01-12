import io
from PIL import Image, ImageDraw, Image, ImageFont


def draw_borders(pillow_image, bounding, color, image_size, caption='', confidence_score=0):

    width, height = image_size
    draw = ImageDraw.Draw(pillow_image)
    draw.polygon([
        bounding.normalized_vertices[0].x *
        width, bounding.normalized_vertices[0].y * height,
        bounding.normailized_vertices[1].x*
        width, bounding.normailized_vertices[1].y * height,
        bounding.normailized_vertices[2].x*
        width, bounding.normailized_vertices[2].y * height,
        bounding.normailized_vertices[3].x*
        width, bounding.normailized_vertices[3].y * height], fill=None, outline=color)
    
    font_size = width * height

    font = ImageFont.truetype('arial.ttf', 16)

    draw.text((bounding.normailized_vertices[0].x * width, bounding.normailized_vertices[0].y * height), font=font, text=caption, fill=color)
    draw.text((bounding.normailized_vertices[0].x * width, bounding.normailized_vertices[0].y * height + 20), font=font, text='confidence score: {0:.2f}%'.format(confidence_score), fill=color)

    return pillow_image



