from requests import get
from xmltodict import parse


rss_url = "RSS_URL"
response = get(rss_url)
print(type(response.text))
parse_data = parse(response.text)

'''
あとはparse_dataから欲しい情報を引っ張り出して使う

使いにくいのはしらん'''