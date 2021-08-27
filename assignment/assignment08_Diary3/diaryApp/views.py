from django.shortcuts import render,get_object_or_404
from .models import Diary
from django.contrib import auth

# Create your views here.
def home(request):
    diaries = Diary.objects
    return render(request, 'diaryApp/home.html', {'diaries':diaries})

def detail(request, diary_id):
    diary_detail = get_object_or_404(Diary, pk=diary_id)
    return render(request, 'diaryApp/detail.html', {'diary':diary_detail, 'weekday':diary_detail.pub_date.weekday()})