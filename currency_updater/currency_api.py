from home.models import currency
import requests
from bs4 import BeautifulSoup

def get():
    page = requests.get('https://api.sunnyweb.ir')
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', {'class':'table'})
    

    dollor = currency.objects.get(name='dollor')
    dollor.rate = int(list(list(list(table)[3])[1])[7].text) // 10
    dollor.save()

    euro = currency.objects.get(name='euro')
    euro.rate = int(list(list(list(table)[3])[3])[7].text) // 10
    euro.save()

    pond = currency.objects.get(name='pond')
    pond.rate = int(list(list(list(table)[3])[5])[7].text) // 10
    pond.save()
