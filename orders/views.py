from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.models import currency
from .models import order
import json


@login_required
def toefl(req):
    dollor_rate = currency.objects.get(name='dollor').rate
    currency_cost = 225
    toman_cost = round(dollor_rate * currency_cost * 1.07)
    if req.method == 'GET':
        return render(req, 'toefl.html', {'currency_cost':currency_cost, 'toman_cost':toman_cost})

    else:
        information = {}
        #save recived information from toefl_form in iformation dictionary
        information['who'] = req.POST.get('person')
        information['username'] = req.POST.get('username')
        information['password'] = req.POST.get('password')
        information['time_type'] = req.POST.get('time_type')
        information['exam_place'] = req.POST.get('exam_place')
        information['exam_reason'] = req.POST.get('exam_reason')
        information['degree'] = req.POST.get('degree')
        information['country'] = ''
        for i in range(1,7):
            if req.POST.get('country'+str(i)):
                information['country'] += req.POST.get('country'+str(i)) + ', '
        information['comment'] = req.POST.get('comment')

        #convert dictionary to str to save datas in database
        information = json.dumps(information)
        Order = order(
            toman_cost = toman_cost,
            currency_cost = currency_cost,
            currency_rate = dollor_rate,
            information = information,
            order_type = 'toefl',
            user = req.user
        )

        if req.FILES.get('attach_file'):
            if req.FILES.get('attach_file').size > 1000000:
                return render(req, 'toefl.html')
            Order.attach_file = req.FILES.get('attach_file')

        Order.save()
        return render(req, 'toefl-details.html', {'order':Order})



@login_required
def order_details(req, order_id):
    Order = order.objects.get(id=order_id)

    if req.user == Order.user:
        information = json.loads(Order.information)
        information['toman_cost'] = Order.toman_cost
        information['currency_cost'] = Order.currency_cost
        information['currency_rate'] = Order.currency_rate
        information['currency_type'] = Order.currency_type

        order_details_page = Order.order_type + '-details.html'
        return render(req, order_details_page, information)

    else:
        return redirect('home')
