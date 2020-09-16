# Generated by Django 3.0.5 on 2020-04-30 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sale', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
                ('site', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=100)),
                ('url_adress', models.CharField(max_length=500)),
                ('text', models.TextField()),
                ('img', models.ImageField(default='default.jpg', upload_to='action_img/detail/')),
                ('img_title', models.ImageField(default='default.jpg', upload_to='action_img/detail/')),
                ('type_sale', models.CharField(max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='action.Category')),
            ],
        ),
    ]