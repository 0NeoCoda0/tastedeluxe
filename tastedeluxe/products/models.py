from django.db import models

class ProductCard(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(default='default.jpg', upload_to='product_images/')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    weight = models.FloatField(null=True, blank=True, verbose_name='Вес')
    caloryes = models.FloatField(null=True, blank=True, verbose_name='Калорийность')
    category = models.CharField(max_length=100, null=True, blank=True, verbose_name='Категория')
    food_type =  models.CharField(max_length=100, null=True, blank=True, verbose_name='Тип')

    class Meta:
        verbose_name_plural = 'Карточки товаров'
        verbose_name = 'карточка товара'

    def __str__(self) -> str:
        return self.name
