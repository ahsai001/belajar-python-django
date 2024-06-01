from django.shortcuts import render

# Create your views here.
def tambah(request, num1, num2):
    context = {
        'title': 'Kalkulator Tambah',
        'result': f'{num1} + {num2} = {num1+num2}'
    }
    return render(request, 'calculator/index.html', context)

def kurang(request, num1, num2):
    context = {
        'title': 'Kalkulator Kurang',
        'result': f'{num1} - {num2} = {num1-num2}'
    }
    return render(request, 'calculator/index.html', context)

def kali(request, num1, num2):
    context = {
        'title': 'Kalkulator Kali',
        'result': f'{num1} x {num2} = {num1*num2}'
    }
    return render(request, 'calculator/index.html', context)

def bagi(request, num1, num2):
    context = {
        'title': 'Kalkulator Bagi',
        'result': f'{num1} : {num2} = {num1/num2}'
    }
    return render(request, 'calculator/index.html', context)