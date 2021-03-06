# Generated by Django 3.2 on 2021-04-28 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_person'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person', 'verbose_name_plural': 'People'},
        ),
        migrations.CreateModel(
            name='PersonMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('actor', 'Actor'), ('director', 'Director')], default='actor', max_length=30)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_movies', to='backend.movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_movies', to='backend.person')),
            ],
        ),
    ]
