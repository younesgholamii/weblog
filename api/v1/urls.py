from django.urls import path, include


urlpatterns = [
    path('blog/', include('weblog.api.v1.urls'))
]