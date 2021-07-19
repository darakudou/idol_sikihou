from django.urls import path

from setlist_forecast import views

urlpatterns = {
    path('', views.IndexView.as_view(), name="index")
}
