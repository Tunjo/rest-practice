# Generated by Django 2.1.5 on 2019-01-21 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appnew', '0002_item_storage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ClassesChar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.PositiveSmallIntegerField(choices=[(1, 'Warrior'), (2, 'Mage'), (3, 'Priest')])),
                ('char', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appnew.Character')),
            ],
        ),
    ]
