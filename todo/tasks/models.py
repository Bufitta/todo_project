from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

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

    title = models.CharField(max_length=255)
    deadline = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    done = models.BooleanField(default=False)
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default=LOW)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')

    class Meta:
        ordering = ['-deadline', 'done']
        # unique_together = ['title', 'category']
        # verbose_name = 'Задача'
        # verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'Задача {self.title}'
