from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^index$', 'demo.views.index_view', name='index_view'),
	url(r'^post/(\d{1,2})$', 'demo.views.post', name='post'),
	url(r'^hora$', 'demo.views.hora_actual', name='hora'),

    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
