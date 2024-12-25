import cv2

def read_image(path):
    """Lê uma imagem do disco."""
    image = cv2.imread(path, cv2.IMREAD_COLOR)
    if image is None:
        print(f"Erro ao carregar a imagem: {path}")
    return image
