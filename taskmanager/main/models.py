from django.db import models


class Task(models.Model):
    title = models.CharField('Назва', max_length=64)
    task = models.TextField('Опис')

class Orders(models.Model):
    P = models.CharField('Прізвище', max_length=16)
    I = models.CharField('Ім`я', max_length=16)
    B = models.CharField('По-батькові', max_length=16)
    email = models.CharField('Електронна пошта', max_length=32)
    phone = models.CharField('Мобільний телефон', max_length=12)
    zona = models.CharField('Фотозона', max_length=32)
    DodPoslugu = models.CharField('Додаткові послуги', max_length=64)
    Descrip = models.TextField('Опис')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачі'