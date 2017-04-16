from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.


@login_required(login_url='/login/')
def view_company_list(request):
    # list = get_object_or_404()
    lists = ProductCompany.objects.all()
    return render(request, 'company_list.html', {'lists': lists, })


@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_superuser, login_url='/login/')
def add_company_view(request):
    if request.method == "POST":
        company_form = AddCompanyForm(request.POST)
        if company_form.is_valid():
            add_company = company_form.save(commit=False)
            add_company.save()
            return redirect('/company_list/')
    else:
        company_form = AddCompanyForm()
    return render(request, 'add_company.html', {'form': company_form})


@login_required(login_url='/login/')
def view_group_list(request):
    lists = ProductGroup.objects.all()
    return render(request, 'group_list.html', {'lists': lists, })


@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_superuser, login_url='/login/')
def add_group_view(request):
    if request.method == "POST":
        group_form = AddGroupForm(request.POST)
        if group_form.is_valid():
            group_form.save()
            return redirect('/group_list/')
    else:
        group_form = AddGroupForm()
    return render(request, 'add_group.html', {'form': group_form})


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_superuser, login_url='/login/')
def add_product_view(request):
    company_name = ProductCompany.objects.all()
    group_name = ProductGroup.objects.all()
    if request.method == "POST":
        product_form = AddProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect('/product_list/')
        else:
            messages.error(request, 'All fields required')
    else:
        product_form = AddProductForm()
    return render(request, 'add_product.html',
                  {'form': product_form, 'company_name': company_name, 'group_name': group_name})


@login_required(login_url='/login/')
def view_product_list(request):
    # list = get_object_or_404()
    lists = Product.objects.all()
    return render(request, 'product_list.html', {'lists': lists, })


@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_superuser, login_url='/login/')
def add_supplier_view(request):
    if request.method == "POST":
        supplier_form = AddSupplierForm(request.POST)
        if supplier_form.is_valid():
            supplier_form.save()
            return redirect('/supplier_list/')
        else:
            messages.error(request, 'All fields required')
    else:
        supplier_form = AddSupplierForm()
    return render(request, 'add_supplier.html', {'form': supplier_form})


@login_required(login_url='/login/')
def view_supplier_list(request):
    # list = get_object_or_404()
    lists = Supplier.objects.all()
    return render(request, 'supplier_list.html', {'lists': lists, })


@login_required(login_url='/login/')
def stock_in_view(request):
    product_info = Product.objects.all()
    supplier_info = Supplier.objects.all()

    if request.method == "POST":
        stock_in_form = AddStockInForm(request.POST)
        if stock_in_form.is_valid():
            stock_in_form.stockin_date = timezone.now()
            p_name = stock_in_form.cleaned_data['product_info']
            p_price = stock_in_form.cleaned_data['product_price']
            p_unit = stock_in_form.cleaned_data['product_unit']
            try:
                ob = Stocks.objects.get(product_name=p_name)
                p_unit = p_unit + ob.product_unit
                Stocks.objects.filter(product_name=p_name).update(product_price=p_price, product_unit=p_unit)
            except Stocks.DoesNotExist:
                ob = Stocks(product_name=p_name, product_price=p_price, product_unit=p_unit)
                ob.save()
            stock_in_form.save()

            return redirect('/stock_in_list/')
        else:
            messages.error(request, 'All fields required')
    else:
        stock_in_form = AddStockInForm()
    '''return render(request, 'stock_in.html',
                  {'form': stock_in_form, 'product_info': product_info, 'supplier_info': supplier_info,
                   'group_info': group_info, 'company_info': company_info})'''
    return render(request, 'stock_in.html', {'form': stock_in_form, 'prduct_info':product_info, 'supplier_info':supplier_info})


@login_required(login_url='/login/')
def stock_in_list(request):
    lists = StockIn.objects.all()
    return render(request, 'stock_in_list.html', {'lists': lists, })


@login_required(login_url='/login/')
def stock_out_view(request):
    product_info = Stocks.objects.all()
    if request.method=="POST":
        stock_out_form = AddStockOutForm(request.POST)
        if stock_out_form.is_valid():
            stock_out_form.stockout_date = timezone.now()
            p_name = stock_out_form.cleaned_data['product_info']
            p_price = stock_out_form.cleaned_data['product_sell_price']
            p_unit = stock_out_form.cleaned_data['product_sell_unit']
            try:
                ob = Stocks.objects.get(product_name=p_name)
                p_unit = ob.product_unit - p_unit
                Stocks.objects.filter(product_name=p_name).update(product_price=ob.product_price, product_unit=p_unit)
            except Stocks.DoesNotExist:
                print('Something error!')

            stock_out_form.save()

            return redirect('/stock_out_list/')
        else:
            messages.error(request, 'All fields required')
    else:
        stock_out_form = AddStockOutForm()

    return render(request, 'stock_out.html',{'form': stock_out_form, 'product_info': product_info})


@login_required(login_url='/login/')
def stock_out_list(request):
    lists = StockOut.objects.all()
    return render(request, 'stock_out_list.html', {'lists': lists, })


@login_required(login_url='/login/')
def stock_view(request):
    lists = Stocks.objects.all()
    return render(request, 'stocks.html', {'lists': lists})


def mod_login_view(request):
    title = "Login"
    if request.method == 'POST':
        form = ModLoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/login/')
        else:
            messages.error(request, "Username or password invalid")
    else:
        form = ModLoginForm()
    return render(request, 'login.html', {'form': form, 'title': title})


@login_required(login_url='/login/')
def mod_logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')