# EMoSearch
## 目次

1.[概要](#概要)
2.[使用している技術](#使用している技術)
3.[仕組み](#仕組み)
4.[環境](#環境)
5.[開発環境構築](#開発環境構築)
## 概要
入力されるいくつかの単語から，推測される絵文字を提供する web アプリケーションです．
PKSHA Technology の日本語テキスト埋め込みモデル [GLuCoSE](https://huggingface.co/pkshatech/GLuCoSE-base-ja) に絵文字に関するデータセットの情報を与えてファインチューニングをしています．
## 使用している技術

## 仕組み

## 環境
|言語/フレームワーク|バージョン|
|------------------|--------|
|Python||
|Reflex|0.4.9|

その他のパッケージのバージョンは requirements.txtを参照してください.

## 環境構築
```
$ python -m venv venv
```
```
$ source ./venv/bin/activate
```
```
$ cd EmojiSearch/venv/
$ pip install -r requirements.txt
```

続きは後で書きます...
