from PIL import Image
from image_stretching.image_stretch import stretch_image

# Set stretching variables:
IMAGE = "test.jpg"
DIRECTION = 'down' # left, right, up, down
STARTING_POINT = 100 # Range: 0 -> height/width of image
STRETCH_STRENGTH = 10 # 1 -> 13


def main():
    with Image.open(IMAGE) as image:
        try:
            if image.format != 'JPEG':
                image = image.convert('RGB')
        except Exception:
            print('File type not compatible')
            return
        
        stretched_image = stretch_image(image, STRETCH_STRENGTH, STARTING_POINT, DIRECTION)
        stretched_image.show()


if __name__ == '__main__':
    main()
