from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseNotAllowed
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render
from .models import Produto
from .forms import ProdutoForm
# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
def welcome(request):
    return render(request, 'welcome.html')    

def getHome(request):
    return render(request, 'gethome.html')

def home(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else: 
        form = ProdutoForm()
        
    produtos = Produto.objects.all()
    return render(request, 'home.html', {'form':form, 'produtos': produtos})