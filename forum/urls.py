from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^post$', views.post, name='post'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^hotlines$', views.hotlines, name='hotlines'),
    url(r'^references$', views.references, name='references'),
]

urlpatterns += [
    url(r'^accounts/login/$', login, { 'template_name': 'admin/login.html' }, name='login' ),
    url(r'^accounts/logout/$', logout, { 'template_name': 'admin/my_account.html', 'next_page': '/' }, name='logout' ),
    url(r'^signup/$', views.signup, name='signup'),
]
