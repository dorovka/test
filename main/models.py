from django.db import models
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Task(models.Model):
    title = models.CharField('Название товара', max_length = 50)
    task = models.TextField('Описание')
    Price = models.CharField('Цена(в рублях)', max_length = 50)
    image = models.ImageField(upload_to="images/", default=r'media\base\PL.png')
    image2 = models.ImageField(upload_to="images/", default=r'media\base\PL.png')
    image3 = models.ImageField(upload_to="images/", default=r'media\base\PL.png')
    image4 = models.ImageField(upload_to="images/", default=r'media\base\PL.png')
    image5 = models.ImageField(upload_to="images/", default=r'media\base\PL.png')




    #user = models.ForeignKey(to = User, null = True, on_delete=models.SET_NULL)
    #upload = models.FileField(upload_to=user_directory_path, null= True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

