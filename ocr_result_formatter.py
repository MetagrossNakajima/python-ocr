import re

def format_ocr_result(texts):
    splitlined_text = texts.splitlines()
    len_1_over_and_formatted_texts = [filter_string(t) for t in splitlined_text if len(filter_string(t)) > 1]
    print(len_1_over_and_formatted_texts)

    pokemons = [{"name": "", "info": []} for _ in range(6)]
    tmp = []
    i = 0
    for t in len_1_over_and_formatted_texts:
        if t.startswith("Lv"):
            pokemons[i]["name"] = tmp.pop()
            if i > 0:
                pokemons[i - 1]["info"] = tmp
                tmp = []
            i += 1
        else:
            tmp.append(t)

    if i > 0:
        pokemons[i - 1]["info"] = tmp

    return pokemons


def filter_string(s):
    # 英数字、ドット、･、・、ひらがな、カタカナを許容する正規表現パターン
    pattern = r'[^a-zA-Z0-9\.\･・\'\u3040-\u309F\u30A0-\u30FF]'
    return re.sub(pattern, '', s)


if __name__ == "__main__":
    text = """2
ペリッパー
Lv.629
あめふらし
「こだわりメガネ
なみのり
ほうふう
ハイドロポンプ
エアカッター
フローゼル
Lv.63 る
すいすい
こだわりハチマキ
ウェーブタックル
ここえるかぜ
アクアジェット
アイススピナー
ゴルダック
Lv.50 る
すいすい
とつげきチョッキ
ハイドロポンプ
こごえるかぜ
テラバースト
クリアスモッグ
カイリュー
Lv.75 8
マルチスケイル
け
するどいくちばし
ぼうふう
しんそく
まもる
かえんほうしゃ
ドドゲザン
Lv.75 ②
そうだいしょう
くろいメガネ
ふいうち
ダメおし
まもる
たぐり
ニンフィア
Lv.77
フェアリースキン
ボン
のみ
オ
ハイパーボイス
で
ん
こう
せっか
まも
る
ミストフィールド
3"""
    import pprint
    pprint.pprint(format_ocr_result(text))