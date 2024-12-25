import matplotlib.pyplot as plt

def plot_image(image, title="Imagem"):
    """Exibe uma imagem única."""
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")
    plt.show()

def plot_result(image1, image2, result_image):
    """Exibe as imagens de entrada e o resultado lado a lado."""
    plt.figure(figsize=(12, 6))
    titles = ["Imagem 1", "Imagem 2", "Resultado"]
    images = [image1, image2, result_image]
    for i, (img, title) in enumerate(zip(images, titles)):
        plt.subplot(1, 3, i + 1)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title(title)
        plt.axis("off")
    plt.tight_layout()
    plt.show()
