import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen

def main():
    url = 'https://spreadsheets.google.com/feeds/list/1azDyccjKiAU0G8HymIeJt34JTDR6jxaqvgbfQE5rt_k/ovifiob/public/values?alt=json'
    response = urlopen(url)
    data = json.loads(response.read().decode('utf-8')) 
    print("")
    for element in data['feed']['entry']:
        title = element['title']['$t']
        if ":" not in title:
            title = title + ":"
        status = element['gsx$message']['$t']
        print(title + " " + status)
    print("")
