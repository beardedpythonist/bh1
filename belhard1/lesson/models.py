from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=64, verbose_name= 'Имя')
    last_name = models.CharField(max_length=64, verbose_name= 'Фамилия')
    email = models.EmailField(max_length=64, unique=True, blank=False, verbose_name= 'емайл')
    password = models.CharField(max_length=128)
    user_id = models.ForeignKey('GroupUsers', blank=False, on_delete=models.PROTECT,verbose_name="ном пром груп")

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'


class GroupUsers(models.Model):
    user_id = models.IntegerField(verbose_name='юзер')
    group_id = models.ForeignKey('Group', verbose_name='номер группы', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'промежуточная таблица группа-юзер'
        verbose_name = 'промежуточная таблица группа-юзер'

class Group(models.Model):
    number = models.SmallIntegerField(default=0, verbose_name='номер группы')
    mentor_id = models.SmallIntegerField(default=0)
    date_start = models.DateField(blank=True, verbose_name='дата начала')
    audience = models.ForeignKey('Audience', on_delete=models.PROTECT, null=True, verbose_name="аудитория")
    course = models.ForeignKey('Course', on_delete=models.PROTECT, null=True, verbose_name="курс")

    class Meta:
        verbose_name_plural = 'группы'
        verbose_name = 'группа'

class Audience(models.Model):
    number =  models.SmallIntegerField(default=0, verbose_name='номер аудитории')
    format = models.ForeignKey('Training_Format', on_delete=models.PROTECT, verbose_name=" формат обучения")

    class Meta:
        verbose_name_plural = 'аудитории'
        verbose_name = 'аудитория'



class Training_Format(models.Model):
    is_online =  models.BooleanField(default=True, verbose_name='онлайн обучение')
    class Meta:
        verbose_name_plural = 'формат обучения'
        verbose_name = 'формат обучения'


class Course(models.Model):
    duration = models.PositiveSmallIntegerField(default=0, verbose_name='продолжительность обучения')
    name = models.CharField(max_length=64, verbose_name= 'название курса', unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='стоимость')

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курсы'



