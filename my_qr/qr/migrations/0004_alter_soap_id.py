# Generated by Django 3.2a1 on 2021-02-19 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0003_alter_soap_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soap',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]