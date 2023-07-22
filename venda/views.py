from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm

# Create your views here.
def index(request):
    lista_index=Produto.objects.all()
    context = {'objetos':lista_index}
    return render(request,'venda/index.html',context)

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

def produto_detalhar(request,id_produto):
    produto = get_object_or_404(Produto, id=id_produto)
    context={
        'produto' : produto,
    }
    return render(request,'venda/produto/detalhe.html',context)