from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .forms import forms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Class based views
class listview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'tasks'


class detailview(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'task'

class updateview(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('updatepage', kwargs={'pk':self.object})
class deleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('homepage')

# function based views
def add(request):
    taskss = task.objects.all()
    if request.method == "POST":
        name = request.POST.get("taskname", "")
        priority = request.POST.get("priority", "")
        date = request.POST.get("date", "")
        tasks = task(name=name, priority=priority, date=date)
        tasks.save()

    return render(request, 'home.html', {'taskss': taskss})


#
# def details(request):
#
#     return render(request, 'update.html', )
def delete(request, taskid):
    tasks = task.objects.get(id=taskid);
    if request.method == 'POST':
        tasks.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    tasks = task.objects.get(id=id)
    form = forms(request.POST or None, instance=tasks)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'tasks': tasks})
