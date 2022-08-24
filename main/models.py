from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone
from django.contrib.postgres.fields import ArrayField

class Task(models.Model):
    STATUSES = (
        ('N', 'Новая'),
        ('P', 'Запланированная'),
        ('I', 'В процессе'),
        ('R', 'Завершенная')
    )

    owner = models.IntegerField(default=0)
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    status = models.CharField('Статус', max_length=50, choices=STATUSES, default="N")
    creationTime = models.DateTimeField('Время создания', default=django.utils.timezone.now)
    finalTime = models.DateTimeField('Время завершения', default=django.utils.timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"