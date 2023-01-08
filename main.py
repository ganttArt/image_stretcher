from PIL import Image
from directional_stretch import downward_stretch, upward_stretch, right_stretch

# Set stretching variables:
IMAGE = "test.jpg"
DIRECTION = 'right' # left, right, up, down
STARTING_POINT = 100 # Range: 0 -> height/width of image
STRETCH_STRENGTH = 13 # 1 -> 13


def main():
    with Image.open(IMAGE) as image:
        try:
            if image.format != 'JPEG':
                image = image.convert('RGB')
        except Exception:
            print('File type not compatible')
            return
        
        stretched_image = right_stretch(image, STRETCH_STRENGTH, STARTING_POINT)
        stretched_image.show()


if __name__ == '__main__':
    main()
