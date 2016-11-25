from BeautifulSoup import BeautifulSoup
import urllib2

def createDictOfPrices(soup):
    prices = {}
    last = soup('ul', {'class' : 'last'})
    
    for element in last:
        for el in element.findAll('li'):
            prices[el.text.split(':')[0]] = el.text.split(':')[1]
    return prices 
    
def getPrice(url):
    opener = urllib2.build_opener()
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
                }
    opener.addheaders = headers.items()
    page = opener.open(url)
    soup = BeautifulSoup(page)
    
    return createDictOfPrices(soup)
