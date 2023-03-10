# Generated by Django 4.1.7 on 2023-02-23 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(default=0, verbose_name='номер аудитории')),
            ],
            options={
                'verbose_name': 'аудитория',
                'verbose_name_plural': 'аудитории',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='категория')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категория',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveSmallIntegerField(default=0, verbose_name='продолжительность обучения')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='название курса')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='стоимость')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lesson.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Курсы',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=350, verbose_name='отзыв')),
            ],
            options={
                'verbose_name': 'отзывы',
                'verbose_name_plural': 'отзывы',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(default=0, verbose_name='номер группы')),
                ('mentor_id', models.SmallIntegerField(default=0)),
                ('date_start', models.DateField(blank=True, verbose_name='дата начала')),
                ('audience', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lesson.audience', verbose_name='аудитория')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lesson.course', verbose_name='курс')),
            ],
            options={
                'verbose_name': 'группа',
                'verbose_name_plural': 'группы',
            },
        ),
        migrations.CreateModel(
            name='GroupUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lesson.group', verbose_name='номер группы')),
            ],
            options={
                'verbose_name': 'группа-юзер',
                'verbose_name_plural': 'руппа-юзер',
            },
        ),
        migrations.CreateModel(
            name='LessonMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='#')),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'учебные материалы',
                'verbose_name_plural': 'учебные материалы',
            },
        ),
        migrations.CreateModel(
            name='Payment_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_paid_date', models.DateField(blank=True, verbose_name='дата 1-ой оплаты')),
                ('first_paid_amount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='сумма 1-ой оплаты')),
                ('sec_paid_date', models.DateField(blank=True, verbose_name='дата 2-ой оплаты')),
                ('sec_paid_amount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='сумма 2-ой оплаты')),
            ],
            options={
                'verbose_name': 'статус оплаты',
                'verbose_name_plural': 'статус оплаты',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='все права', max_length=10, null=True, unique=True, verbose_name='права пользователя ')),
            ],
            options={
                'verbose_name': 'разрешение',
                'verbose_name_plural': 'разрешение',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='студент', max_length=10, null=True, unique=True, verbose_name='роль пользователя')),
            ],
            options={
                'verbose_name': 'статус пользователя',
                'verbose_name_plural': 'статус пользователя',
            },
        ),
        migrations.CreateModel(
            name='Training_Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_online', models.BooleanField(default=True, verbose_name='онлайн обучение')),
            ],
            options={
                'verbose_name': 'формат обучения',
                'verbose_name_plural': 'формат обучения',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=64, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=64, unique=True, verbose_name='емайл')),
                ('password', models.CharField(max_length=128)),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lesson.feedback', verbose_name='отзыв')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lesson.payment_info', verbose_name='статус оплаты')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lesson.role', verbose_name='роль пользователя')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lesson.groupusers', verbose_name='ном пром груп')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lesson.permission', verbose_name='права пользователя')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lesson.role', verbose_name='статус пользователя')),
            ],
            options={
                'verbose_name': 'роль-разрешение',
                'verbose_name_plural': 'роль-разрешение',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField(verbose_name='дата и время урока')),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lesson.lessonmaterial')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'урок',
            },
        ),
        migrations.AddField(
            model_name='groupusers',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lesson.user', verbose_name='студент'),
        ),
        migrations.AddField(
            model_name='audience',
            name='format',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lesson.training_format', verbose_name=' формат обучения'),
        ),
    ]
