# Generated by Django 3.0.2 on 2020-01-31 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0003_auto_20200131_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictor',
            name='antibiotic',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
        migrations.AlterField(
            model_name='predictor',
            name='gender',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
        migrations.AlterField(
            model_name='predictor',
            name='immune',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
        migrations.AlterField(
            model_name='predictor',
            name='infection',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
        migrations.AlterField(
            model_name='predictor',
            name='location',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
        migrations.AlterField(
            model_name='predictor',
            name='pregnancy',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
        migrations.AlterField(
            model_name='predictor',
            name='resistance',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
    ]