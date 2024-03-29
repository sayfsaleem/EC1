from django.contrib import admin
from .models import Tag, Service, CaseStudies, Industries

class ServiceInline(admin.TabularInline):
    model = Service.tags.through
    extra = 1

class CaseStudiesInline(admin.TabularInline):
    model = CaseStudies.tags.through
    extra = 1

class IndustriesInline(admin.TabularInline):
    model = Industries.tags.through
    extra = 1

class TagAdmin(admin.ModelAdmin):
    inlines = [ServiceInline, CaseStudiesInline, IndustriesInline]

admin.site.register(Tag, TagAdmin)
admin.site.register(Service)
admin.site.register(CaseStudies)
admin.site.register(Industries)
from django.contrib import admin
from .models import Job, Applied_User

class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_detail')
    search_fields = ('name', 'short_detail')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Job, JobAdmin)

class AppliedUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'applied_date', 'job')
    search_fields = ('name', 'email', 'job__name')
    list_filter = ('applied_date', 'job__name')

admin.site.register(Applied_User, AppliedUserAdmin)

from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')  # Fields to display in the list view
    search_fields = ('name', 'email', 'subject')  # Enable searching by name, email, and subject
    list_filter = ('subject',)  # Add a filter by subject

admin.site.register(Contact, ContactAdmin)  # Register Contact model with custom admin configuration
