# Generated by Django 3.1.3 on 2020-11-14 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StoryPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('uv', models.IntegerField(default=0)),
                ('dv', models.IntegerField(default=0)),
                ('writtenby', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='plotpoint',
            old_name='downvotes',
            new_name='dv',
        ),
        migrations.RenameField(
            model_name='plotpoint',
            old_name='upvotes',
            new_name='uv',
        ),
        migrations.CreateModel(
            name='Upvotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.plotpoint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.user')),
            ],
        ),
        migrations.CreateModel(
            name='Edits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_status', models.BooleanField(default=True)),
                ('plot_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.plotpoint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.user')),
            ],
        ),
        migrations.CreateModel(
            name='Downvotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.plotpoint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.user')),
            ],
        ),
        migrations.CreateModel(
            name='Choice_Upvotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.choice')),
                ('plot_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.plotpoint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.user')),
            ],
        ),
        migrations.CreateModel(
            name='Choice_Edits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_status', models.BooleanField(default=True)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.choice')),
                ('plot_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.plotpoint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.user')),
            ],
        ),
        migrations.CreateModel(
            name='Choice_Downvotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.choice')),
                ('plot_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.plotpoint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.user')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='plotpoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.plotpoint'),
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.plotpoint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoryPage.user')),
            ],
        ),
    ]
