from django.conf.urls.defaults import patterns, url


urlpatterns = patterns("froide.publicbody.views",
    url(r"^(?P<slug>[-\w]+)/$", 'show_foilaw', name="publicbody-foilaw-show"),
)
