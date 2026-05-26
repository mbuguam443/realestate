from django.shortcuts import render,redirect
from .models import Property,Enquiry

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from .forms import ContactForm
from django.core.paginator import Paginator

from .forms import PropertyForm
# Create your views here.
def home(request):
    properties = Property.objects.all().order_by('-id')

    paginator = Paginator(properties, 9)  # 9 properties per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index_video.html', {
        'page_obj': page_obj
    })
   
def about(request):
    return render(request,'about.html')
def notfound(request, exception):
    return render(request,'404.html', status=404)
def agent_profile(request):
    return render(request,'agent_profile.html')
def blog_post(request):
    return render(request,'blog-post.html')
def gallery(request):
    return render(request,'gallery.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    print("Hello there")
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                subject,
                f"Name: {name}\nEmail: {email}\n\n{message}",
                email,
                ['mbuguam443@gmail.com'],
                fail_silently=False,
            )

            return render(request, 'thank-you.html')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
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
        
        return redirect('thank_you')

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
    properties = Property.objects.all().order_by('-id')

    paginator = Paginator(properties, 9)  # 9 properties per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'property.html', {
        'page_obj': page_obj
    })
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
@staff_member_required
def delete_property(request, pk):
    property = get_object_or_404(Property, pk=pk)

    if request.method == "GET":
        property.delete()
        return redirect('property')

    return redirect('property_details', pk=pk)    
@staff_member_required
def edit_property(request, pk):
    property = get_object_or_404(Property, pk=pk)

    if request.method == 'POST':
        form = PropertyForm(
            request.POST,
            request.FILES,
            instance=property
        )

        if form.is_valid():
            form.save()
            return redirect('property_details', pk=property.pk)

    else:
        form = PropertyForm(instance=property)

    return render(
        request,
        'editproperty.html',
        {
            'form': form,
            'property': property
        }
    )

def property_search(request):

    properties = Property.objects.all().order_by('-id')

    location = request.GET.get('location')
    property_type = request.GET.get('property_type')
    status = request.GET.get('status')
    max_price = request.GET.get('max_price')
    bedrooms = request.GET.get('bedrooms')
    bathrooms = request.GET.get('bathrooms')
    min_area = request.GET.get('min_area')

    if location:
        properties = properties.filter(location__icontains=location)

    if property_type:
        properties = properties.filter(property_type=property_type)

    if status:
        properties = properties.filter(status=status)

    if max_price:
        properties = properties.filter(price__lte=max_price)

    if bedrooms:
        properties = properties.filter(bedrooms__gte=bedrooms)

    if bathrooms:
        properties = properties.filter(bathrooms__gte=bathrooms)

    if min_area:
        properties = properties.filter(area__gte=min_area)

    # Pagination
    paginator = Paginator(properties, 9)  # 9 properties per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'index_video.html',
        {
            'page_obj': page_obj,
            'location': location,
            'property_type': property_type,
            'status': status,
            'max_price': max_price,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'min_area': min_area,
        }
    )