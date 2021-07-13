from django.shortcuts import get_object_or_404, redirect, render
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.
def home(request):
    reviews = Review.objects
    return render(request, 'crudapp/home.html', {'reviews':reviews})

def detail(request, review_id):
    review_detail = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review_detail
            comment.save()
            return redirect('detail', review_id=review_detail.pk)
        else:
            redirect('list')
    else:
        form = CommentForm()
        return render(request, 'crudapp/detail.html', {'form':form, 'review':review_detail})

def reviewcreate(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('home')
        else:
            form = ReviewForm()
            return render(request, 'crudapp/new.html', {'form':form, 'error':'폼에 유효하지 않은 값이 있습니다.'})    
    else:
        form = ReviewForm()
        return render(request, 'crudapp/new.html', {'form':form})

def reviewupdate(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('detail', review_id=review.pk)
        else:
            form = ReviewForm()
            return render(request, 'crudapp/edit.html', {'form':form, 'error':'폼에 유효하지 않은 값이 있습니다.'})    
    else:
        form = ReviewForm(instance=review)
        return render(request, 'crudapp/edit.html', {'form':form})

def reviewdelete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return redirect('home')

    
def commentupdate(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        edit_form = CommentForm(request.POST, instance=comment)
        if edit_form.is_valid():
            comment = edit_form.save(commit=False)
            comment.save()
            return redirect('detail', review_id=comment.review.pk)
    else:
        form = CommentForm()
        edit_form = CommentForm(instance=comment)
        return render(request, 'crudapp/detail.html', {'form':form, 'edit_form':edit_form, 'edit_form_id':comment_id, 'review':comment.review})

def commentdelete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    review_id = comment.review.pk
    comment.delete()
    return redirect('detail', review_id=review_id)


