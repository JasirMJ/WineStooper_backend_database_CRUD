from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from warehouse.models import tbl_wines, tbl_country, tbl_wine_colors
from warehouse.serializer import *

STATUS = "status"
MESSAGE = "message"

class WareHouseAPI(ListAPIView):
    serializer_class = WarehouseSerializer

    def get_queryset(self):
        qs = tbl_warehouse.objects.all()
        print("query set", qs)
        return qs

    def post(self, request):
        print("Post worked")
        try:

            instance = WarehouseSerializer(data=self.request.data, partial=True)
            instance.is_valid(raise_exception=True)
            instance.save()
            return Response({"status":True,"message":"data saved"})
        except Exception as e:
            return Response({"status": False, "message": str(e)})

    def put(self, request):
        print("Put worked")
        try:
            obj = tbl_warehouse.objects.filter(id=id).first()
            instance = WarehouseSerializer(obj=obj,data=self.request.data, partial=True)
            instance.is_valid(raise_exception=True)
            instance.save()
            return Response({"status":True,"message":"data Updated"})
        except Exception as e:
            return Response({"status": False, "message": str(e)})

class DistributionCenterAPI(ListAPIView):
    serializer_class = DistributionCentersSerializer

    def get_queryset(self):
        qs = tbl_distribution_centers.objects.all()
        print("query set", qs)
        return qs

    def post(self, request):
        print("Post worked")
        try:
            instance = DistributionCentersSerializer(data=self.request.data, partial=True)
            instance.is_valid(raise_exception=True)
            instance.save(warehouse=tbl_warehouse.objects.get(id=self.request.POST.get('warehouse')))
            return Response({"status":True,"message":"data saved"})
        except Exception as e:
            return Response({"status": False, "message": str(e)})

    def put(self, request):
        print("Put worked")
        try:
            id = self.request.POST.get('id')
            obj = tbl_distribution_centers.objects.filter(id=id).first()
            instance = DistributionCentersSerializer(obj = obj ,data=self.request.data, partial=True)
            instance.is_valid(raise_exception=True)
            instance.save()
            return Response({"status":True,"message":"data Updated"})
        except Exception as e:
            return Response({"status": False, "message": str(e)})

