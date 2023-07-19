from django.shortcuts import render, get_object_or_404, redirect
from .models import Marca, Produto
from .forms import MarcaForm, ProdutoForm

# Create your views here.
def index(request):
    total_marcas = Marca.objects.count() #Retorna a quantidade de elementos do banco
    total_produtos = Produto.objects.count()
    context = {
        'total_marcas' : total_marcas,
        'total_produtos' : total_produtos,
    }
    return render(request, 'venda/index.html', context)


#Marca
def marca_editar(request, id = id):
    marca = get_object_or_404(Marca, id = id)
   
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance = marca)

        if form.is_valid():
            form.save()
            return redirect('marca_listar')
    else:
        form = MarcaForm(instance = marca) #Evita a duplicação de informações, pois recebe como instância um aluno que já existe

    return render(request,'venda/marca/formmarca.html', {'form' : form}) 


def marca_remover(request, id):
    marca = get_object_or_404(Marca, id = id)
    marca.delete()
    return redirect('marca_listar') #Procure um url com o nome 'lista_aluno'


def marca_criar(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marca_listar')
    else:
        form = MarcaForm()

    return render(request, 'venda/marca/formmarca.html', {'form': form})


def marca_listar(request):
    marcas = Marca.objects.all()
    context = {
        'marcas': marcas
    }
    return render(request, 'venda/marca/marcas.html', context)



#Produto
def produto_editar(request, id = id):
    produto = get_object_or_404(Produto, id = id)
   
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance = produto)

        if form.is_valid():
            form.save()
            return redirect('produto_listar')
    else:
        form = ProdutoForm(instance = produto) #Evita a duplicação de informações, pois recebe como instância um aluno que já existe

    return render(request,'venda/produto/formproduto.html', {'form' : form}) 


def produto_remover(request, id):
    produto = get_object_or_404(Produto, id = id)
    produto.delete()
    return redirect('produto_listar') #Procure um url com o nome 'lista_aluno'


def produto_criar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto_listar')
    else:
        form = ProdutoForm()

    return render(request, 'venda/produto/formproduto.html', {'form': form})


def produto_listar(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'venda/produto/produtos.html', context)