from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'Категория {self.title}'


class Task(models.Model):
    LOW = 'LW'
    MIDDLE = 'MD'
    HIGH = 'HG'

    PRIORITY_CHOICES = [
        (LOW, 'Низкий'),
        (MIDDLE, 'Средний'),
        (HIGH, 'Высокий')
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    deadline = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False)
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default=LOW)
    attachment = models.FileField(upload_to='uploads/', verbose_name='Вложение', null=True, blank=True)

    class Meta:
        ordering = ['-deadline', 'done']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'Задача {self.title}'
