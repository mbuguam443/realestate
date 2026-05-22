from django.shortcuts import render,redirect
from .models import Property,Enquiry

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from .forms import PropertyForm
# Create your views here.
def home(request):
    return render(request,'index_video.html')
def about(request):
    return render(request,'about.html')
def notfound(request):
    return render(request,'404.html')
def agent_profile(request):
    return render(request,'agent_profile.html')
def blog_post(request):
    return render(request,'blog-post.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def faq(request):
    return render(request,'faq.html')
def property_details(request, pk):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Enquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        messages.success(request, "Your enquiry has been submitted successfully.")
        
        return redirect('property_details',pk=pk)

    # Get a single property by its primary key (id)
    property = get_object_or_404(Property, pk=pk)

    # Get two similar properties (excluding the current one)
    similar_properties = Property.objects.exclude(pk=pk)[:2]

    context = {
        'property': property,
        'similar_properties': similar_properties,
    }

    return render(request, 'property-details.html', context)
def property(request):
    # Fetch all properties from the database
    properties = Property.objects.all().order_by('-id')

    # Send the properties to property.html
    mydict = {
        'properties': properties
    }
    return render(request, 'property.html', context=mydict)
def register(request):
    return render(request,'register.html')
def login_view(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('messagesClient')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')
    
def single_agent(request):
    return render(request,'single_agent.html')
def thank_you(request):
    return render(request,'thank-you.html')
def index_map(request):
    return render(request,'index_map.html')
def index_parallax(request):
    return render(request,'index_parallax.html')
def index_slideshow(request):
    return render(request,'index_slideshow.html')
def index_video(request):
    return render(request,'index_video.html')
@login_required
def postproperty(request):
    # Check if the form has been submitted
    if request.method == 'POST':
        # Create form instance with submitted data and uploaded files
        form = PropertyForm(request.POST, request.FILES)

        # Validate the form
        if form.is_valid():
            # Save property to the database
            form.save()
            print("form saved successfully...")
            # Redirect to property listing page after saving
            return redirect('property')   # Change to your actual URL name
    else:
        # Create an empty form when the page is first loaded
        form = PropertyForm()

    # Send the form to the template
    return render(request, 'postproperty.html', {
        'form': form
    })
@login_required
def messagesClient(request):

    unread_count = Enquiry.objects.filter(is_read=False).count()

    context = {
        'unread_count': unread_count
    }

    enquiries = Enquiry.objects.all().order_by('-created_at')
    
    mydict={'enquiries': enquiries,'unread_count':unread_count }

    return render(request, 'messagesClient.html',context=mydict)


def logout_view(request):
    logout(request)
    return redirect('login')

def markread(request, pk):

    enquiry = Enquiry.objects.get(id=pk)

    enquiry.is_read = True
    enquiry.save()

    return redirect('messagesClient')