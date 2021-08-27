from django.db import models
import datetime

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField(null=True)
    img = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title

    #body 내용 중 100글자만 반환
    def summary(self):
        return self.body[:100]

    #게시글 시간을 계산해서 요일로 반환
    def weekday(self):
        weekday = ['월','화','수','목','금','토','일']
        time_difference = self.pub_date + datetime.timedelta(hours=9)   #시차 계산
        return weekday[time_difference.weekday()]
        