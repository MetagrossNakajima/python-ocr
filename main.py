from image_preprocessor import prepare_for_ocr
from google_ocr import detect_text
from ocr_result_formatter import format_ocr_result


def main(path):
    content = prepare_for_ocr(path)
    texts = detect_text(content)
    pokemons = format_ocr_result(texts)
    print(pokemons)


if __name__ == "__main__":
    path = "./orecore.jpg"
    main(path)
