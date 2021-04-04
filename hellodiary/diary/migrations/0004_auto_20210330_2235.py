# Generated by Django 3.1.5 on 2021-03-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20210329_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='diary',
            name='diary_entry',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='diary',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]