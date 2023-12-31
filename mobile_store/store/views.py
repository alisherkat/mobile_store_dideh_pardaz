from django.db.models import F
from django.http import JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Mobile
from store.forms import MobileForm
from store.serializers import MobileSerializers


def mobile_from_brands(request, nationality):
    mobiles = Mobile.objects.filter(brand__nationality__iexact=nationality)
    if not mobiles:
        return JsonResponse(f"mobile with this brand nationality ({nationality}) not found", safe=False)

    if request.method == "GET":
        serializer = MobileSerializers(mobiles, many=True)
        return JsonResponse(serializer.data, safe=False)


def mobile_same_brands(request):
    mobiles = Mobile.objects.filter(country__iexact=F("brand__nationality"))
    if not mobiles:
        return JsonResponse("Not Found", safe=False)

    if request.method == "GET":
        serializer = MobileSerializers(mobiles, many=True)

        j = JsonResponse(serializer.data, safe=False)
        return j


class MobileStoreView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'create_mobile_store.html'

    def get(self, request):
        form = MobileForm()
        return Response({'form': form})

    def post(self, request):
        form = MobileForm(request.POST)
        if not form.is_valid():
            return Response({'form': form})
        mobile = form.save()
        serializer = MobileSerializers(mobile)
        return JsonResponse(serializer.data, safe=False)


class GetMobileWithBrandView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'get_mobile_with_brand.html'

    def get(self, request):
        return Response()

    def post(self, request):
        brand_name = request.POST.get('brand')

        mobiles = Mobile.objects.filter(brand__name__iexact=brand_name)
        if mobiles:
            serializer = MobileSerializers(mobiles, many=True)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(f"mobile with this brand ({brand_name}) not found", safe=False)
