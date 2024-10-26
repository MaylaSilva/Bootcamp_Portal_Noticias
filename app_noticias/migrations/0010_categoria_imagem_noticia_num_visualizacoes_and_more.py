# Generated by Django 5.1.1 on 2024-10-25 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_noticias', '0009_alter_noticia_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='noticia',
            name='num_visualizacoes',
            field=models.IntegerField(default=0, editable=False, verbose_name='Número de visualizações'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='slug',
            field=models.SlugField(editable=False, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='noticia',
            name='subtitulo',
            field=models.CharField(max_length=300, null=True, verbose_name='Subtítulo'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Título'),
        ),
    ]