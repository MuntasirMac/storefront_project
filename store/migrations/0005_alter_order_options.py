# Generated by Django 4.1.2 on 2022-10-20 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_customer_options_remove_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancel_order', 'Can cancel order')]},
        ),
    ]