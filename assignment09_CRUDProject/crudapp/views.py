from django.shortcuts import get_object_or_404, redirect, render
from .models import Review
from .forms import ReviewForm
from .models import Review

# Create your views here.
def home(request):
    reviews = Review.objects
    return render(request, 'crudapp/home.html', {'reviews':reviews})

def detail(request, review_id):
    review_detail = get_object_or_404(Review, pk=review_id)
    return render(request, 'crudapp/detail.html', {'review':review_detail})

def postcreate(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
        else:
            form = ReviewForm()
            return render(request, 'crudapp/new.html', {'form':form, 'error':'폼에 유효하지 않은 값이 있습니다.'})    
    else:
        form = ReviewForm()
        return render(request, 'crudapp/new.html', {'form':form})

def postupdate(request, review_id):
    post = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', review_id=post.pk)
        else:
            form = ReviewForm()
            return render(request, 'crudapp/edit.html', {'form':form, 'error':'폼에 유효하지 않은 값이 있습니다.'})    
    else:
        form = ReviewForm(instance=post)
        return render(request, 'crudapp/edit.html', {'form':form})

def postdelete(request, review_id):
    post = get_object_or_404(Review, pk=review_id)
    post.delete()
    return redirect('home')


