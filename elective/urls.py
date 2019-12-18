from django.urls import path
from . import views 

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('popularity/',views.sort_popularity,name='sort_popularity'),
    path('attendence/',views.sort_attendence,name='sort_attendence'), 
    path('marks/',views.sort_marks,name='sort_marks'),  
    path('quality/',views.sort_quality,name='sort_quality'),
    path('feedback/',views.take_feedback,name='take_feedback'),
    path('elective/<int:pk>/',views.show_review,name='show_review'),


        
]