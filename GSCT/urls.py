from django.contrib import admin
from django.urls import path
from student import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin-hub/", admin.site.urls),
    path("", views.home, name="home"),
    path("courses/", views.courses, name="courses"),
    path("courseshow/", views.courseshow, name="courseshow"),
    path("coursedetails/<int:id>", views.coursedetails, name="coursedetails"),
    path("studenthub/", views.studenthub, name="studenthub"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("contactus/", views.contactus, name="contactus"),
    path("admin/", views.student_create_show, name="student_create"),
    path("admin/<int:id>", views.student_data, name="student_data"),
    path("update/<int:id>", views.student_update, name="student_update"),
    path("doupdate/<int:id>", views.student_doupdate, name="student_doupdate"),
    path("delete/<int:id>", views.student_delete, name="student_delete"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
