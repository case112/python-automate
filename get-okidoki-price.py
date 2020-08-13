import bs4, requests

print('Insert okidoki.ee product link here to get the price:')
url = input()

def get_okidoki_price(product_url):
    res = requests.get(product_url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    element = soup.select('.price')
    return element[0].text.strip()

print('Price is: ' + get_okidoki_price(url))