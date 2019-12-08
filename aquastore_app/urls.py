from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'aquastore_app'

urlpatterns = [
    path('', views.lista_aguas, name='lista_aguas'),
    path('<slug:slug_da_categoria>/', views.lista_aguas, name='lista_aguas_por_categoria'),
    path('produto/<int:id>/', views.exibe_agua, name='exibe_agua'),
    path('sobre.html', views.sobre, name='sobre'),
    path('cadastro.html', views.novo, name='cadastro'),
    path('listaadmin.html', views.adminlist, name='adminlist'),
    path('admin.html', views.admin, name='admin'),
    path('busca.html', views.busca, name='busca'),
    path(r'<int:id>/update', views.atualiza, name='atualiza'),
    path(r'<int:id>/delete', views.deleta, name='deleta'),
    path('busca.html', views.busca, name='busca'),
    path('register.html', views.register, name='register'),
    path('logout', views.logout_user, name='logout_user')
]




# ####################################################################################################################
# Path converters¶
# The following path converters are available by default:
#
# str - Matches any non-empty string, excluding the path separator, '/'. This is the default if a converter isn’t included in the expression.
# int - Matches zero or any positive integer. Returns an int.
# slug - Matches any slug string consisting of ASCII letters or numbers, plus the hyphen and underscore characters. For example, building-your-1st-django-site.
# uuid - Matches a formatted UUID. To prevent multiple URLs from mapping to the same page, dashes must be included and letters must be lowercase. For example, 075194d3-6885-417e-a8a8-6c931e272f00. Returns a UUID instance.
# path - Matches any non-empty string, including the path separator, '/'. This allows you to match against a complete URL path rather than just a segment of a URL path as with str.
# ####################################################################################################################

# ####################################################################################################################
# Registering custom path converters
# For more complex matching requirements, you can define your own path converters.
#
# A converter is a class that includes the following:
#
# A regex class attribute, as a string.
# A to_python(self, value) method, which handles converting the matched string into the type that should be passed to the view function. It should raise ValueError if it can’t convert the given value.
# A to_url(self, value) method, which handles converting the Python type into a string to be used in the URL.
# For example:
#
# class FourDigitYearConverter:
#     regex = '[0-9]{4}'
#
#     def to_python(self, value):
#         return int(value)
#
#     def to_url(self, value):
#         return '%04d' % value
# ####################################################################################################################

# ####################################################################################################################
# Register custom converter classes in your URLconf using register_converter():
#
# from django.urls import register_converter, path
#
# from . import converters, views
#
# register_converter(converters.FourDigitYearConverter, 'yyyy')
#
# urlpatterns = [
#     path('articles/2003/', views.special_case_2003),
#     path('articles/<yyyy:year>/', views.year_archive),
#     ...
# ]
# ####################################################################################################################

# ####################################################################################################################
# Using regular expressions¶
# If the paths and converters syntax isn’t sufficient for defining your URL patterns, you can also use regular expressions. To do so, use re_path() instead of path().
#
# In Python regular expressions, the syntax for named regular expression groups is (?P<name>pattern), where name is the name of the group and pattern is some pattern to match.
#
# Here’s the example URLconf from earlier, rewritten using regular expressions:
#
# from django.urls import path, re_path
#
# from . import views
#
# urlpatterns = [
#     path('articles/2003/', views.special_case_2003),
#     re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
#     re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
#     re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),
# ]
# ####################################################################################################################
