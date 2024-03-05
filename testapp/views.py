from django.shortcuts import render, redirect
from .models import YourModel
from testapp.tasks import change
from django.http import HttpResponse  
def your_view(request):
    model = YourModel.objects.all()
    if request.method == 'POST':
        form = request.POST.get('a')
        obj=YourModel.objects.create(a=form)
        obj.save()
        
        return redirect('your_view')
    return render(request, 'index.html',{'model':model}) 
