from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import currency


def home(req):
    currencies = currency.objects.all()
    return render(req, 'index.html', {'dollor_rate':currency.objects.get(name='dollor').rate, 'euro_rate':currency.objects.get(name='euro').rate, 'pond_rate':currency.objects.get(name='pond').rate})

def services(req):
    return render(req, 'services.html')