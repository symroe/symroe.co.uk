import re
from django import template
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
import markdown2
from markdown_deux.conf import settings

EXTRAS = [
    'header-ids',
    'footnotes',
    'smarty-pants',
    
]

register = template.Library()

@register.tag(name="markdown")
def markdown_tag(parser, token):
    nodelist = parser.parse(('endmarkdown',))
    bits = token.split_contents()
    parser.delete_first_token() # consume '{% endmarkdown %}'
    return MarkdownNode(nodelist)

class MarkdownNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        value = self.nodelist.render(context)
        try:
            return mark_safe(markdown2.markdown(value, extras=EXTRAS))
        except ImportError:
            if settings.DEBUG:
                raise template.TemplateSyntaxError("Error in `markdown` tag: "
                    "The python-markdown2 library isn't installed.")
            return force_unicode(value)

