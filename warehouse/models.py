from django.db import models


# Create your models here.


class tbl_warehouse(models.Model):
    region_name = models.CharField(max_length=20)
    stock_cases = models.PositiveIntegerField()
    stock_bottles = models.PositiveIntegerField()
    next_arrival_date = models.DateTimeField()
    address = models.CharField(max_length=200)


class tbl_distribution_centers(models.Model):
    center_name = models.CharField(max_length=20)
    warehouse = models.ForeignKey(tbl_warehouse, on_delete=models.CASCADE)
    stock_cases = models.PositiveIntegerField()
    stock_bottles = models.PositiveIntegerField()
    next_arrival_date = models.DateTimeField()
    address = models.CharField(max_length=200)


class tbl_customers(models.Model):
    first_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class tbl_shopping_bucket(models.Model):
    distribution_center = models.ForeignKey(tbl_distribution_centers, on_delete=models.CASCADE)
    customer = models.ForeignKey(tbl_customers, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivery_charge = models.FloatField()


class tbl_shopping_list(models.Model):
    distribution_center = models.ForeignKey(tbl_distribution_centers, on_delete=models.CASCADE)
    customer = models.ForeignKey(tbl_customers, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivery_charge = models.FloatField()

class tbl_orders(models.Model):
    distribution_center = models.ForeignKey(tbl_distribution_centers, on_delete=models.CASCADE)
    customer = models.ForeignKey(tbl_customers, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivery_charge = models.FloatField()

class tbl_order_items(models.Model):
    order = models.ForeignKey(tbl_orders, on_delete=models.CASCADE)
    bucket = models.ForeignKey(tbl_shopping_bucket, on_delete=models.CASCADE,null=True)
    list = models.ForeignKey(tbl_shopping_list, on_delete=models.CASCADE,null=True)
    frequency = models.CharField(max_length=120,null=True)
    wine_id = models.CharField(max_length=120)
    wine_name = models.CharField(max_length=120)
    qty = models.PositiveIntegerField()
    price = models.FloatField()
    discount_in_perc = models.CharField(max_length=20)
    case = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField()
    availablity = models.CharField(max_length=100,default="In stock")

class tbl_wine_colors(models.Model):
    name = models.CharField(max_length=20)


class tbl_country(models.Model):
    name = models.CharField(max_length=20)


class tbl_wines(models.Model):
    name = models.CharField(max_length=200)
    color = models.ManyToManyField(tbl_wine_colors)
    country = models.ManyToManyField(tbl_country)
    description = models.CharField(max_length=120)
    bottle_size = models.IntegerField()
    case_capacity = models.IntegerField()
    case_cost = models.FloatField()
    bottle_cost = models.FloatField()
    indicator = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
