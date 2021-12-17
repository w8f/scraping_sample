# 学習メモ(Scraping Sample)

- [学習メモ(Scraping Sample)](#学習メモscraping-sample)
  - [仮想環境の作成](#仮想環境の作成)
  - [仮想環境への切り替え](#仮想環境への切り替え)
  - [python-dotenv モジュールのインストール](#python-dotenv-モジュールのインストール)
  - [スクレイピング準備](#スクレイピング準備)
    - [各ライブラリ インストール](#各ライブラリ-インストール)
    - [selenium インストール](#selenium-インストール)
    - [chromedriver インストール(mac)](#chromedriver-インストールmac)
    - [HEADLESS MODE](#headless-mode)
    - [CSV 出力](#csv-出力)
  - [BeatifulSoup4を利用したスクレイピング](#beatifulsoup4を利用したスクレイピング)
    - [ライブラリインストール](#ライブラリインストール)
  - [Link](#link)

## 仮想環境の作成

```shell
python3 -m venv .venv
```

## 仮想環境への切り替え

```shell
$ . .venv/bin/activate
(.venv) $
```

## python-dotenv モジュールのインストール

```shell
(venv) $ pip install python-dotenv

```

## スクレイピング準備

- ライブラリインストール
- ブラウザ起動
- Webサイトアクセス
- Webサイトログイン

### 各ライブラリ インストール

```shell
pip install selenium
pip install numpy
pip install pandas
```

### selenium インストール

```shell
pip install selenium
```

### chromedriver インストール(mac)

```shell
$ brew install chromedriver

# chromedriverのパスを通すコード
$ pip install chromedriver-binary-auto

```

### HEADLESS MODE

```py
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')

# こちらでもOK
options.set_headless(True)

browser = webdriver.Chrome(options=options)
```

### CSV 出力

```py
import pandas as pd
df = pd.DataFrame()
df['hoge'] = names
df.to_csv('hoge.csv')
```

## BeatifulSoup4を利用したスクレイピング

### ライブラリインストール

```shell
pip install requests
pip install BeautifulSoup4
```

BeautifulSoup4はHTMLの構造解析をしてくれる

## Link

- [seleniumを使用しようとしたら、「"chromedriver"は開発元を検証できないため開けません。」と言われた](https://qiita.com/apukasukabian/items/77832dd42e85ab7aa568)
- [Python/ChromeDriverインストールとパスの通し方](https://watlab-blog.com/2019/08/10/chromedriver-path/)
