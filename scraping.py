# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys
from urllib import request
import os.path

# url先の画像を保存する関数
def download(url):
    img = request.urlopen(url)
    localfile = open(os.path.basename(url), 'wb')
    localfile.write(img.read())
    img.close()
    localfile.close()


# 年指定
s = input("year：")
year = int(s)
# 月指定
s = input("month：")
month = int(s)
# 日にち指定
s = input("day：")
day = int(s)
# shutterstockの画像検索結果を保存

base_url = "http://www.bijogoyomi.com"

while day<31:
    # アクセス先
    par_url = base_url + "/bijo3/index.php/"+str(year) + "/" + str("{0:02d}".format(month)) + '/' + str("{0:02d}".format(day))
    # urlアクセス
    res = request.urlopen(par_url)
    # beautifulsoupでパース
    soup = BeautifulSoup(res.read(), "html.parser")

    # ページに存在するimgタグを検索
    for link in soup.find_all('img'):
        # 画像URLを取得
        img_url = link.get('src')
        print (img_url)

        # お休みの日は日付をプラスしてスキップ
        if "holiday" in img_url:
            day += 1
            break

        elif "img2.php" in img_url:
            img_url = base_url + img_url
            # ローカルに画像をダウンロード
            download(img_url)
            # 次の日を読み込みするようにする
            day += 1
            break
