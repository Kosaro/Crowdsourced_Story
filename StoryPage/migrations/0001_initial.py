# Generated by Django 3.1.3 on 2020-11-14 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlotPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pptext', models.CharField(max_length=1000)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('isEnd', models.BooleanField(default=False)),
                ('writtenby', models.CharField(max_length=50)),
            ],
        ),
    ]