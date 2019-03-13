# Generated by Django 2.0 on 2019-03-10 20:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Descripton', models.TextField()),
                ('Status', models.CharField(choices=[('PLANNING', 'Planning'), ('PLANNED', 'Planned'), ('INPROGRESS', 'Inprogress'), ('DONE', 'Done')], default='PLANNING', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Creator_name', models.CharField(max_length=120)),
                ('Team_Name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TeamCreater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_Name', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=120)),
                ('Permission', models.CharField(max_length=50)),
                ('Username', models.CharField(max_length=70)),
                ('Password', models.CharField(max_length=50)),
                ('ConfirmPassword', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='teamcreater',
            name='Users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TasKManager.Users'),
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(to='TasKManager.Users'),
        ),
        migrations.AddField(
            model_name='task',
            name='Assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TasKManager.Users'),
        ),
        migrations.AddField(
            model_name='task',
            name='Team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TasKManager.Team'),
        ),
    ]