# Imports the Google Cloud client library
from google.cloud import vision


def get_contend(path):
    with open(path, "rb") as image_file:
        content = image_file.read()
    return content


def detect_text(content):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    return response.text_annotations[0].description


if __name__ == "__main__":
    path = "./merged.png"
    detect_text(path)
