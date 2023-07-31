from django.urls import path

from store import views

urlpatterns = [
    path('brand/country/<str:nationality>', views.mobile_from_brands),
    path('add', views.MobileStoreView.as_view(), name="add_mobile"),
    path('brand', views.GetMobileWithBrandView.as_view(), name="get_mobile_with_brand_name")

]
