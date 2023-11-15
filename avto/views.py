from django.shortcuts import render
from .models import Avto

def avtomobiles(request):
    content = Avto.objects.all()
    # content = [
    #     {'model':'cobalt', 'year':'2000', 'price':'6700', 'color':'white', 'image':'images/cobalt.png'},
    #     {'model':'jentra', 'year':'2019', 'price':'12000', 'color':'black', 'image':'images/jentra.jpeg'},
    #     {'model':'nexia 3', 'year':'2020', 'price':'11000', 'color':'blue', 'image':'images/nexia3.jpg'}
    # ]
    return render(request=request, template_name='avtomobiles.html', context={'content':content})
