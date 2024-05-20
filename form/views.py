from django.shortcuts import render, redirect
from .forms import UserForm

def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserForm()
    
    return render(request, 'form/user_form.html', {'form': form})

def success_view(request):
    return render(request, 'form/success.html')

# Create your views here.
