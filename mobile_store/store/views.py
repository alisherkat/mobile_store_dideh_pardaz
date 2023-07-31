from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Mobile
from store.forms import MobileForm
from store.serializers import MobileSerializers


def mobile_from_brands(request, nationality):
    mobiles = Mobile.objects.filter(brand__nationality=nationality)
    if not mobiles:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = MobileSerializers(mobiles, many=True)
        return JsonResponse(serializer.data, safe=False)


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
