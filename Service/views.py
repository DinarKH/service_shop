from .models import City, Street, Shop
from .serializers import ShopSerializer, CitySerializer, StreetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime


# GET /city/
class List_cities(APIView):
    def get(self, request):
        serializer = CitySerializer(City.objects.all(), many=True)
        return Response(serializer.data)



# GET /city/<city_id>/street/
class City_street(APIView):
    def get(self, requset, city_id):
        city_name = City.objects.get(id=city_id).name
        list_obj = Street.objects.filter(city=city_id)
        serializer = StreetSerializer(list_obj, many=True)
        for item in serializer.data:
            item['city'] = city_name
        return Response(serializer.data)


class Shop_work(APIView):
    # GET /shop/?street=<street_id>&city=<city_id>&open=0/1
    def get(self, request):
        list_obj = Shop.objects.all()
        street_val = request.GET.get('street')
        city_val = request.GET.get('city')
        open = request.GET.get('open')
        if street_val is not None:
            try:
                street_val = int(street_val)
            except ValueError:
                return Response({'Errot': 'Value Error'}, status=status.HTTP_400_BAD_REQUEST)
            list_obj = list_obj.filter(street=street_val)
        if city_val is not None:
            try:
                city_val = int(city_val)
            except ValueError:
                return Response({'Errot': 'Value Error'}, status=status.HTTP_400_BAD_REQUEST)
            list_obj = list_obj.filter(city=city_val)
        if open is not None:
            if open == '0':
                list_obj = list_obj.filter(time_close__gt=datetime.datetime.now().time())
                list_obj = list_obj.filter(time_open__lt=datetime.datetime.now().time())
            elif open == '1':
                many_close = list_obj.exclude(time_close__gt=datetime.datetime.now().time())
                many_open = list_obj.exclude(time_open__lt=datetime.datetime.now().time())
                list_obj = many_close.union(many_open)
            else:
                return Response({'Errot': 'State Error'}, status=status.HTTP_400_BAD_REQUEST)
        serilizer = ShopSerializer(list_obj, many=True)
        for item in serilizer.data:
            item['city'] = City.objects.get(id=item['city']).name
            item['street'] = Street.objects.get(id=item['street']).name
        return Response(serilizer.data)

    # POST /shop/
    def post(self, request):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            el = Shop.objects.last().id
            return Response({"id": el})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
    Example
    {"name":"Gulliver",
    "city":1,
    "street":1,
    "home":21,
    "time_open":"08:00:00",
    "time_close":"20:00:00"}
    """