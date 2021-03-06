# Generated by Django 2.2.7 on 2019-11-14 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aviao',
            options={'verbose_name': 'Avião', 'verbose_name_plural': 'Aviões'},
        ),
        migrations.AlterModelOptions(
            name='postotrabalho',
            options={'verbose_name': 'Posto de Trabalho', 'verbose_name_plural': 'Postos de Trabalho'},
        ),
        migrations.AlterModelOptions(
            name='produtopostotrabalho',
            options={'verbose_name': 'Posto de Trabalho', 'verbose_name_plural': 'Postos de Trabalho'},
        ),
        migrations.AlterField(
            model_name='aviao',
            name='numero',
            field=models.CharField(max_length=7, verbose_name='número'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='aviao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Aviao', verbose_name='avião'),
        ),
    ]
