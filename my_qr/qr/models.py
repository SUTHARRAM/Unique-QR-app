from django.db import models
import qrcode 
from django.core.files import File
from PIL import Image, ImageDraw
from io import BytesIO

# Create your models here.
class Soap(models.Model):
    ''' Storing detail about soap'''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    qr_code = models.ImageField(upload_to='qrcode/', blank=True, null=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        qrcode_img = qrcode.make(str(self.id)+","+self.name+","+str(self.price))
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = 'qr_code-'+str(self.id)+'.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
       