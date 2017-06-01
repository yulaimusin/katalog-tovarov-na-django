from django.db import models
from django.core.urlresolvers import reverse


# Модель категории
class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Заголовок')
    slug = models.SlugField(db_index=True, unique=True, verbose_name='ЧПУ категории')

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_category_url(self):
        return reverse('market:list', kwargs={'category_slug': self.slug})


# Модель продукта
class Product(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    category = models.ForeignKey(Category, verbose_name='Категория')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='ЧПУ товара')
    image = models.ImageField(upload_to='products/%m.%Y/', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    in_stock = models.IntegerField(default=0, db_index=True, verbose_name='Кол-во в наличии')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Товар добавлен')
    updated = models.DateTimeField(auto_now=True, verbose_name='Товар обновлен')

    class Meta:
        ordering = ['id']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.title

    def get_product_url(self):
        return reverse('market:details', kwargs={'category_slug': self.category.slug, 'product_id': self.id,
                                                 'product_slug': self.slug})