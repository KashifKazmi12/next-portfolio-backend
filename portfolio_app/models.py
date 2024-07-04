from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from .utils import validate_video

# Create your models here.

# Header Model
class Header(models.Model):
    profile_picture = models.ImageField(upload_to='HeaderImages/')
    heading = models.CharField(max_length=100)
    sub_heading = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.heading


""" about section model """
# About Model
class About(models.Model):
    video_link = models.URLField(max_length=200, null=True, blank=True)
    heading = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.heading
    

# ProjectStats Model
class ProjectStats(models.Model):
    experience = models.IntegerField()
    projects = models.IntegerField()
    clients = models.IntegerField()

    def __str__(self):
        return f"Experience: {self.experience}, Projects: {self.projects}, Clients: {self.clients}"



# Skill Model
class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return f"{self.skill_name} - {self.percentage}%"
    

# Experience Model
class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    short_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        if self.end_date:
            return f"{self.job_title} at {self.company} ({self.start_date} - {self.end_date})"
        else:
            return f"{self.job_title} at {self.company} (Started: {self.start_date}, Current)"



# Services Model
class Service(models.Model):
    service_title = models.CharField(max_length=100)
    service_image = models.ImageField(upload_to='service_images/')

    def __str__(self):
        return self.service_title


# Portfolio Model
class Portfolio(models.Model):
    portfolio_title = models.CharField(max_length=100)
    portfolio_image = models.ImageField(upload_to='portfolio/portfolio_images/')
    description = models.TextField()
    link = models.URLField(blank=True)
    service_type = models.ForeignKey(Service, on_delete=models.CASCADE)
    video = models.FileField(upload_to='portfolio/portfolio_videos/', blank=True, validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv', 'webm']), validate_video])
    

    def __str__(self):
        return self.portfolio_title
    

# Testimonial Model
class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    TESTIMONIAL_TYPES = [
        ('text', 'Text'),
        ('video', 'Video'),
    ]
    testimonial_type = models.CharField(max_length=10, choices=TESTIMONIAL_TYPES)
    video = models.FileField(upload_to='testimonial_videos/', blank=True, validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv', 'webm']), validate_video])
    feedback = models.TextField()

    def __str__(self):
        return f"{self.client_name}'s Testimonial"
    


#faq model
class FAQ(models.Model):
    faq_title = models.CharField(max_length=100)
    faq_description = models.TextField()
    service_type = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.service_type_id:
            default_service = Service.objects.get_or_create(service_title='General')[0]
            self.service_type = default_service
        super().save(*args, **kwargs)

    def __str__(self):
        return self.faq_title


#ContactDetails model
class ContactDetails(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.heading
    

#Social Links model
class Social(models.Model):
    platform_name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='social_icons/')
    link = models.URLField(unique=True)

    def clean(self):
        # Check if the link is unique
        if Social.objects.exclude(pk=self.pk).filter(link=self.link).exists():
            raise ValidationError('This link already exists.')

    def __str__(self):
        return self.platform_name

    

#ContactUS model
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    services = models.TextField()
    budget_range = models.CharField(max_length=100)
    timeline = models.CharField(max_length=100)
    file = models.FileField(upload_to='contact_files/',blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf'])
    ])
    description = models.TextField()

    def __str__(self):
        return self.name + ' - ' + self.company_name



#FreelancePlatform model
class FreelancePlatform(models.Model):
    platform_name = models.CharField(max_length=100)
    platform_icon = models.ImageField(upload_to='platform_icons/')
    platform_link = models.URLField(unique=True)

    def clean(self):
        # Check if the link is unique
        if FreelancePlatform.objects.exclude(pk=self.pk).filter(platform_link=self.platform_link).exists():
            raise ValidationError('This link already exists.')

    def __str__(self):
        return self.platform_name