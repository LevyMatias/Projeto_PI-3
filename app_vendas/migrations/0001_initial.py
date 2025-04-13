from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id_venda', models.AutoField(primary_key=True, serialize=False)),
                ('produto_venda', models.TextField(max_length=255)),
                ('valor_venda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_venda', models.DateTimeField(auto_now=True)),
                ('quantidade_venda', models.IntegerField(max_length=4)),
            ],
        ),
    ]
