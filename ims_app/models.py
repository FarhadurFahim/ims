from django.db import models
from django.utils import timezone
# Create your models here.


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=50)
    supplier_address = models.CharField(max_length=100)
    supplier_contact = models.CharField(max_length=40,null=False)
    supplier_email=models.EmailField()

    class Meta:
        db_table = 'supplier'

    def __str__(self):
        return self.supplier_name


class ProductCompany(models.Model):
    company_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'product_company'

    def __str__(self):
        return self.company_name


class ProductGroup(models.Model):
    group_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'product_group'

    def __str__(self):
        return self.group_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
    product_company = models.ForeignKey(ProductCompany, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.product_name


class StockIn(models.Model):
    product_info = models.ForeignKey(Product, null=True)
    # product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
    # product_company = models.ForeignKey(ProductCompany, on_delete=models.CASCADE)
    supplier_info = models.ForeignKey(Supplier)
    product_price = models.FloatField()
    product_unit = models.IntegerField()
    stockin_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'stock_in'

    def __str__(self):
        return '%s %s %s' %(self.product_info.product_name, self.product_info.product_company, self.product_price)


class Stocks(models.Model):
    # available_stock = models.ForeignKey(StockIn, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField()
    product_unit = models.IntegerField()

    class Meta:
        db_table = 'stocks'

    def __str__(self):
        return self.product_name


class StockOut(models.Model):
    product_info = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    product_sell_price = models.FloatField()
    product_sell_unit = models.IntegerField()
    stockout_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'stock_out'

    def __str__(self):
        return '%s %s' %(self.product_info.product_name, self.product_sell_price)
        # return '%s %s' (self.product_name, self.product_price)

