from datetime import datetime, timedelta
from django.db import models
class Member(models.Model):
    GENDER_CHOICES = [
        ('M', 'ذكر'),
        ('F', 'انثي'),
    ]
    CONTRACT_CHOICES = [
        ('monthly', 'شهري'),
        ('yearly', 'سنوي'),
        ('half-month', 'نصف شهري'),
    ]

    name = models.CharField(max_length=50, verbose_name='الاسم')
    contact = models.CharField(max_length=11, help_text='ادخل رقم الهاتف المكون من 11 رقم', verbose_name='رقم الهاتف')
    age = models.CharField(max_length=40, verbose_name='العمر')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M', verbose_name='الجنس')
    plan = models.CharField(max_length=50, verbose_name='الخطة')
    join_date =models.DateField(default=datetime.now , verbose_name='تاريخ الانضمام')
    expire_date = models.DateField(default=datetime.now() + timedelta(days=30) ,  verbose_name='تاريخ الانتهاء')
    initial_amount = models.CharField(max_length=10, default='200', verbose_name='المبلغ الابتدائي')
    contract_type = models.CharField(max_length=10, choices=CONTRACT_CHOICES, default='monthly', verbose_name='نوع العقد')
    
    class Meta:
        verbose_name = 'العضو'
        verbose_name_plural = 'الأعضاء'

    def __str__(self):
        return self.name