# Generated by Django 4.2.3 on 2023-07-19 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_marca', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('preco', models.FloatField()),
                ('img', models.ImageField(upload_to='imagens')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venda.marca')),
            ],
        ),
    ]
