from rest_framework import serializers
from portfolio_app.models import Header, About, ProjectStats, Skill, Experience, Service, Portfolio, Testimonial, FAQ, ContactDetails, Social, FreelancePlatform, ContactUs

# class TestHeaderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Header
#         fields = ['profile_picture', 'heading', 'sub_heading', 'description']

#     def validate(self, attrs):
#         heading = attrs.get('heading', '')
#         sub_heading = attrs.get('sub_heading', '')

#         if len(heading) <= 10:
#             raise serializers.ValidationError("Heading must be more than 10 characters long.")

#         word_count = len(sub_heading.split())
#         if word_count < 20 or word_count > 30:
#             raise serializers.ValidationError("Sub heading must be between 20 to 30 words.")

#         return attrs
    


class headerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ['profile_picture', 'heading', 'sub_heading', 'description']


class aboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id','video_link', 'heading', 'description']


class projectStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStats
        fields = ['experience', 'projects', 'clients']


class skillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill_name', 'percentage']


class experienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['job_title', 'company', 'short_description', 'start_date', 'end_date']


class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['service_title', 'service_image']


class portfolioSerializer(serializers.ModelSerializer):
    service_type = serviceSerializer()

    class Meta:
        model = Portfolio
        fields = ['id','portfolio_title', 'portfolio_image', 'description', 'link', 'service_type', 'video']

class testimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['client_name', 'company', 'testimonial_type', 'video', 'feedback']


class FAQSerializer(serializers.ModelSerializer):
    service_type = serviceSerializer()
    
    class Meta:
        model = FAQ
        fields = ['id','faq_title', 'faq_description', 'service_type']


class contactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetails
        fields = ['heading', 'description', 'email', 'phone_number']


class socialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['platform_name', 'icon', 'link']


class contactUsSerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return value

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'company_name', 'phone_number', 'services', 'budget_range', 'timeline', 'file', 'description']



class freelancePlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreelancePlatform
        fields = ['platform_name', 'platform_icon', 'platform_link']