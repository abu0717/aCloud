from django.db import models

class UploadFile(models.Model):
    img = models.ImageField(upload_to='img-file/')
    folder = models.FileField(upload_to='folders/')

    def __str__(self):
        return self.folder

    class Meta:
        verbose_name = 'Folder'
        verbose_name_plural = 'Folders'