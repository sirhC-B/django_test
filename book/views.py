from django.shortcuts import render
from book.models import *
from book.forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


# Create your views here.


def get_purchase_list(request):
    purchases = Purchase.objects.all()

    return render(request, 'purchase/purchase_list.html', {'page_title': 'My Purchases',
                                                           'purchases': purchases,
                                                           })


def shop_list(request):
    shop = Shop.objects.all()

    return render(request, 'purchase/shop_list.html', {'page_title': 'Shop List',
                                                       'shops': shop,
                                                       })


def set_list(request):
    sets = Set.objects.all()

    return render(request, 'purchase/set_list.html', {'page_title': 'Lego Sets',
                                                      'sets': sets,
                                                      })


def theme_list(request):
    theme = Theme.objects.all()

    return render(request, 'purchase/theme_list.html', {'page_title': 'Themes',
                                                        'themes': theme,
                                                        })


def owner_list(request):
    owner = Owner.objects.all()

    return render(request, 'purchase/owner_list.html', {'page_title': 'Owner',
                                                        'owners': owner,
                                                        })


def add_shop(request):
    shop = Shop()
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Shop saved.')
            return HttpResponseRedirect(reverse_lazy('purchase_list'))
        else:
            messages.error(request, 'Data incorrect!')



    else:
        form = ShopForm(instance=shop)

    return render(request, 'purchase/add_shop.html', {'page_title': 'Add Shop',
                                                      'form': form,
                                                      })


def add_theme(request):
    theme = Theme()
    if request.method == 'POST':
        form = ThemeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Theme saved.')
            return HttpResponseRedirect(reverse_lazy('theme_list'))
        else:
            messages.error(request, 'Data incorrect!')
    else:
        form = ThemeForm(instance=theme)

    return render(request, 'purchase/add_theme.html', {'page_title': 'Add Theme',
                                                       'form': form,
                                                       })


def add_set(request):
    set = Set()
    if request.method == 'POST':
        form = SetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Set saved.')
            return HttpResponseRedirect(reverse_lazy('set_list'))
        else:
            messages.error(request, 'Data incorrect!')



    else:
        form = SetForm(instance=set)

    return render(request, 'purchase/add_set.html', {'page_title': 'Add Set',
                                                     'form': form,
                                                     })


def add_owner(request):
    owner = Owner()
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Owner saved.')
            return HttpResponseRedirect(reverse_lazy('owner_list'))
        else:
            messages.error(request, 'Data incorrect!')



    else:
        form = OwnerForm(instance=owner)

    return render(request, 'purchase/add_owner.html', {'page_title': 'Add Owner',
                                                       'form': form,
                                                       })

def add_purchase(request):
    purchase = Purchase()
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Purchase saved.')
            return HttpResponseRedirect(reverse_lazy('purchase_list'))
        else:
            messages.error(request, 'Data incorrect!')



    else:
        form = PurchaseForm(instance=purchase)

    return render(request, 'purchase/add_purchase.html', {'page_title': 'Add Purchase',
                                                       'form': form,
                                                       })
