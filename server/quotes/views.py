from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import DailyQuote
from .serializers import DailyQuoteSerializer
from .services.ai_generator import gerar_frase_diaria

class TodayQuoteView(APIView):
  def get(self, request):
    today = date.today()
    
    # Tenta buscar a frase criada hoje no banco de dados
    quote_obj = DailyQuote.objects.filter(created_at=today).first()

    # Se ainda não existe frase para hoje, chama a IA
    if not quote_obj:
      try:
        texto_gerado = gerar_frase_diaria()
        quote_obj = DailyQuote.objects.create(quote=texto_gerado)
      except Exception as e:
        return Response(
          {"error": f"Erro ao gerar frase com a IA: {str(e)}"},
          status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    serializer = DailyQuoteSerializer(quote_obj)
    return Response(serializer.data, status=status.HTTP_200_OK)