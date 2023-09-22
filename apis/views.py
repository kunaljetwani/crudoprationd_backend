
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from django.views import View
from .models import *

from apis.models import product
from .data import *
from .serializers import productserializer
import json

# Create your views here.


class bookdetails (View):
    def get(self, request):
        return JsonResponse(book, safe=False)

# gettings all the products


class productdetails(View):
    def get(self, request):
        details = product.objects.all()
        serializer = productserializer(details, many=True).data
        return JsonResponse(serializer, safe=False)

# adding all the products


class AddProducts(View):
    def post(self, request):
        add_product = json.loads(request.body)
        print(add_product)
        serilzer = productserializer(data=add_product)
        try:
            if serilzer.is_valid():
                serilzer.save()
                return JsonResponse(serilzer.data, status=200)
            return JsonResponse(serilzer.errors, status=400)
        except json.JSONDecodeError as e:
            return HttpResponseBadRequest("Invalid JSON data")


class UpdateProduct(View):
    def put(self, request, product_id):
        try:
            prod = product.objects.get(product_id=product_id)
            Update_data = json.loads(request.body)
            print(Update_data)

            serializer = productserializer(
                prod, data=Update_data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
        except product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "Invalid JSON data" + str(e)}, status=400)
# class AddCategory(View):
#     def get(self, request):
#         details = Category.objects.all()
#         serializer = Categoryerializer(details, many=True).data
#         return JsonResponse(serializer, safe=False)

#     def post(self, request):
#         add_Cat = json.loads(request.body)
#         try:
#             Category.objects.create(**add_Cat)
#             return JsonResponse(add_Cat, status=200)
#         except Exception as e:
#             return HttpResponseBadRequest(str(e))

# products by id


class productdetailsbyid(View):
    def get(self, request, product_id):
        try:
            products = product.objects.get(product_id=product_id)
            serializer = productserializer(products).data
            return JsonResponse(serializer, status=200)
        except:
            return JsonResponse({"mesg": "product not found"}, status=404)


# delete products
class ProductsDelete(View):
    def delete(self, request, product_id):
        try:
            products = product.objects.get(product_id=product_id)
            products.delete()
            return JsonResponse({"mesg": "product deleted sucessfuly"})
        except:
            JsonResponse({"mesg": "error somethin in deleting"})


# get is for single data
# all is for all the collections in database and
# filter is to get filtered from the collections
