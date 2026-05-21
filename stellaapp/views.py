from django.shortcuts import render,redirect
from .models import Property
from django.shortcuts import render, get_object_or_404

from .forms import PropertyForm
# Create your views here.
def home(request):
    return render(request,'index.html')
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
def login(request):
    return render(request,'login.html')
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
