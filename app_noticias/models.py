'''
MODELS app_noticias
'''
from datetime import datetime
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from .util.tempo_util import calcular_tempo_decorrido


class Categoria(models.Model):
    '''
    Categoria
    '''
    nome = models.CharField('Categoria', max_length=30, unique=True)
    imagem = models.ImageField(upload_to='', blank=True, null=True)
    criado_em = models.DateField(auto_now_add=True)
    def __str__(self):
        '''
        str
        '''
        return str(self.nome)

class Noticia(models.Model):
    '''
    Noticia
    '''
    titulo = models.CharField('Título', max_length=100, unique=True,  null=True)
    slug = models.SlugField(max_length=100, editable=False, unique=True, null=True)
    subtitulo = models.CharField('Subtítulo', max_length=300, null=True )
    conteudo= models.TextField('Conteúdo', max_length=3000)
    criada_em = models.DateTimeField('Criada em', help_text='dd/mm/yyyy hh:MM', auto_now_add=True)
    atualizada_em = models.DateTimeField('Atualizada', help_text='dd/mm/yyyy hh:MM', auto_now_add=True)
    imagem = models.ImageField(upload_to='', blank=True)
    autor = models.ForeignKey(User, on_delete=models.RESTRICT, editable=False)
    categoria = models.ManyToManyField(Categoria)
    publicada_em = models.DateTimeField('Publicada em', help_text='dd/mm/yyyy hh:MM', null=True, editable=False)
    publicada = models.BooleanField('Publicada', default=False)
    num_visualizacoes = models.IntegerField(default=0, verbose_name='Número de visualizações', editable=False)
    fonte_informacao = models.CharField('Fonte', max_length=400, null=True )

    def _calcular_tempo_da_atualizacao(self) -> str:
        '''
        Calculo do tempo de atualização da notícia:
        '''
        return calcular_tempo_decorrido(self.atualizada_em)

    atualizacao_tempo = property(_calcular_tempo_da_atualizacao)

    def _calcular_tempo_da_publicacao(self) -> str:
        '''
        Calculo do tempo de publicação da notícia:
        '''
        return calcular_tempo_decorrido(self.publicada_em)

    publicacao_tempo = property(_calcular_tempo_da_publicacao)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        if self.publicada and not self.publicada_em:
            self.publicada_em = datetime.now()
        elif not self.publicada and self.publicada_em:
            self.publicada_em = None
        return super().save(*args, **kwargs)

    class Meta:
        '''
        Metamodelo
        '''
        db_table = 'noticias'
        permissions = [
            ("pode_publicar", "Permissão atribuida à Editores para a publicação da Notícia"),
        ]
    
    def __str__(self):
        '''
        str
        '''
        if self.publicada:
            return  f"Título: {str(self.titulo)} - PUBLICADA"
        return f"Título: {str(self.titulo)}"

