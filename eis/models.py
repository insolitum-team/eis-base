from django.db import models


class Article(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    subtitle = models.TextField(verbose_name="Подзаголовок")
    slug = models.CharField(verbose_name="Слаг", max_length=255, unique=True, db_index=True)
    body = models.TextField(verbose_name="Оснновной текст")
    image_url = models.URLField(verbose_name="Ссылка на изображение", blank=False)
    time_created = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    time_update = models.DateTimeField(verbose_name="Время обновления", auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass

    class Meta:
        verbose_name = "Статьи"
        verbose_name_plural = "Статьи"
        ordering = ["time_created"]
