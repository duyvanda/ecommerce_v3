# Generated by Django 3.2.6 on 2021-08-05 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_order_orderitem_review_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
