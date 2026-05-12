from django.urls import path, re_path
from django.conf import settings
from arches_resolver.views import ResolverMain

uuid_regex = settings.UUID_REGEX

urlpatterns = [
	path("", ResolverMain.as_view(), name="arches_resolver_home"),
]

