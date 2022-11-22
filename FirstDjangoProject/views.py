from typing import final
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from FirstDjangoProject import urls
from .forms import practiceforms
# import models services and news
from services.models import Services
from news.models import News
from contact.models import Contact

# create a paginator
from django.core.paginator import Paginator


def Home(request):
    ServiceData = Services.objects.all().order_by('Title')[1:5]  # - befor column name mean descending and without - mean Ascending
    NewsData = News.objects.all();
    data = {
        'NewsData': NewsData,
        'ServiceData': ServiceData,
    }
    # data = {
    #     'Title': 'welcom to Elearner!',
    #     'h2': 'welcom to Elearner Website!',
    #     'list': ['hp', 'dell', 'apple'],
    #     'numbers': [],
    #     'Students':[{'name': 'roky', 'phone': 32724262},
    #        {'name': 'boby', 'phone': 45724262},
    #        {'name': 'rony', 'phone': 327094262}]
    # }
    # return render(request, "index.html", data)
    return render(request, "portal_Home.html", data)

def AboutUs(request):
    if request.method=="GET":
        output = request.GET.get('output')
    return render(request, "about-Us.html", {'output':output})

    # return render(request, "about-Us.html")
    
def project(request):
    return render(request, "project.html")

def team(request):
    return render(request, "team.html")

def what_do(request):
    # __icontains
    ServiceData = Services.objects.all()
    # if request.method == 'GET':
    #     inputName = request.GET.get('Service_search')
    #     if inputName != None:
    #         SData = Services.objects.filter(Title__icontains = inputName)
    
    # paginations create
    pagination = Paginator(ServiceData, 2)
    page_Number = request.GET.get('page')
    Final_page = pagination.get_page(page_Number)
    data={
    #    'ServiceData': SData,
       'Final_page': Final_page
    }

    return render(request, "what-do.html", data)
def contact(request):
    return render(request, "contact.html")

def Submited(request):
    n = ''
    if request.method == "POST":
        Fname = request.POST.get('Fname')
        Lname = request.POST.get('Lname')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')
        message = request.POST.get('message')
        update = Contact(FirstName = Fname, LastName = Lname, ContactNumber = phone, Mails = mail, Messages = message)
        update.save()
        n = 'Data insert Successfully!'
    return render(request, "contact.html", {'n': n})

def practiceFrm(request):
    # get methods
    # finalAns = 0;
    # try:
    #     if request.method=="GET":
    # #     n1 = int(request.GET['num1'])
    # #     n2 = int(request.GET['num2'])
    #         n1 = int(request.GET.get('num1'))
    #         n2 = int(request.GET.get('num2'))
    #     # print(n1 + n2);
    #     finalAns = n1 + n2
    # except:
    #     pass
    # return render(request, "practiceFrm.html", {'output':finalAns})

    # post methods
    finalAns = 0
    # create a empty dectionary to data
    form = practiceforms()
    data = {'form': form}
    # data = {}
    try:
        if request.method=="POST":
            # n1 = int(request.post['num1'])
            # n2 = int(request.post['num2'])
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
        # print(n1 + n2);
        finalAns = n1 + n2
        # filup empty dectionary data
        data = {
            'form': form,
            'n1': n1,
            'n2': n2,
            'output': finalAns
        }
        url = "/about-Us/?output={}".format(finalAns)
        # return HttpResponseRedirect(url)
        return redirect(url)

        # return HttpResponseRedirect('/about-Us/')
        # return redirect('//about-Us/')
    except:
        pass
    return render(request, "practiceFrm.html", data)
def submitform(request):
    Pform = practiceforms()
    data = {'form': Pform}
    try:
        if request.method=="POST":
            # n1 = int(request.post['num1'])
            # n2 = int(request.post['num2'])
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
        # print(n1 + n2);
        finalAns = n1 + n2
        # filup empty dectionary data
        data = {
            'form': Pform,
            'n1': n1,
            'n2': n2,
            'output': finalAns
        }
        # url = "/about-Us/?output={}".format(finalAns)
        # return HttpResponseRedirect(url)
        # return redirect(url)
        return HttpResponse(finalAns)

        # return HttpResponseRedirect('/about-Us/')
        # return redirect('//about-Us/')
    except:
        pass

def calculate(request):
    c = ''
    count = {}
    try:
        if request.method=="POST":
            n1 = eval(request.POST.get('value_1'))
            n2 = eval(request.POST.get('value_2'))
            op = request.POST.get('operator')

            if op == "+":
                c = n1 + n2
            elif op == "-":
                c = n1 - n2
            elif op == "*":
                c = n1 * n2
            elif op == "/":
                c = n1 / n2

        count = {
            'n1': n1,
            'n2': n2
        }
    except:
        c = "invalid operator !"
    print(c)
    return render(request, "calculate.html", {'c':c})
def oddEven(request):
    output = ''
    try:
        if request.method == "POST":
            num = eval(request.POST.get("num"))

            if num % 2 == 0:
                output = "Even number"
            elif num % 2 != 0:
                output = "Odd number"
            else:
                output = "Invalid number"
    except:
        output = "Error"
    print(output)
    return render(request, "oddEven.html", {'output': output})

def markshet(request):
        if request.method == "POST":
            sub_1 = eval(request.POST.get("num1"))
            sub_2 = eval(request.POST.get("num2"))
            sub_3 = eval(request.POST.get("num3"))
            sub_4 = eval(request.POST.get("num4"))
            sub_5 = eval(request.POST.get("num5"))

            t = sub_1 + sub_2 + sub_3 + sub_4 + sub_5
            p = t*100/500
            
            if p >= 80:
                d = "First Class"
            elif p >= 65:
                d = "Second Class"
            elif p >= 40:
                d = "third Class"
            else:
                d = "fail"
            data = {
                'total': t,
                'percentage': p,
                'divition': d
            }
            return render(request, "markshet.html", data)
        return render(request, "markshet.html")
def NewsShow(request, slug):
    newsData = News.objects.get(autoslug = slug)
    data ={
        'newsData': newsData,
    }
    return render(request, "NewsShow.html", data)