from django.contrib import admin
from .models import Header, About, ProjectStats, Skill, Experience, Service, Portfolio, Testimonial, ContactDetails, Social, ContactUs, FreelancePlatform, FAQ
from django.utils.html import format_html

# Register your models here.
class HeaderAdmin(admin.ModelAdmin):
    def profilePicture(self, obj):
        return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(obj.profile_picture.url))

    list_display = ('heading', 'sub_heading', 'description', 'profilePicture')  
    search_fields = ('heading', 'sub_heading', 'description')  
    list_filter = ('heading', 'sub_heading')  


admin.site.register(Header, HeaderAdmin)


#about admin
class AboutAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description', 'videoLink')
    search_fields = ('heading',)

    def videoLink(self, obj):
        if obj.video_link:
            return format_html('<a href="{}" target="_blank">{}</a>'.format(obj.video_link, obj.video_link))
        else:
            return "No video link"
    videoLink.short_description = 'Video Link'

admin.site.register(About, AboutAdmin)


class ProjectStatsAdmin(admin.ModelAdmin):
    list_display = ('experience', 'projects', 'clients')
    search_fields = ('experience', 'projects', 'clients')

admin.site.register(ProjectStats, ProjectStatsAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'percentage')
    search_fields = ('skill_name',)

admin.site.register(Skill, SkillAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date')
    search_fields = ('job_title', 'company')

admin.site.register(Experience, ExperienceAdmin)


class ServiceAdmin(admin.ModelAdmin):
    def serviceImage(self, obj):
        if obj.service_image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(obj.service_image.url))
        else:
            return "No Image"
    
    list_display = ('service_title','serviceImage')
    search_fields = ('service_title',)

admin.site.register(Service, ServiceAdmin)



class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('portfolio_title', 'portfolio_video_url', 'portfolio_image_display')
    search_fields = ('portfolio_title',)

    def portfolio_image_display(self, obj):
        if obj.portfolio_image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(obj.portfolio_image.url))
        else:
            return "No image"
    portfolio_image_display.short_description = 'Portfolio Image'
    
    def portfolio_video_url(self, obj):
        if obj.video:
            return format_html("<a href={} target='_blank'>{}</a>".format(obj.video.url, obj.video.url.split('/')[-1]))
        else:
            return "No Video"
    portfolio_video_url.short_description = 'Portfolio Video'
admin.site.register(Portfolio, PortfolioAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'testimonial_type', 'testimonial_link')
    search_fields = ('client_name', 'company')
    list_filter = ('testimonial_type',)

    def testimonial_link(self, obj):
        if obj.testimonial_type == 'video' and obj.video:
            return format_html("<a href={} target='_blank'>Video</a>".format(obj.video.url))
        else:
            return obj.feedback
    testimonial_link.short_description = 'Testimonial'

admin.site.register(Testimonial, TestimonialAdmin)



class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ('heading', 'email', 'phone_number')
    search_fields = ('heading', 'email', 'phone_number')

admin.site.register(ContactDetails, ContactDetailsAdmin)


class SocialAdmin(admin.ModelAdmin):
    list_display = ('platform_name', 'link', 'social_icon')
    search_fields = ('platform_name', 'link')

    def social_icon(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(obj.icon.url))
        else:
            return "No image"
    social_icon.short_description = 'Portfolio Image'


admin.site.register(Social, SocialAdmin)



class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company_name', 'phone_number', 'services', 'budget_range', 'timeline')
    search_fields = ('name', 'email', 'company_name', 'phone_number', 'services', 'budget_range', 'timeline')

admin.site.register(ContactUs, ContactUsAdmin)


class FreelancePlatformAdmin(admin.ModelAdmin):
    list_display = ('platform_name', 'platform_link', 'platformIcon')
    search_fields = ('platform_name', 'platform_link')

    def platformIcon(self, obj):
        return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(obj.platform_icon.url))
    
    platformIcon.short_description = 'platform icon'

admin.site.register(FreelancePlatform, FreelancePlatformAdmin)



admin.site.register(FAQ)