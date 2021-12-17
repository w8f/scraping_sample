import requests
from bs4 import BeautifulSoup

url = 'https://sauna-ikitai.com/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

# print(soup)
# print(soup.prettify())

# h2タグ全てをとってくる
h2 = soup.find_all('h2')

# 最初のh2タグをとってくる
h2 = soup.find('h2')

# h2 = soup.h2()
print(h2.text)

# 引数attrsでクラスを指定する。
p = soup.find_all('p', attrs={'class': 'c-lead'})

print(p)

# セレクタで指定する
# .hoge はクラス名hogeの要素を取得する
c_lead = soup.select('.c-lead')

print(c_lead)

# セレクタで指定する
# .hoge はクラス名hogeの要素を取得する
# 先頭の要素ををリストで返す
c_lead = soup.select_one('.c-lead')

print(c_lead)
