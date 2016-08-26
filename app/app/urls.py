"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views

from main import views as main_views
from products import views as products_views

urlpatterns = [
    # Admin Panel Routes
    url(r'^admin/', admin.site.urls),

    # Login/Logout Routes
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout, name='logout'),

    # Main Site Routes
    url(r'^$', main_views.Index.as_view(), name='index'),
    url(r'^about/', main_views.About.as_view(), name='about'),
    url(r'^contact/', main_views.Contact.as_view(), name='contact'),
    url(r'^cover/', main_views.Cover.as_view(), name='cover'),
    url(r'^test/$', main_views.Test.as_view(), name='test'),

    # Categories Routes
    url(r'^categories/$', products_views.CategoryList.as_view(), name='category_list'),
    url(r'^categories/new', products_views.CategoryCreate.as_view(), name='category_create'),
    url(r'^categories/(?P<slug>[-\w]+)/show$', products_views.CategoryDetail.as_view(), name='category_detail'),
    url(r'^categories/(?P<slug>[-\w]+)/update', products_views.CategoryUpdate.as_view(), name='category_update'),
    url(r'^categories/(?P<slug>[-\w]+)/$', products_views.CategoryProductsList.as_view(), name='category_product_list'),

    # Products Routes
    url(r'^products/$', products_views.ProductList.as_view(), name='product_list'),
    url(r'^products/new', products_views.ProductCreate.as_view(), name='product_create'),
    url(r'^products/(?P<slug>[-\w]+)/$', products_views.ProductDetail.as_view(), name='product_detail'),
    url(r'^products/(?P<slug>[-\w]+)/update', products_views.ProductUpdate.as_view(), name='product_update'),
    # Test Route
    #url(r'^test/(?P<slug>[-\w]+)', products_views.CategoryTest.as_view(), name='category_test'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
