from django.urls import path, include
from .api.v1.views import PortfolioSectionsData_View, ContactUsSubmit_View

urlpatterns = [
    path("", PortfolioSectionsData_View.as_view(), name="SectionsData"),
    path("contact/", ContactUsSubmit_View.as_view(), name="contact"),
    
]