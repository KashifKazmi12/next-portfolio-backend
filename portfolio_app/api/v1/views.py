from rest_framework.views import APIView
from rest_framework.response import Response 
from portfolio_app.models import Header, About, ProjectStats, Skill, Experience, Service, Portfolio, Testimonial, FAQ, ContactDetails, Social, FreelancePlatform, ContactUs
from portfolio_app.api.v1.serializer import headerSerializer, aboutSerializer, projectStatsSerializer, skillSerializer, experienceSerializer, serviceSerializer, portfolioSerializer, testimonialSerializer, FAQSerializer, contactDetailsSerializer, socialSerializer, freelancePlatformSerializer, contactUsSerializer
from rest_framework import status
from rest_framework.permissions import BasePermission
import os
from rest_framework.exceptions import PermissionDenied


class RequestAuthorization(BasePermission):
    def has_permission(self, request, view):
        auth_key = request.headers.get('secret')
        # Your custom logic goes here
        # Example: Check if the user is authenticated
        print(auth_key)

        if auth_key == os.getenv('SECRET_KEY'):
            return True
        else:
            raise PermissionDenied({"message":"You do not have permission to perform this action Okay."})
    

class PortfolioSectionsData_View(APIView):
    permission_classes = [RequestAuthorization]
    def get(self, request):
        # headerData
        header = Header.objects.last()
        header = headerSerializer(header)      

        #AboutData
        about = About.objects.last()
        about = aboutSerializer(about)

        # ProjectStats
        projectStats = ProjectStats.objects.last()
        projectStats = projectStatsSerializer(projectStats)
        
        skills = Skill.objects.all()
        skills = skillSerializer(skills, many=True)

        experience = Experience.objects.all()
        experience = experienceSerializer(experience, many=True)

        services = Service.objects.all()
        services = serviceSerializer(services, many=True)
        
        portfolio = Portfolio.objects.all()
        portfolio = portfolioSerializer(portfolio, many=True)
        
        testimonials = Testimonial.objects.all()
        testimonials = testimonialSerializer(testimonials, many=True)

        faqs = FAQ.objects.all()
        faqs = FAQSerializer(faqs, many=True)

        contactDetails = ContactDetails.objects.last()
        contactDetails = contactDetailsSerializer(contactDetails)

        socialLinks = Social.objects.all()
        socialLinks = socialSerializer(socialLinks, many=True)

        freelancePlatform = FreelancePlatform.objects.all()
        freelancePlatform = freelancePlatformSerializer(freelancePlatform, many=True)

        

        # Return the serialized data in the response
        return Response({
            "header":header.data,
            "about":about.data,
            "projectStates":projectStats.data,
            "skills":skills.data,
            "experience":experience.data,
            "services":services.data,
            "portfolio":portfolio.data,
            "testimonials":testimonials.data,
            "faqs":faqs.data,
            "contactDetails":contactDetails.data,
            "socialLinks":socialLinks.data,
            "freelancePlatform":freelancePlatform.data
            
            }, status=status.HTTP_200_OK)


class ContactUsSubmit_View(APIView):
    permission_classes = [RequestAuthorization]
    def post(self, request, format=None):
        serializer = contactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)