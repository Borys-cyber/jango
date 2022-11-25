from django.http import request
from django.shortcuts import render
from django.views import generic
from .models import Product


def index(request):
    product=Product.objects.all()
    # product = Product.object.get(id=id)
    visits = request.session.get('visits', 0)
    request.session['visits'] = visits + 1

    return render(request, 'index.html', context={'product_list': product, 'visits': visits})

    # return render(request, 'index.html')


# def product_details(request, id):
#     product = Product.object.get(id=id)
#     visits = request.session.get('visits', 0)
#     request.session['visits'] = visits + 1
#
#     return render(request, 'index.html', context={'product': product, 'visits': visits})


class ProductListView(generic.ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'product_list'
    # visits = request.session.get('visits', 0)
    # request.session['visits'] = visits + 1
    # extra_context = {'visits': visits}

    def get_queryset(self):
        return Product.object.filter(price__gte=40)


def index1(request):
    print(f"Hi1\n{request}\n")
    return render(request, 'index-1.html')


def index2(request):
    print(f"Hi2\n{request}\n")
    return render(request, 'index-2.html')


def index3(request):
    print(f"Hi3\n{request}\n")
    return render(request, 'index-3.html')


def index4(request):
    print(f"Hi4\n{request}\n")
    return render(request, 'index-4.html')


def index5(request):
    print(f"Hi5\n{request}\n")
    return render(request, 'index-5.html')


class ProductListView(generic.ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'product_list'

# Create your views here.
