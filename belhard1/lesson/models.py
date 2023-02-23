from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия')
    email = models.EmailField(max_length=64, unique=True, blank=False, verbose_name='емайл')
    password = models.CharField(max_length=128)
    payment = models.ForeignKey('Payment_info', blank=False, on_delete=models.PROTECT, verbose_name="статус оплаты")
    role = models.ForeignKey('Role', blank=False, on_delete=models.PROTECT, verbose_name="роль пользователя")
    feedback = models.ForeignKey('Feedback', blank=False, on_delete=models.PROTECT, verbose_name="отзыв")

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'


class GroupUsers(models.Model):
    user_id = models.ForeignKey('User', blank=False, on_delete=models.PROTECT, verbose_name="студент", default='Иванов')
    group_id = models.ForeignKey('Group', verbose_name='номер группы', on_delete=models.PROTECT, default=1)

    def __int__(self):
        return self.group_id

    class Meta:
        verbose_name_plural = 'Группа-юзер'
        verbose_name = 'группа-юзер'


class Group(models.Model):
    number = models.SmallIntegerField(default=0, verbose_name='номер группы')
    mentor_id = models.SmallIntegerField(default=0)
    date_start = models.DateField(blank=True, verbose_name='дата начала')
    audience = models.ForeignKey('Audience', on_delete=models.PROTECT, null=True, verbose_name="аудитория")
    course = models.ForeignKey('Course', on_delete=models.PROTECT, null=True, verbose_name="курс")


    class Meta:
        verbose_name_plural = 'группы'
        verbose_name = 'группа'

    def __int__(self):
        return self.number, self.audience


class Audience(models.Model):
    number = models.SmallIntegerField(default=0, verbose_name='номер аудитории')
    format = models.ForeignKey('Training_Format', on_delete=models.PROTECT, verbose_name=" формат обучения")

    def __int__(self):
        return self.number

    class Meta:
        verbose_name_plural = 'аудитории'
        verbose_name = 'аудитория'


class Training_Format(models.Model):
    is_online = models.BooleanField(default=True, verbose_name='онлайн обучение')

    def __bool__(self):
        return self.is_online

    class Meta:
        verbose_name_plural = 'формат обучения'
        verbose_name = 'формат обучения'


class Course(models.Model):
    duration = models.PositiveSmallIntegerField(default=0, verbose_name='продолжительность обучения')
    name = models.CharField(max_length=64, verbose_name='название курса', unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='стоимость')
    category = models.ForeignKey('Category', verbose_name='категория', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курсы'


class Payment_info(models.Model):
    first_paid_date = models.DateField(blank=True, verbose_name='дата 1-ой оплаты')
    first_paid_amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='сумма 1-ой оплаты')
    sec_paid_date = models.DateField(blank=True, verbose_name='дата 2-ой оплаты')
    sec_paid_amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='сумма 2-ой оплаты')

    class Meta:
        verbose_name_plural = 'статус оплаты'
        verbose_name = 'статус оплаты'


class Role(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name='роль пользователя', null=True, default='студент')

    class Meta:
        verbose_name_plural = 'статус пользователя'
        verbose_name = 'статус пользователя'
    def __str__(self):
        return self.name



class RolePermission(models.Model):
    role_id = models.ForeignKey('Role', blank=False, on_delete=models.PROTECT, verbose_name="статус пользователя")
    name = models.ForeignKey('Permission', blank=False, on_delete=models.PROTECT, verbose_name="права пользователя")

    class Meta:
        verbose_name_plural = 'роль-разрешение'
        verbose_name = 'роль-разрешение'


class Permission(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='права пользователя ', null=True, default='все права')

    class Meta:
        verbose_name_plural = 'разрешение'
        verbose_name = 'разрешение'
    def __str__(self):
        return self.name

class Lesson(models.Model):
    day = models.DateTimeField(verbose_name='дата и время урока')
    url = models.ForeignKey('LessonMaterial', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'урок'
        verbose_name = 'урок'

class LessonMaterial(models.Model):
    file = models.FileField(upload_to='#', storage=None, max_length=100,)
    url = models.URLField(max_length=200)

    class Meta:
        verbose_name_plural = 'учебные материалы'
        verbose_name = 'учебные материалы'

class Feedback(models.Model):
    text = models.TextField(max_length=350, verbose_name='отзыв')
    class Meta:
        verbose_name_plural = 'отзывы'
        verbose_name = 'отзывы'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'категория'
        verbose_name = 'категория'
