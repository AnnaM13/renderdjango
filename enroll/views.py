from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import StudentRegistration
from .models import User
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # Check if the user already exists to avoid duplicates
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            if User.objects.filter(email=em).exists():
                # Optionally add an error message
                fm.add_error('email', 'A user with this email already exists.')
            else:
                # Save the form if no duplicate exists
                fm.save()
                return redirect('addshow')  # Redirect after successful form submission
    else:
        fm = StudentRegistration()

    stud = User.objects.all()  # Fetch all User objects after processing the form
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})
     # for delte
def delete_data(request, id):
     if request.method == 'POST':
      pi = User.objects.get(pk=id)
      pi.delete()
      return HttpResponseRedirect('/')

# def delete_data(request, id):  # Make sure 'id' is passed into the view
#     if request.method == 'POST':
#         # Fetch the User object by ID or return 404 if not found
#         pi = get_object_or_404(User, pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/')  # Redirect to a success page or home
#     return HttpResponseRedirect('/')  # Optionally handle non-POST requests here

def update_data(request,id):
    if request.method == 'POST':
     pi = User.objects.get(pk=id)  
     fm = StudentRegistration(request.POST, instance=pi)
     if fm.is_valid():
        fm.save()
    else:
     pi = User.objects.get(pk=id)  
     fm = StudentRegistration(instance=pi)    
    return render(request, 'enroll/updatestudent.html',{'form':fm})