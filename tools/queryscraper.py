import urllib.request, json

with urllib.request.urlopen(
        "https://query1.finance.yahoo.com/v8/finance/chart/HINDUNILVR.NS?region=US&lang=en-US&includePrePost=false&interval=30m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance") as url:
    data = json.loads(url.read().decode())
    print("https://query1.finance.yahoo.com/v8/finance/chart/HINDUNILVR.NS?region=US&lang=en-US&includePrePost=false&interval=30m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance")
    print(data['chart']['result'][0]['meta']['symbol'])
    print(data['chart']['result'][0]['indicators']['quote'][0]['open'])
    print(data['chart']['result'][0]['indicators']['quote'][0]['high'])
    print(data['chart']['result'][0]['indicators']['quote'][0]['low'])
    print(data['chart']['result'][0]['indicators']['quote'][0]['close'])
    print(data['chart']['result'][0]['indicators']['quote'][0]['volume'])



