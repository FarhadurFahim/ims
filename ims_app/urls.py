from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_product_list, name='stock_in'),
    url(r'^add_company/$', views.add_company_view, name='add_company'),
    url(r'^company_list/$', views.view_company_list, name='company_list'),
    url(r'^add_group/$', views.add_group_view, name='add_group'),
    url(r'^group_list/$', views.view_group_list, name='group_list'),
    url(r'^add_product/$', views.add_product_view, name='add_product'),
    url(r'^product_list/$', views.view_product_list, name='company_list'),
    url(r'^add_supplier/$', views.add_supplier_view, name='add_supplier'),
    url(r'^supplier_list/$', views.view_supplier_list, name='supplier_list'),
    url(r'^stock_in/$', views.stock_in_view, name='stock_in'),
    url(r'^stock_in_list/$', views.stock_in_list, name='stock_in_list'),
    url(r'^stock_out/$', views.stock_out_view, name='stock_out'),
    url(r'^stock_out_list/$', views.stock_out_list, name='stock_out_list'),
    url(r'^stocks/$', views.stock_view, name='stocks'),
]