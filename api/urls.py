"""api URL Configuration

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
from django.conf.urls import url,include
from taxproj import views, factories
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user/signup$', views.SignUp.as_view(view_factory=factories.UserViewFactory)),
    url(r'^user/signin$', views.SignIn.as_view(view_factory=factories.UserViewFactory)),
    url(r'^user/(?P<user_id>.+)/tax/insert$', views.InsertTaxObject.as_view(view_factory=factories.TaxObjectViewFactory)),
    url(r'^user/(?P<user_id>.+)/tax/get$', views.GetTaxObject.as_view(view_factory=factories.TaxObjectViewFactory))
]

urlpatterns = format_suffix_patterns(urlpatterns)
