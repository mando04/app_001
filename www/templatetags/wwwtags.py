from django import template
from django.template.defaultfilters import stringfilter, register
import sys
from django.core.urlresolvers import reverse
from www.models import www

register = template.Library()

@register.filter
@stringfilter
def lower(value):
    sys.stdout("Converting {0} to Lowercase".format(value))
    return value.lower()


@register.simple_tag
def is_page_active(request, value):
    if request.path == reverse(value):
        return "active"
    else:
        return ""
@register.simple_tag
def about_page():
    about = www.objects.get(id=1)
    return about.about

@register.simple_tag
def about_page_extended():
    about = www.objects.get(id=1)
    return about.about_extended

@register.simple_tag
def page_title():
    return "<h1>{0}</h1>".format(www.objects.get(id=1).title)

@register.simple_tag
def site_desc():
    return "My simple Django blog!"