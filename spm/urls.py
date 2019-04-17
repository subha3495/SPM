"""spm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, ListView

from app import views
from app.models import Add_Company, Add_Agent, Customer_Registration, Shares_Add, Feedback, Suggesstion
from django.conf.urls.static import static
from spm import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',TemplateView.as_view(template_name='index.html')),
    path('adminlog/',TemplateView.as_view(template_name="admin_log.html")),
    path('home/',TemplateView.as_view(template_name="homepage.html")),
    path('about/',TemplateView.as_view(template_name="aboutus.html")),
    path('carrir/',TemplateView.as_view(template_name="carrier.html")),
    path('contact/',TemplateView.as_view(template_name="contactus.html")),
    path('company/',TemplateView.as_view(template_name="company.html")),
    path('company_reg/',views.companyregi),
    path('company_login/',views.companylogin),
    path('add_company/',TemplateView.as_view(template_name='add_company.html')),
    path('addcomp/',views.add_company),
    path('view_allcompanies/',ListView.as_view(template_name='view_companies.html',model=Add_Company),name='companyviews'),
    path('update_company/',ListView.as_view(template_name='update_company.html',model=Add_Company)),
    # path('update/',views.openupdatecompany),
    path('save_update_company<int:pk>/',views.save_update_company.as_view()),
    # path('view_companies/',views.updatedcompant),

    path('Delete_company/', views.delete_comp),
    path('delete/', views.delete),
    #agent
    path('add_agent/',TemplateView.as_view(template_name='add_agent.html')),
    path('addagent/',views.add_agent),
    path('view_allagents/',ListView.as_view(template_name='view_agents.html',model=Add_Agent)),

    path('update_agent/',ListView.as_view(template_name='update_agent.html',model=Add_Agent)),
    path('save_update_agent<int:pk>/',views.save_update_agent.as_view()),
    path('Delete_agent/', views.delete_agent),
    path('deleteagent/', views.deleteagent),

    #customer
    path('custmerregisration/',TemplateView.as_view(template_name='customer_reg.html')),
    path('customereg/',views.customereg),
    path('view_allcustomers/', ListView.as_view(template_name='view_customer.html', model=Customer_Registration)),
    path('update_customer/', ListView.as_view(template_name='update_customer.html', model=Customer_Registration)),
    path('save_update_customer<int:pk>/',views.save_update_customer.as_view()),
    path('Delete_Customer/',views.Delete_Customer),
    path('deletecustomer/',views.deletecustomer),

#company
    path('shares_add/',TemplateView.as_view(template_name='add_share.html')),
    path('sharesadded/',views.add_share),
    path('view_allshares/',ListView.as_view(template_name='view_shares.html', model=Shares_Add)),
    path('update_shares/',ListView.as_view(template_name='update_shares.html',model=Shares_Add)),
    path('view_shares/',views.updatedshares),
    path('updateshares/',views.openupdatedshares),
    path('Delete_share/', views.delete_shar),
    path('deleteshare/', views.deleteshare),

#feedback
    path('fb/',TemplateView.as_view(template_name='feedback.html')),
    path('savefb/',views.feedbacksave),
    path('viewfeedback/', ListView.as_view(template_name='adminfeedback..html', model=Feedback)),
    path('deletefb/',views.deletefeedback),

#suggesstion
    path('sg/',TemplateView.as_view(template_name='suggession.html')),
    path('savesug/',views.suggessionsave),
    path('viewsuggession/', ListView.as_view(template_name='adminsuggession.html', model=Suggesstion)),
    path('deletesg/',views.deletesuggession),

#search
    path('search/',views.searchcompanies),

#Buy shares
    path('addshare_customer/',TemplateView.as_view(template_name='buy.html')),
    path('add_buyshare/',views.addshare_customer),
    path('view_allbuyers/', ListView.as_view(template_name='view_buyshares.html', model=Shares_Add)),

    #Sell Shares
    path('sellshare_customer/', TemplateView.as_view(template_name='sell.html')),
    path('add_sellshare/', views.sellshare_customer),
    path('view_allsellers/', ListView.as_view(template_name='view_sellshares.html', model=Shares_Add)),




]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)