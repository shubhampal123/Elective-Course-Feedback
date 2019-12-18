from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def homepage(request):
    return render(request,'elective/homepage.html',{})


def sort_popularity(request):
    courses=Course.objects.all().order_by('-count')
    return render(request,'elective/sort.html',{'courses':courses})


def sort_attendence(request):
    courses=Course.objects.all().order_by('-attendence')
    return render(request,'elective/sort.html',{'courses':courses})



def sort_marks(request):
    courses=Course.objects.all().order_by('-marks')
    return render(request,'elective/sort.html',{'courses':courses})

    

     
def sort_quality(request):
    courses=Course.objects.all().order_by('-quality')
    return render(request,'elective/sort.html',{'courses':courses})

def take_feedback(request):
    if request.method == "POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():

            feedback=form.save(commit=False)
        
            course=Course.objects.all().filter(name=feedback.name).filter(teacher=feedback.teacher)
              
            x=len(course)
            if x<=0 : 
                return HttpResponse("No such course")
            else :
                temp=course[0].pk
                
                cnt=course[0].count 
                mk=course[0].marks
                at=course[0].attendence
                ql=course[0].quality

                cnt+=1 
                print(temp)
                Course.objects.filter(pk=temp).update(count=cnt)

                y=mk+feedback.marks
                y=y/cnt

                Course.objects.filter(pk=temp).update(marks=y)

                y=at+feedback.attendence
                y=y/cnt

                Course.objects.filter(pk=temp).update(attendence=y)

                y=ql+feedback.quality
                y=y/cnt

                Course.objects.filter(pk=temp).update(quality=y)
                feedback.course=course[0]
                feedback.save()

                return redirect('/')
        else:
            return HttpResponse("Invalid respone")  
    
    else:
        form=FeedbackForm()
        return render(request,'elective/take_feedback.html',{'form':form})


def show_review(request,pk):
    course=get_object_or_404(Course,pk=pk)
    feedbacks=Feedback.objects.filter(course=course)
    return render(request,'elective/show_review.html',{'feedbacks':feedbacks,'course':course})


    

