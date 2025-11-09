from django.shortcuts import render ,redirect
from .models import Project
from django.contrib import messages
from .forms import ContactForm
from .models import About

def home(request):
    
    projects=Project.objects.all()
    return render(request,'main/home.html',{'projects':projects})

def contact(request):
    if request.method=='POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your message has been sent successfully.")
            return redirect('contact')  # Redirect to the same page to clear the form
    else:
        form =ContactForm()
        
    return render(request, 'main/contact.html', {'form': form})
# views.py
from .models import Contact

def messages_list(request):
    all_messages = Contact.objects.all().order_by('-date_time')
    return render(request, 'main/messages.html', {'messages': all_messages})

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')