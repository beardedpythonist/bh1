# Generated by Django 4.1.2 on 2023-02-22 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(default=0, verbose_name='номер ацдитории')),
                ('format_id', models.SmallIntegerField(default=0, verbose_name='номер ацдитории')),
            ],
            options={
                'verbose_name': 'аудитория',
                'verbose_name_plural': 'аудитории',
            },
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'группа', 'verbose_name_plural': 'группы'},
        ),
        migrations.AlterModelOptions(
            name='groupusers',
            options={'verbose_name': 'промежуточная таблица группа-юзер', 'verbose_name_plural': 'промежуточная таблица группа-юзер'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='group',
            name='mentor_id',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='group',
            name='audience_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lesson.audience', verbose_name='аудитория'),
        ),
    ]
