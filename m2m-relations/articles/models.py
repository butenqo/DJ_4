from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
    

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Scope(models.Model):
    tag = models.ForeignKey(Tag, null=True, on_delete=models.CASCADE, related_name='tags', verbose_name="Раздел")
    is_main = models.BooleanField(verbose_name="Основной?")
    articles = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    

    class Meta:
        verbose_name = 'Тематики статьи'
        verbose_name_plural = 'Тематики статьи'
        ordering = ['-is_main', 'tag']