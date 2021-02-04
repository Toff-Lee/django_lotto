from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm
# Create your views here.

def index(request):

    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos':lottos})

def hello(request):
    return HttpResponse('<h1 style="color:red;">Hellom world!</h1>')


def post(request):

    if request.method == 'POST':
        print()
        print('*** CURRENT REQUEST IS POST ***')
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            return redirect('index')

    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey) # primary key
    return render(request, "lotto/detail.html", {"lotto":lotto})
