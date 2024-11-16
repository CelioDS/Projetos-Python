from image_processing.utils import io, plot
from image_processing.processing import combination, transformation


image1 = io.read_image(r"C:\Users\celio\Downloads\arvore1.webp")
image2 = io.read_image(r"C:\Users\celio\Downloads\arvore2.png")

if image1 is None or image2 is None:
    raise  ValueError("Image error")

#plot.plot_image(image1)
#plot.plot_image(image2)

result_image = combination.transfer_histogram(image1, image2)

if result_image is None:
    raise  ValueError("Error process")

plot.plot_result(image1, image2, result_image)


