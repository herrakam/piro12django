
import logging
import re
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from . models import Item
from . forms import ItemForm
# Create your views here.
def archives_year(request,year):
    return HttpResponse('{}년도에 대한 내용'.format(year))

def item_list(request):
    qs= Item.objects.all()
    q=request.GET.get('q','')
    if q:
        qs = qs.filter(name__icontains=q)

    logger.debug('query : {}'.format(q))

    return render(request, 'shop/item_list.html',{
        'item_list':qs,
        'q' : q,
    })

def item_detail(request,pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_list.html',{
        'item': item,
    })

def item_new(request, item=None):
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect(item)
    else:
        form=ItemForm(instance=item)

    return render(request, 'shop/item_form.html', {
        "form": form,
    })


def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return item_new(request, item)
