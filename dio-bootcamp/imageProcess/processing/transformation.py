import cv2

def resize_image(image, width, height):
    """Redimensiona uma imagem para as dimensões especificadas."""
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
