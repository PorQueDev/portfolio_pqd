from django.db import models

class DailyQuote(models.Model):
  quote = models.TextField(verbose_name="Frase")
  created_at = models.DateField(auto_now_add=True, unique=True, verbose_name="Data de Criação")

  def __str__(self):
    return f"Frase de {self.created_at}"