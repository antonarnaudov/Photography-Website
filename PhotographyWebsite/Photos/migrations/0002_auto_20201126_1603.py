# Generated by Django 3.1.3 on 2020-11-26 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='')),
                ('category', models.CharField(max_length=80)),
            ],
        ),
        migrations.AlterField(
            model_name='photos',
            name='watermarked_photo',
            field=models.ImageField(blank=True, upload_to='public/photos'),
        ),
        migrations.AlterField(
            model_name='photos',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Photos.category'),
        ),
    ]