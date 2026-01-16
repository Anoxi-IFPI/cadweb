from django.shortcuts import render, redirect

from .models import *

from .forms import *

from django .contrib import messages

def index(request):
    return render(request,'index.html')

def categoria(request):
    contexto = {
        'lista': Categoria.objects.all().order_by('-id'),
    }
    return render(request, 'categoria/lista.html',contexto)


# Formulário de Categoria
def form_categoria(request):
    if request.method == 'POST':
       form = CategoriaForm(request.POST) # instancia o modelo com os dados do form
       if form.is_valid():# faz a validação do formulário
            form.save() # salva a instancia do modelo no banco de dados
            messages.success(request, 'Categoria cadastrada com sucesso!')
            return redirect('categoria') # redireciona para a listagem
    else:# método é get, novo registro
        form = CategoriaForm() # formulário vazio
    contexto = {
        'form':form,
    }
    return render(request, 'categoria/formulario.html', contexto)


# Editar Categoria
def editar_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
    except Categoria.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('categoria')  # Redireciona para a listagem
     
    if request.method == 'POST':
        # combina os dados do formulário submetido com a instância do objeto existente, permitindo editar seus valores.
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save() # save retorna o objeto salvo
            messages.success(request, 'Operação realizada com Sucesso')
            return redirect('categoria') # redireciona para a listagem
    else:
         form = CategoriaForm(instance=categoria)
    return render(request, 'categoria/formulario.html', {'form': form,})


# View para exibir detalhes 
def detalhes_categoria(request, id):
    categoria = Categoria.objects.get(pk=id) # Busca a categoria no banco [cite: 12]
    return render(request, 'categoria/detalhes.html', {'item': categoria}) 

# View para remover categoria 
def remover_categoria(request, id):
    categoria = Categoria.objects.get(pk=id)
    categoria.delete() # Exclui o registro
    return redirect('categoria') # Redireciona para listagem 

# View para listar clientes
def cliente(request):
    contexto = {
        'lista': Cliente.objects.all().order_by('-id'),
    }
    return render(request, 'cliente/lista.html',contexto)

def form_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Operação realizada com sucesso!')
            return redirect('cliente')
        else:
            # Opcional: Mensagem genérica, pois os erros específicos 
            # estarão no form.errors dentro do template.
            messages.error(request, 'Erro ao salvar o registro. Verifique os campos.')
    else:
        form = ClienteForm() # Método GET: Formulário vazio
    
    contexto = {'form': form}
    return render(request, 'cliente/formulario.html', contexto)


# --- ADICIONE ISSO AO FINAL DO SEU VIEWS.PY ---

# View para Editar Cliente
def editar_cliente(request, id):
    try:
        cliente_instancia = Cliente.objects.get(pk=id)
    except Cliente.DoesNotExist:
        messages.error(request, 'Cliente não encontrado')
        return redirect('cliente')

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente_instancia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('cliente')
    else:
        form = ClienteForm(instance=cliente_instancia)
    
    return render(request, 'cliente/formulario.html', {'form': form})

# View para Remover Cliente
def remover_cliente(request, id):
    try:
        cliente_instancia = Cliente.objects.get(pk=id)
        cliente_instancia.delete()
        messages.success(request, 'Cliente removido com sucesso!')
    except Cliente.DoesNotExist:
        messages.error(request, 'Erro ao remover: Cliente não encontrado')
    
    return redirect('cliente')


# ... (mantenha o código anterior de categoria e cliente como está)

# --- VIEWS DE PRODUTO (Baseado no Slide 13 e no seu arquivo lista.html) ---

# View para listar produtos 
def produto(request):
    contexto = {
        'lista': Produto.objects.all().order_by('-id'),
    }
    return render(request, 'produto/lista.html', contexto)

# View para o formulário de produto
def form_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto salvo com sucesso!')
            return redirect('produto')
    else:
        form = ProdutoForm()
    
    # Verifique se o nome do arquivo é formulario.html ou form.html (seu zip veio como form.html)
    return render(request, 'produto/form.html', {'form': form})

# View para Editar Produto (Necessária para o botão Editar do lista.html)
def editar_produto(request, id):
    item = Produto.objects.get(pk=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado!')
            return redirect('produto')
    else:
        form = ProdutoForm(instance=item)
    return render(request, 'produto/form.html', {'form': form})

# View para Remover Produto (Necessária para o botão Remover do lista.html)
def remover_produto(request, id):
    item = Produto.objects.get(pk=id)
    item.delete()
    messages.success(request, 'Produto removido!')
    return redirect('produto')

# View para Detalhes do Produto (Slide 70)
def detalhes_produto(request, id):
    item = Produto.objects.get(pk=id)
    return render(request, 'produto/detalhes.html', {'item': item})
