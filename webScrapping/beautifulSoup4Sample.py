import bs4,requests

def getBCIPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('.woocommerce-Price-amount')
    return elems[0].text.strip()


price = getBCIPrice('https://www.bladecultureusa.com/?product=gtg-t')
print('The Price is ' + price)