from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from .models import Review, Comment, Scrap, Like
from django.contrib.auth import get_user_model
from .forms import ReviewForm, CommentForm

# Create your views here.
def home(request):
    reviews = Review.objects
    return render(request, 'crudapp/home.html', {'reviews':reviews})

def search(request):
    if request.method == "GET" and request.GET["keyword"]:
        keyword = request.GET["keyword"]
        reviews = Review.objects.filter(restaurant__contains=keyword) | Review.objects.filter(food__contains=keyword)
        return render(request, 'crudapp/home.html', {'reviews':reviews})
        
    reviews = Review.objects.all()
    return render(request, 'crudapp/home.html', {'reviews':reviews})

def myscrap(request):
    User = get_user_model()
    user = get_object_or_404(User, username=request.user)
    reviews = user.scrapped_review.all() #원래는 [소스모델]_set으로 사용하면 되지만, related_name을 지정해준 경우에는 그 값을 사용하면 됨
    return render(request, 'crudapp/myscrap.html', {'reviews':reviews})

def detail(request, review_id):
    review_detail = get_object_or_404(Review, pk=review_id)
    scrap = Scrap.objects.filter(user=request.user, review=review_detail)
    like = Like.objects.filter(user=request.user, review=review_detail)
    like_count = Like.objects.filter(review=review_detail).count

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
        return render(request, 'crudapp/detail.html', {'form':form, 'review':review_detail, 'scrap':scrap, 'like':like, 'like_count':like_count})

def reviewcreate(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
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

def scrap(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    scrapped = Scrap.objects.filter(user=request.user, review=review)
    if not scrapped:
        Scrap.objects.create(user=request.user, review=review) 
    else:
        scrapped.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def like(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    liked = Like.objects.filter(user=request.user, review=review)
    if not liked:
        Like.objects.create(user=request.user, review=review) 
    else:
        liked.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

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


