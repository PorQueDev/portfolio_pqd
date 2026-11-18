from decouple import config
from google import genai

def gerar_frase_diaria():
	api_key = config('GEMINI_API_KEY')
	client = genai.Client(api_key=api_key)
	
	# Modelo atualizado e ativo recomendados pela Google
	response = client.models.generate_content(
		model='gemini-3.8-flash',
		contents='Gere uma frase motivacional curta sobre programação e tecnologia para o meu portfólio. Retorne apenas o texto da frase.',
	)
	
	return response.text.strip()