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
    title_about2 = models.CharField(max_length = 155, verbose_name = 'описания материала')
    description_about2 = RichTextField(
        verbose_name='Описание О нас 2'
    )
    description_about3 = RichTextField(
        verbose_name='Описание О нас 3'
    )
    description_about4 = RichTextField(
        verbose_name='Описание О нас 4'
    )
    images_about1 = models.ImageField(
        upload_to='settings',
        verbose_name='Фотка'
    )
    images_about2 = models.ImageField(
        upload_to='settings',
        verbose_name='Фотка'
    )
    images_about3 = models.ImageField(
        upload_to='settings',
        verbose_name='Фотка'
    )
    images_about4 = models.ImageField(
        upload_to='settings',
        verbose_name='Фотка'
    )
    images_about5 = models.ImageField(
        upload_to='settings',
        verbose_name='Фотка'
    )
    images_about6 = models.ImageField(
        upload_to='settings',
        verbose_name='Фотка'
    )
    images_about7 = models.ImageField(
        upload_to='settings',
        verbose_name='Фотка'
    )
    images_about8 = models.ImageField(
        upload_to='settings',
        verbose_name='Фотка'
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

class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name="ФИО преподавателя")
    photo = models.ImageField(upload_to='teachers/', verbose_name="Фото")
    bio_title = models.CharField(max_length=255, default="Кто преподает?", verbose_name="Заголовок")
    experience = models.CharField(max_length=255, verbose_name="Опыт работы")

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        return self.name


class Achievement(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='achievements', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, verbose_name="Достижение")

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"

    def __str__(self):
        return self.text

class AboutPage(models.Model):
    title_banner = models.CharField(
        max_length=155,
        verbose_name='Заголовка Баннера'
    )
    description_banner = RichTextField(
        verbose_name='Описание Баннера'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка О нас'
    )
    description = RichTextField(
        verbose_name='Описание о нас'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройки страницы о нас"
        verbose_name_plural = "Настройки страницы о нас"

class AboutObjects(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    description = RichTextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='about',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Данный'
        verbose_name_plural = 'Данные'

class AboutObjects2(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    description = RichTextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='about',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Данный 2'
        verbose_name_plural = 'Данные 2'


