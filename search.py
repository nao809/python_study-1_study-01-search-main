### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
# source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

with open("source.csv", encoding="shift-jis") as f:
    source = f.read().split('\n')
#print(source)

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    if word in source:
        print("{}が見つかりました".format(word))
    else:
        print("{}が見つかりませんでした".format(word))
        with open("source.csv", mode='a') as f:
            f.write(word)

if __name__ == "__main__":
    search()
