# Generated by Django 3.2.1 on 2021-06-19 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_admin', '0010_merge_20210607_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cost',
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('weight', models.CharField(max_length=512)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_admin.product')),
            ],
            options={
                'db_table': 'product_model',
            },
        ),
    ]
