from django.urls import path

from store import views

urlpatterns = [
    path('brand/country/<str:nationality>', views.mobile_from_brands, name="mobile_with_brand_country"),
    path('brand/same', views.mobile_same_brands, name="get_same_brand_manufacture_country"),
    path('add', views.MobileStoreView.as_view(), name="add_mobile"),
    path('brand', views.GetMobileWithBrandView.as_view(), name="get_mobile_with_brand_name")

]
