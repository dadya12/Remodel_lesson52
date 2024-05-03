from django.db import models

from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Tasks(models.Model):
    description = models.TextField(max_length=2000, verbose_name='Описание')
    status = models.CharField(default='new', choices=status_choices, verbose_name='Статус', max_length=200)
    date_done = models.DateField(verbose_name='Дата окончания', null=True, blank=True, default='')

    def __str__(self):
        return f'{self.description} {self.status}'
