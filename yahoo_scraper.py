import requests
from bs4 import BeautifulSoup as bs
import time
import csv

urls=  ["https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch", "https://finance.yahoo.com/quote/RLLCF?p=RLLCF", "https://finance.yahoo.com/quote/AMD?p=AMD", "https://finance.yahoo.com/quote/AVP?p=AVP"]
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

open_csv = open("stock_scrap.csv", "w")
csv_writer = csv.writer(open_csv)
csv_writer.writerow(["Stock Name","Current Value","Previous Close", "Open", "Bid", "Ask", "Day's Range", "52 Week Range", "Volume", "Avg. Volume" ])

for url in urls:
    stock = []
    html_page = requests.get(url, headers=headers)
    # create soup object.
    soup = bs(html_page.content, 'lxml')
    header_info = soup.find_all("div", id = 'quote-header-info')[0]
    stock_title = header_info.find("h1").get_text()
    stock_price = header_info.find("div", class_ = "D(ib) Mend(20px)").find("span").get_text()
    stock.append(stock_title)
    stock.append(stock_price)
    # Table information
    table_info = soup.find_all('div',class_ = 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')[0].find_all('tr')
    for i in range(0,8):
        table_value = table_info[i].find_all ("td")[1].get_text ()
        stock.append(table_value)
    csv_writer.writerow(stock)
    time.sleep(5)
open_csv.close()