class CustomerAPI(ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        qs = tbl_customers.objects.all()
        print("query set", qs)
        return qs

    def post(self, request):
        print("Post worked")
        try:
            instance = CustomerSerializer(data=self.request.data, partial=True)
            instance.is_valid(raise_exception=True)
            instance.save()
            return Response({"status":True,"message":"data saved"})
        except Exception as e:
            return Response({"status": False, "message": str(e)})
    def put(self, request):
        print("Put worked")
        try:
            obj = tbl_customers.objects.filter(id=id).first()
            instance = CustomerSerializer(obj=obj,data=self.request.data, partial=True)
            instance.is_valid(raise_exception=True)
            instance.save()
            return Response({"status":True,"message":"data Updated"})
        except Exception as e:
            return Response({"status": False, "message": str(e)})

class OrderAPI(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        qs = tbl_orders.objects.all()
        print("query set", qs.query)
        # items = tbl_order_items.objects.filter(order=1)
        return qs

    def post(self, request):
        print("Post worked")
        try:
            instance = OrderSerializer(data=self.request.data, partial=True)
            instance.is_valid(raise_exception=True)
            instance.save(
                distribution_center = tbl_distribution_centers.objects.get(id=self.request.POST.get('distribution_center')),
                customer = tbl_customers.objects.get(id=self.request.POST.get('customer')),

            )
            return Response({"status":True,"message":"data saved"})
        except Exception as e:
            return Response({"status": False, "message": str(e)})

    def put(self, request):
        print("Put worked")
        try:
            obj = tbl_orders.objects.filter(id=id).first()
            instance = OrderSerializer(obj=obj,data=self.request.data, partial=True)
            instance.is_valid(raise_exception=True)
            instance.save()
            return Response({"status":True,"message":"data Updated"})
        except Exception as e:
            return Response({"status": False, "message": str(e)})

class OrderItemsAPI(ListAPIView):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        qs = tbl_order_items.objects.all()
        print("query set", qs)
        return qs

    def post(self, request):
        print("Post worked")
        try:
            w_obj = tbl_wines.objects.get(id=self.request.POST.get('wine'))
            instance = OrderItemSerializer(data=self.request.data, partial=True)
            instance.is_valid(raise_exception=True)
            instance.save(
                order=tbl_orders.objects.get(id=self.request.POST.get('order')),
                wine_id = w_obj.id,
                wine_name = w_obj.name,
            )
            return Response({"status":True,"message":"data saved"})
        except Exception as e:
            return Response({"status": False, "message": str(e)})
    def put(self, request):
        print("Put worked")
        try:
            obj = tbl_order_items.objects.filter(id=id).first()
            instance = OrderItemSerializer(obj=obj,data=self.request.data, partial=True)
            instance.is_valid(raise_exception=True)
            instance.save()
            return Response({"status":True,"message":"data Updated"})
        except Exception as e:
            return Response({"status": False, "message": str(e)})

class WineColorAPI(ListAPIView):
    serializer_class = WineColorSerializer

    def get_queryset(self):
        qs = tbl_wine_colors.objects.all()
        print("query set", qs)

        return qs

    def post(self, request):
        print("Post worked")
        try:
            instance = WineColorSerializer(data=self.request.data, partial=True)
            instance.is_valid(raise_exception=True)
            instance.save()
            return Response({"status":True,"message":"data saved"})
        except Exception as e:
            return Response({"status": False, "message": str(e)})
    def put(self, request):
        print("Put worked")
        try:
            obj = tbl_wine_colors.objects.filter(id=id).first()
            instance = WineColorSerializer(obj=obj,data=self.request.data, partial=True)
            instance.is_valid(raise_exception=True)
            instance.save()
            return Response({"status":True,"message":"data Updated"})
        except Exception as e:
            return Response({"status": False, "message": str(e)})

class WineCountryAPI(ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        qs = tbl_country.objects.all()
        print("query set", qs)
        return qs

    def post(self, request):
        print("Post worked")
        try:
            instance = CountrySerializer(data=self.request.data, partial=True)
            instance.is_valid(raise_exception=True)
            instance.save()
            return Response({"status": True, "message": "data saved"})
        except Exception as e:
            return Response({"status": False, "message": str(e)})
    def put(self, request):
        print("Put worked")
        try:
            obj = tbl_country.objects.filter(id=id).first()
            instance = CountrySerializer(obj=obj, data=self.request.data, partial=True)
            instance.is_valid(raise_exception=True)
            instance.save()
            return Response({"status": True, "message": "data Updated"})
        except Exception as e:
            return Response({"status": False, "message": str(e)})

class WineAPI(ListAPIView):
    serializer_class = WineSerializer

    def get_queryset(self):
        qs = tbl_wines.objects.all()
        print("query set", qs)
        qs =qs.filter(color__name="red")
        print("qs ",qs.query)
        return qs

    def post(self, request):
        print("Post worked")
        try:
            instance = WineSerializer(data=self.request.data, partial=True)
            instance.is_valid(raise_exception=True)
            instance.save()
            return Response({"status":True,"message":"data saved"})
        except Exception as e:
            return Response({"status": False, "message": str(e)})

    def put(self, request):
        print("Put worked")
        obj = tbl_wines.objects.filter(id=self.request.POST.get('id')).first()
        obj.color.add(tbl_wine_colors.objects.get(id=self.request.POST.get("color_id")))

        obj.country.add(tbl_country.objects.get(id=self.request.POST.get("country_id")))

        try:
            keyword = self.request.POST.get('keyword',"")
            print("obj ",obj)
            instance = WineSerializer(obj=obj,data=self.request.data, partial=True)
            instance.is_valid(raise_exception=True)
            obj = instance.save()
            print("Saved",obj)
            if keyword =="color":
                obj.color.add(tbl_wine_colors.objects.get(id=self.request.POST.get("color_id")))
                # return Response({"status": True, "message": "color Updated"})
                print("color updated")
            if keyword == "country":
                obj.color.add(tbl_country.objects.get(id=self.request.POST.get("country_id")))
                print("country updated")

                # return Response({"status": True, "message": "country Updated"})

            return Response({"status":True,"message":"data Updated"})
        except Exception as e:
            return Response({"status": False, "message": str(e)})
