# Generated by Django 2.2.6 on 2019-10-13 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaAguas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'categoria_aguas',
            },
        ),
        migrations.CreateModel(
            name='Agua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('imagem', models.CharField(max_length=200)),
                ('descricao', models.TextField(blank=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estoque', models.PositiveIntegerField()),
                ('disponivel', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='agua', to='produto.CategoriaAguas')),
            ],
            options={
                'db_table': 'agua',
            },
        ),
    ]