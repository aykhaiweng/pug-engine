from django.urls import path, include


app_name = "api.v1"


urlpatterns = [
    path('pugs/', include('pugs.api.v1.urls'), name="pugs")
]
