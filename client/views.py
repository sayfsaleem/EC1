from django.views.generic import TemplateView
from .models import Service,CaseStudies,Industries
from django.utils.text import slugify
from django.shortcuts import get_object_or_404,render
# Create your views here.
class HomeView(TemplateView):
    template_name = 'index-2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve queryset including names
        services = Service.objects.values_list('name', flat=True)
        services_with_slugs = [(name, slugify(name)) for name in services]
        context["services"] = services_with_slugs
        cases1 = CaseStudies.objects.values('name','slug')

        context["cases1"] = cases1
        industries1 = Industries.objects.values_list('name', flat=True)
        industries1_with_slugs = [(name, slugify(name)) for name in industries1]
        casestudies = CaseStudies.objects.values('title','date','image','slug')
        context["industries1"] = industries1_with_slugs
        context["cases"] = casestudies
        return context


class ServiceView(TemplateView):
    template_name = 'service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve the slug from the URL
        service_slug = kwargs.get('name')

        # Unslugify the slug to get the original name of the service
        service_name_parts = service_slug.split('-')[:2]  # Get first two words
        service_name = ' '.join(service_name_parts)

        # Retrieve the service based on the name matching the first one or two words
        service = get_object_or_404(Service, name__startswith=service_name)
        services = Service.objects.values_list('name', flat=True)
        services_with_slugs = [(name, slugify(name)) for name in services]
        last_5_case_studies = CaseStudies.objects.order_by('-id')[:5]
        case_studies = last_5_case_studies
        industries = Industries.objects.values('name', 'square_image',)
        cases1 = CaseStudies.objects.values('name','slug')

        context["cases1"] = cases1
        industries1 = Industries.objects.values_list('name', flat=True)
        industries1_with_slugs = [(name, slugify(name)) for name in industries1]
        context["industries1"] = industries1_with_slugs
        context["case_studies"] = case_studies
        context["service"] = service
        context["services"] = services_with_slugs
        context["industries"] = industries
        return context


class IndustryView(TemplateView):
    template_name = 'industry.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve the slug from the URL
        industry_slug = kwargs.get('name')

        # Unslugify the slug to get the original name of the industry
        industry_name = industry_slug.replace('-', ' ')

        # Retrieve the industry based on the name matching the unslugified name
        industry = get_object_or_404(Industries, name__iexact=industry_name)

        # Retrieve services
        services = Service.objects.values_list('name', flat=True)
        services_with_slugs = [(name, slugify(name)) for name in services]
        industries = Industries.objects.values('name','square_image')
        # Retrieve recent case studies
        last_5_case_studies = CaseStudies.objects.order_by('-id')[:5]
        cases1 = CaseStudies.objects.values('name','slug')

        context["cases1"] = cases1
        industries1 = Industries.objects.values_list('name', flat=True)
        industries1_with_slugs = [(name, slugify(name)) for name in industries1]
        context["industries1"] = industries1_with_slugs
        context["industry"] = industry
        context["services"] = services_with_slugs
        context["case_studies"] = last_5_case_studies
        context["industries"] = industries
        return context

# views.py

class CaseView(TemplateView):
    template_name = 'casestudy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve the slug from the URL
        case_slug = kwargs.get('name')

        # Retrieve the case study based on the slug
        case_study = get_object_or_404(CaseStudies, slug=case_slug)

        # Retrieve services
        services = Service.objects.values_list('name', flat=True)
        services_with_slugs = [(name, slugify(name)) for name in services]

        # Retrieve related industries
        industries = Industries.objects.values('name', 'square_image')
        last_case_studies = CaseStudies.objects.all().reverse()
        context["case"] = case_study
        context["services"] = services_with_slugs
        context["industries"] = industries
        context["case_studies"] = last_case_studies
        cases1 = CaseStudies.objects.values('name','slug')

        context["cases1"] = cases1
        industries1 = Industries.objects.values_list('name', flat=True)
        industries1_with_slugs = [(name, slugify(name)) for name in industries1]
        context["industries1"] = industries1_with_slugs
        return context

from django.shortcuts import redirect
from .models import Contact

