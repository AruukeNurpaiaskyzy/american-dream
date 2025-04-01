from django.db import models
from ckeditor.fields import RichTextField

class Settings(models.Model):
    title_banner = models.CharField(
        max_length=155,
        verbose_name='Заголовок Баннер'
    )
    description_banner = RichTextField(
        verbose_name='Описание Баннер'
    )
    title_about= models.CharField(
        max_length=155,
        verbose_name='Заголовок О нас'
    )
    image_about = models.ImageField(
        upload_to='settings',
        verbose_name='Фото'
    )
    description_about = RichTextField(
        verbose_name='Описание О нас 1'
    )
    title_about = models.CharField(max_length = 155, verbose_name = 'описания материала')
    description_about2 = RichTextField(
        verbose_name='Описание О нас 2'
    )
    description_about3 = RichTextField(
        verbose_name='Описание О нас 3'
    )
    description_about4 = RichTextField(
        verbose_name='Описание О нас 4'
    )
    popular_courses = models.CharField(
        max_length=155,
        verbose_name='Популярные курсы'
    )
    our_teachers = models.CharField(
        max_length=155,
        verbose_name='Наши преподы'
    )
    feedback = models.CharField(
        max_length=155,
        verbose_name='Заголоаок обратный связи'
    )
    feedback_description = RichTextField(
        verbose_name='Описание обратной связи '
    )

    def __str__(self):
        return self.title_banner

    class Meta:
        verbose_name_plural = 'Настрокий Главной Страницы'

class Contacts(models.Model):
    phone_numbers = RichTextField(verbose_name='номер телефона')
    email = models.CharField(verbose_name = 'почта', max_length=155)
    address = models.CharField(verbose_name = 'адрес', max_length=155)
    links_email = models.URLField(verbose_name='Ссылка на почту')
    links_address = models.URLField(verbose_name='Ссылка на адрес')

    class Meta:
        verbose_name_plural = 'Настрокий контакты'