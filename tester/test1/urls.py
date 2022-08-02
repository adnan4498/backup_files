from django.urls import path
from .import views 
from .views import API1, Login, LCStudentList, RUDStudentList, StudentModelViewSet
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

#Register StudentViewSet with Router
router.register('studentapi', views.StudentModelViewSet, basename = 'student')


urlpatterns = [
    # path('index/',views.index,name='index'),
    # path('API1/',API1.as_view()),
    # path('Login/',Login.as_view()),
    path('Stu/',LCStudentList.as_view()),
    path('Stu/<int:pk>/',RUDStudentList.as_view()),
]
