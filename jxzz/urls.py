from django.contrib import admin
from django.urls import include,path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.views import static ##新增
# from django.conf import settings ##新增
# from django.conf.urls import url ##新增


urlpatterns = [
    path('jxzz_2/', include('jxzz_2.urls')),
    path('admin/', admin.site.urls),
    # path('index/', vmm_views.home),
    # url(r'^static/(?P<path>.*)$', static.serve,{'document_root': settings.STATIC_ROOT}, name='static'),
]
urlpatterns += staticfiles_urlpatterns()