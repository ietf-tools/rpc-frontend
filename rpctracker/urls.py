"""
URL configuration for rpc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, register_converter

from rpc import views
from rpc import api as rpc_api


class DraftNameConverter:
    regex = "draft(-[a-z0-9]+)+"

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value


class RfcNumberConverter:
    regex = "rfc(1-9)[0-9]+"

    def to_python(self, value):
        return int(value[3:])

    def to_url(self, value):
        return f"rfc{value:d}"


register_converter(DraftNameConverter, "draft-name")
register_converter(RfcNumberConverter, "rfc-number")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("oidc/", include("mozilla_django_oidc.urls")),
    path("login/", views.index),
    path("api/rpc/assignments/", rpc_api.assignments),
    path("api/rpc/assignments/<int:assignment_id>", rpc_api.assignment),
    path("api/rpc/clusters/", rpc_api.clusters),
    path("api/rpc/clusters/<int:number>", rpc_api.cluster),
    path("api/rpc/documents/", rpc_api.rfcs_to_be),
    path("api/rpc/documents/<draft-name:draftname>/", rpc_api.rfc_to_be),
    path("api/rpc/documents/<rfc-number:rfcnum>/", rpc_api.rfc_to_be),
    path("api/rpc/documents/<draft-name:draftname>/labels/", rpc_api.rfc_to_be_labels),
    path("api/rpc/documents/<rfc-number:rfcnum>/labels/", rpc_api.rfc_to_be_labels),
    path("api/rpc/profile", rpc_api.profile),
    path("api/rpc/rpc_person/", rpc_api.rpc_person),
    path("api/rpc/submissions/", rpc_api.submissions),
    path("api/rpc/queue/", rpc_api.queue),
    path("api/rpc/label/", rpc_api.label),
]
