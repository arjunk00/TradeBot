import csv
import requests
dates = ["year1month1","year1month2","year1month3","year1month4","year1month5","year1month6","year1month7","year1month8","year1month9","year1month10","year1month11","year1month12","year2month1","year2month2","year2month3","year2month4","year2month5","year2month6","year2month7","year2month8","year2month9","year2month10","year2month11","year2month12"]
for i in dates:
    CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=1min&slice='+i+'&apikey=R7J7IVX7H1WYY18Y'

    with requests.session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        mylist = list(cr)
        for row in mylist:
            print(row)