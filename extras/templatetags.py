from django import template
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
 
 
register = template.Library()
 
@register.simple_tag(takes_context = True)
def navlink(context, url, text, **extra):
    path = context['path']
    if path == url:
        return text
    
    if url == "index.html": # specal case
        url = "/"
    return '<a href="%s">%s</a>' % (url, text)