class ContactView(TemplateView):
    template_name = '/contact/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = Service.objects.values_list('name', flat=True)

        # Generate slugs for each name
        services_with_slugs = [(name, slugify(name)) for name in services]

        context["services"] = services_with_slugs
        cases1 = CaseStudies.objects.values('name','slug')

        context["cases1"] = cases1
        industries1 = Industries.objects.values_list('name', flat=True)
        industries1_with_slugs = [(name, slugify(name)) for name in industries1]
        context["industries1"] = industries1_with_slugs
        return context

    def post(self, request, *args, **kwargs):
        print("POST request received.")  # Add a print statement for debugging
        # Extract data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create a new Contact instance and save it to the database
        contact = Contact.objects.create(name=name, email=email, subject=subject, text=message)

        # Redirect to the root URL after successful form submission # Add a print statement for debugging
        return render(request,'message.html',{"message_name":'Submitted Successfully',"message_title":"You've Successfully Received your message","message_description":"We've Received your message,Elitechain LLC will get back to you soon - Happy Future!"})


from .models import Job,Applied_User
class CareersView(TemplateView):
    template_name = 'career.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = Service.objects.values_list('name', flat=True)
        services_with_slugs = [(name, slugify(name)) for name in services]
        context["services"] = services_with_slugs
        context["jobs"] = Job.objects.all()
        services = Service.objects.values_list('name', flat=True)
        services_with_slugs = [(name, slugify(name)) for name in services]
        context["services"] = services_with_slugs
        cases1 = CaseStudies.objects.values('name','slug')

        context["cases1"] = cases1
        industries1 = Industries.objects.values_list('name', flat=True)
        industries1_with_slugs = [(name, slugify(name)) for name in industries1]
        context["industries1"] = industries1_with_slugs
        return context



class ApplyView(TemplateView):
    template_name = 'apply.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = kwargs.get('name')
        job_detail = Job.objects.get(slug=name)
        services = Service.objects.values_list('name', flat=True)
        services_with_slugs = [(name, slugify(name)) for name in services]
        context["services"] = services_with_slugs
        context["Job"] = job_detail
        services = Service.objects.values_list('name', flat=True)
        services_with_slugs = [(name, slugify(name)) for name in services]
        context["services"] = services_with_slugs
        cases1 = CaseStudies.objects.values('name','slug')

        context["cases1"] = cases1
        industries1 = Industries.objects.values_list('name', flat=True)
        industries1_with_slugs = [(name, slugify(name)) for name in industries1]
        context["industries1"] = industries1_with_slugs
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('number')
        cover_letter = request.FILES.get('cover_letter')
        resume = request.FILES.get('resume')
        name = kwargs.get('name')
        job_detail = Job.objects.get(slug=name)
        try:
            apply = Applied_User.objects.create(
                name=name,
                email=email,
                number=phone_number,
                cover_letter=cover_letter,
                resume=resume,
                job=job_detail
            )
            # Redirect to a success page or another URL
            return render(request,'message.html',{"message_name":'Submitted Successfully',"message_title":"You've Successfully Applied for this Position","message_description":"We've Received your info for this Position,Elitechain LLC will get back to you soon - Happy Future!"})
        except Job.DoesNotExist:
            # Handle the case where the specified job does not exist
            return render(request,'message.html',{"message_name":'ERROR',"message_title":"Please Try again Later","message_description":"We've Received your browser info for this Bug,Elitechain LLC will fix this bug soon - Happy Day!"}) # Redirect to an error page or display an error message


class AboutView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve queryset including names
        services = Service.objects.values_list('name', flat=True)
        services_with_slugs = [(name, slugify(name)) for name in services]
        context["services"] = services_with_slugs
        cases1 = CaseStudies.objects.values('name','slug')

        context["cases1"] = cases1
        industries1 = Industries.objects.values_list('name', flat=True)
        industries1_with_slugs = [(name, slugify(name)) for name in industries1]
        context["industries1"] = industries1_with_slugs
        return context




def custom_error(request):
    return render(request, 'message.html', {
        "message_name": "Error",
        "message_title": "Oops! Something went wrong",
        "message_description": "We apologize, but an unexpected error occurred."
    })

def handler404(request, exception):
    return render(request, 'message.html', {
        "message_name": "404 Not Found",
        "message_title": "Oops! Page Not Found",
        "message_description": "The page you are looking for does not exist."
    }, status=404)

def handler500(request):
    return render(request, 'message.html', {
        "message_name": "500 Internal Server Error",
        "message_title": "Oops! Server Error",
        "message_description": "Something went wrong on the server. Please try again later."
    }, status=500)
