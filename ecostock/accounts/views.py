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
    form = ProdutoForm()
    
    if request.method == 'POST':
        if 'additem' in request.POST:
            pk = request.POST.get('additem')
            if not pk:    
                form = ProdutoForm(request.POST)
            else:
                    produto = Produto.objects.get(id=pk)
                    form = ProdutoForm(request.POST, instance=produto)
            form.save()
            return redirect('/home/')
            
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            produto = Produto.objects.get(id=pk)
            produto.delete()
            return redirect('/home/')
        
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            produto = Produto.objects.get(id=pk)
            form = ProdutoForm(instance=produto)
    else: 
        form = ProdutoForm()
        
    produtos = Produto.objects.all()
    return render(request, 'home.html', {'form': form, 'produtos': produtos})