from django import forms
from .models import StockIn, StockOut, ProductCompany, ProductGroup, Product, Supplier


class AddCompanyForm(forms.ModelForm):
    # company_name = forms.CharField(max_length=100)

    class Meta:
        model = ProductCompany
        fields = ('company_name',)


class AddGroupForm(forms.ModelForm):
    # company_name = forms.CharField(max_length=100)

    class Meta:
        model = ProductGroup
        fields = ('group_name',)


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_group', 'product_company')


class AddSupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('supplier_name', 'supplier_address', 'supplier_contact','supplier_email')


class AddStockInForm(forms.ModelForm):
    class Meta:
        model = StockIn
        fields = ('product_info', 'supplier_info', 'product_price', 'product_unit')
        labels = {'product_info': ('Product name'), 'supplier_info': ('Supplier name')}


class AddStockOutForm(forms.ModelForm):
    class Meta:
        model = StockOut
        fields = ('product_info', 'product_sell_price', 'product_sell_unit')
        labels = {'product_info': 'Product name', 'product_sell_price':'Product Sell Price',
                  'product_sell_unit':'Product Sell Unit'}


class ModLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)