from django.urls import path
from .import views

urlpatterns = [
    path('search', views.search, name="search"),
    path('myscrap', views.myscrap, name="myscrap"),
    path('detail/<int:review_id>', views.detail, name="detail"),
    path('new/', views.reviewcreate, name="reviewcreate"),
    path('edit/<int:review_id>', views.reviewupdate, name="reviewupdate"),
    path('delete/<int:review_id>', views.reviewdelete, name="reviewdelete"),
    path('scrap/<int:review_id>', views.scrap, name="scrap"),
    path('like/<int:review_id>', views.like, name="like"),
    path('commentupdate/<int:comment_id>', views.commentupdate, name="commentupdate"),
    path('commentdelete/<int:comment_id>', views.commentdelete, name="commentdelete"),
]