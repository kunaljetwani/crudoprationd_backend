"""
URL configuration for rest_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apis import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookings/', views.bookdetails.as_view()),
    path('products/', csrf_exempt(views.productdetails.as_view()),name="productdetails  "),
    # path('products/cat', csrf_exempt(views.AddCategory.as_view())),
    path('products/add', csrf_exempt(views.AddProducts.as_view()),name="AddProducts"),
    path('products/delete/<int:product_id>/',csrf_exempt(views.ProductsDelete.as_view()),name="ProductsDelete"),
    path('products/<int:product_id>/', views.productdetailsbyid.as_view(),name="productdetailsbyid"),
    path('products/update/<int:product_id>/', csrf_exempt(views.UpdateProduct.as_view()),name="UpdateProduct")

]
