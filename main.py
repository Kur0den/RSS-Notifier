import time

import schedule
from requests import get
from xmltodict import parse


def job():
    rss_url = "RSS_URL" # RSSのURL
    response = get(rss_url) # RSSを取得
    parse_data = parse(response.text) # RSS(xml)をDict化

    '''
    ここでparse_dataから欲しい情報を引っ張り出して使う

    使いにくいのはしらん
    '''

## 分ごとにRSSを取得したいなら
# schedule.every(MINUTE).minutes.do(job)
## 時ごとに取得なら
# schedule.every(HOUR).hours.do(job)
## 指定時刻に取得なら
# schedule.every().day.at("HH:MM", "TIMEZONE").do(job)

## 詳しくは https://schedule.readthedocs.io/en/stable/index.html

# ずっと実行させるやつ(?)
while True:
    schedule.run_pending()
    time.sleep(1)