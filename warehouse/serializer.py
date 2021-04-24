from rest_framework import serializers

from warehouse.models import tbl_warehouse, tbl_distribution_centers, tbl_customers, tbl_orders, tbl_order_items, \
    tbl_wine_colors, tbl_country, tbl_wines


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_warehouse
        fields = "__all__"


class DistributionCentersSerializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer()

    class Meta:
        model = tbl_distribution_centers
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_customers
        fields = "__all__"

#
# class Order_OrderItemSerializer(serializers.ModelSerializer):
#
#
#     class Meta:
#         model = tbl_order_items
#         fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    distribution_center = DistributionCentersSerializer()
    # order_items = serializers.SerializerMethodField()
    # def get_order_items(self,obj):
    #     objs = tbl_order_items.objects.filter(order=obj.id)
    #     # serializer = OrderItemSerializer(objs)
    #     # return serializer.data
    #     data = []
    #     for x in objs:
    #         data.append({"id":x.id,"wine":x.wine_name,"quantity":x.qty,"frequency":x.frequency,"availablity":x.availablity})
    #     return data
    class Meta:
        model = tbl_orders
        fields = "__all__"



class OrderItemSerializer(serializers.ModelSerializer):


    class Meta:
        model = tbl_order_items
        fields = "__all__"



class WineColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_wine_colors
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_country
        fields = "__all__"


class WineSerializer(serializers.ModelSerializer):
    color = WineColorSerializer(many=True)
    country = CountrySerializer(many=True)

    class Meta:
        model = tbl_wines
        fields = "__all__"


