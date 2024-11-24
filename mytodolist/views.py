from django.shortcuts import render
from .forms import MyForm
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    return HttpResponse("Hello, Mate!")

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            name = form.cleaned_data['fieldname']  # Replace 'fieldname' with your actual field name
            email = form.cleaned_data['email']    # Ensure these fields exist in your form
            report = form.cleaned_data['report']
            
            # Example: Log the data or save it to a database
            print(f"Name: {name}, Email: {email}, Report: {report}")
            
            # Redirect after successful form submission
            return HttpResponseRedirect('/success/')  # Replace '/success/' with your URL
    else:
        form = MyForm()
    
    return render(request, 'mytemplate.html', {'form': form})
