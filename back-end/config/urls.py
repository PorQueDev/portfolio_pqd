
from django.contrib import admin
from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def teste_api(request):
    return Response({
        'mensagem': 'API funcionando corretamente!'
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/teste/', teste_api),
]
