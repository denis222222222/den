from django.db import models
from django.contrib import admin


class Advertisements(models.Model):
    class Meta: 
        db_table = 'advertisements'
    def __str__(self): 
        return 'advertisements'
    title = models.CharField('Заголвок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте если умечтен торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime('%d:%m:%Y в %H:%M:%S')
    

'''class Advertisement(models.Model): 

    def __str__(self): 
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'''

