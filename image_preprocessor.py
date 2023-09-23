from PIL import Image, ImageDraw, ImageOps
import io


def prepare_for_ocr(path):
    with Image.open(path) as im:
        w, h = im.size
        X_BASE_PX = 1280
        Y_BASE_PX = 720
        percent_w = w / X_BASE_PX
        percent_y = h / Y_BASE_PX

        X_POKEMON_START = [int(x*percent_w) for x in [40, 650]]
        X_MOVE_START = [int(x*percent_w) for x in [398, 1005]]
        Y_POKEMON_START = [int(y*percent_y) for y in [100, 282, 464]]
        Y_ITEM_START = [int(y*percent_y)for y in [218, 400, 582]]

        X_P_WIDTH = int(221*percent_w)  # ポケモン情報の横幅
        X_M_WIDTH = int(191*percent_w)  # 技情報の横幅
        Y_P_HEIGHT = int(164*percent_y)  # ポケモン情報の縦幅
        X_I_WIDTH = int(46*percent_w)
        Y_I_HEIGHT = int(37*percent_y)

        pokemons = []
        moves = []

        for y_p_s, y_i_s in zip(Y_POKEMON_START, Y_ITEM_START):
            y_p_e = y_p_s + Y_P_HEIGHT

            # pokemon画像の追加
            for x_p_s in X_POKEMON_START:
                x_p_e = x_p_s + X_P_WIDTH
                x_i_e = x_p_s + X_I_WIDTH
                y_i_e = y_i_s + Y_I_HEIGHT

                # 持ち物が文字と誤認識される場合があるため塗りつぶす
                draw = ImageDraw.Draw(im)
                draw.ellipse((x_p_s, y_i_s, x_i_e, y_i_e),
                             fill=(0, 0, 0),
                             outline=(0, 0, 0))

                cropped_pokemon = im.crop((x_p_s, y_p_s, x_p_e, y_p_e))
                pokemons.append(cropped_pokemon)

            # 技画像の追加
            for x_m_s in X_MOVE_START:
                x_m_e = x_m_s + X_M_WIDTH
                cropped_move = im.crop((x_m_s, y_p_s, x_m_e, y_p_e))
                moves.append(cropped_move)

        # 新しい画像のサイズを計算
        new_width = X_P_WIDTH
        new_height = Y_P_HEIGHT * 12

        # 新しい画像を作成
        merged_img = Image.new("RGB", (new_width, new_height))

        # 画像を結合
        for i in range(0, 6, 1):
            p_height = i * 2 * Y_P_HEIGHT
            m_height = p_height + Y_P_HEIGHT
            merged_img.paste(pokemons[i], (0, p_height))
            merged_img.paste(moves[i], (0, m_height))

        # グレースケール化
        grayscale_image = ImageOps.grayscale(merged_img)
        buffered_image = io.BytesIO()
        grayscale_image.save(buffered_image, format="JPEG")
        return buffered_image.getvalue()


if __name__ == "__main__":
    path = "./orecore.jpg"
    prepare_for_ocr(path)
