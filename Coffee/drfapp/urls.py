from django.urls import path
from .views import MachineList, PodList

urlpatterns = [

    """Note : use filter fields as url parameters """

    path ('machineList/', views.MachineList.as_view(), name="machineList"),
    path ('podList/', views.PodList.as_view(), name="podList"),

     
]