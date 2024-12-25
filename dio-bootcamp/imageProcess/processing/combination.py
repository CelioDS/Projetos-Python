import cv2

def transfer_histogram(source, target):
    """Transfere o histograma da imagem `source` para `target`."""
    if source is None or target is None:
        return None
    source_hsv = cv2.cvtColor(source, cv2.COLOR_BGR2HSV)
    target_hsv = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

    # Igualar histogramas de cada canal
    for i in range(3):  # H, S, V
        source_hist, _ = cv2.calcHist([source_hsv], [i], None, [256], [0, 256])
        target_hist, _ = cv2.calcHist([target_hsv], [i], None, [256], [0, 256])
        lut = cv2.createCLAHE(clipLimit=2.0).apply(target_hist.flatten())
        target_hsv[..., i] = cv2.LUT(target_hsv[..., i], lut)

    return cv2.cvtColor(target_hsv, cv2.COLOR_HSV2BGR)
