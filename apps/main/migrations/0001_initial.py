# Generated by Django 4.2.6 on 2023-10-10 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название альбома')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='posters', verbose_name='логотип')),
            ],
            options={
                'verbose_name': 'альбом',
                'verbose_name_plural': 'альбомы',
            },
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('country', models.CharField(max_length=50, verbose_name='страна')),
            ],
            options={
                'verbose_name': 'группа',
                'verbose_name_plural': 'группы',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='жанр')),
            ],
            options={
                'verbose_name': 'жанр',
                'verbose_name_plural': 'жанры',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название песни')),
                ('audio_file', models.FileField(upload_to='songs/%Y/%m/%d/', verbose_name='аудио файл')),
                ('duration', models.PositiveSmallIntegerField(default=False, verbose_name='длительность трека')),
                ('is_favorite', models.BooleanField(default=False, verbose_name='избранное')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='main.album', verbose_name='альбом')),
                ('genre', models.ManyToManyField(to='main.genre', verbose_name='жанр')),
            ],
            options={
                'verbose_name': 'песня',
                'verbose_name_plural': 'песни',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='', max_length=50, verbose_name='псевдоним')),
                ('band', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.band', verbose_name='группа')),
            ],
            options={
                'verbose_name': 'музыкант',
                'verbose_name_plural': 'музыканты',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.band', verbose_name='группа'),
        ),
    ]
