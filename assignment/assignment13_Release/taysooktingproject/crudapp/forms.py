from django import forms
from django.forms import TextInput, NumberInput, Textarea
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['restaurant','food','rating','review','food_image']
        labels = {
            'restaurant' : '음식점',
            'food' : '음식',
            'rating':'별점',
            'review':'리뷰 내용',
            'food_image':'사진',
        }
        widgets = {
            'restaurant': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '리뷰할 음식점을 입력하세요',
            }),
            'food': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '리뷰할 메뉴 또는 음식 이름을 입력하세요',
            }),
            'rating': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '1~5 사이의 값을 입력하세요',
            }),
            'review': Textarea(attrs= {
                'class': 'form-control',
                'placeholder': '해당 음식이 어떠셨나요? :)',
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']