from django.conf import settings
from django.db import models
from django.utils import timezone


class Postagem(models.Model):
    ptg_id_autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ptg_nm_postagem = models.CharField(max_length=200)
    ptg_ds_postagem = models.TextField()
    ptg_ts_criacao = models.DateTimeField(default=timezone.now)
    ptg_ts_alteracaco = models.DateTimeField(blank=True, null=True)

    class Meta:
            verbose_name = 'Postagem'
            verbose_name_plural = 'Postagens'

    def publicacao(self):
        self.ptg_ts_criacao = timezone.now()
        self.save()

    def __str__(self):
        return self.ptg_nm_postagem
