# 学習メモ(Scraping Sample)

## 仮想環境の作成
```shell:title
$ python3 -m venv .venv
```

## 仮想環境への切り替え
```shell:title
$ . .venv/bin/activate
(.venv) $
```

## python-dotenv モジュールのインストール
```shell:title
(venv) $ pip install python-dotenv

```

## スクレイピング準備

- ライブラリインストール
- ブラウザ起動
- Webサイトアクセス
- Webサイトログイン


## ライブラリインストール

### selenium インストール
```shell:title
$ pip install selenium
```

### chromedriver インストール(mac)
```shell:title
$ brew install chromedriver

# chromedriverのパスを通すコード
$ pip install chromedriver-binary-auto

```

### HEADLESS MODE
```py:main.py
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')

browser = webdriver.Chrome(options=options)
```


### Link

- [seleniumを使用しようとしたら、「"chromedriver"は開発元を検証できないため開けません。」と言われた](https://qiita.com/apukasukabian/items/77832dd42e85ab7aa568)
- [Python/ChromeDriverインストールとパスの通し方](https://watlab-blog.com/2019/08/10/chromedriver-path/)
