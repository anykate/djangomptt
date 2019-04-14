from django.shortcuts import render
from .models import Category


# Create your views here.
def home(request):
    my_queryset = Category.objects.all()
    categories=Category.objects.get_queryset_descendants(my_queryset, include_self=True)
    return render(request, 'app_mptt/home.html', {'categories': categories})
