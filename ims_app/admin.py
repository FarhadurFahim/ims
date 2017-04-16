from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'supplier_address', 'supplier_contact', 'supplier_email')
    list_display_links = ('supplier_name',)
    list_filter = ('supplier_address',)
    search_fields = ('supplier_name', 'supplier_address', 'supplier_contact')
    list_per_page = 20


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name',)
    list_display_links = ('company_name',)
    list_filter = ('company_name',)
    search_fields = ('company_name',)
    list_per_page = 20


class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name',)
    list_display_links = ('group_name',)
    list_filter = ('group_name',)
    search_fields = ('group_name',)
    list_per_page = 20


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_group', 'product_company')
    list_display_links = ('product_name',)
    list_filter = ('product_name', 'product_group', 'product_company')
    search_fields = ('product_name', 'product_group', 'product_company')
    list_per_page = 20


class StockInAdmin(admin.ModelAdmin):
    model = StockIn
    list_display = ('get_name', 'get_sup_name', 'product_price', 'product_unit', 'stockin_date')
    list_display_links = ('get_name',)
    list_filter = ('product_info', 'supplier_info' ,'stockin_date')
    search_fields = ('get_name', 'get_sup_name', 'stockin_date')
    list_per_page = 20
    date_hierarchy = 'stockin_date'

    def get_name(self, obj):
        return obj.product_info.product_name

    def get_sup_name(self, obj):
        return obj.supplier_info.supplier_name
    get_name.admin_order_field = 'supplier_name'
    get_name.short_description = 'Product Name'
    get_sup_name.short_description = 'Supplier Name'


class StockOutAdmin(admin.ModelAdmin):
    model = StockOut
    list_display = ('get_p_name', 'get_b_price', 'product_sell_price', 'get_a_unit', 'product_sell_unit', 'stockout_date')
    list_display_links = ('get_p_name',)
    list_filter = ('product_info','stockout_date')
    search_fields = ('get_p_name', 'stockout_date')
    list_per_page = 20
    date_hierarchy = 'stockout_date'

    def get_p_name(self, obj):
        return obj.product_info.product_name

    def get_b_price(self, obj):
        return obj.product_info.product_price

    def get_a_unit(self, obj):
        return obj.product_info.product_unit

    def get_sup_name(self, obj):
        return obj.supplier_info.supplier_name
    # get_name.admin_order_field = 'supplier_name'
    get_p_name.short_description = 'Product Name'
    get_b_price.short_description = 'Buying price'
    get_a_unit.short_description = 'Available unit'


class StockAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'product_unit')
    list_display_links = ('product_name',)
    search_fields = ('product_name',)
    list_per_page = 20

admin.site.register(ProductCompany, CompanyAdmin)
admin.site.register(ProductGroup, GroupAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(StockIn, StockInAdmin)
admin.site.register(StockOut, StockOutAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Stocks, StockAdmin)

admin.site.unregister(Group)