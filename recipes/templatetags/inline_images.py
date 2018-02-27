import re

from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()
from recipes.models import Image

regex = re.compile(r'\[inline (?P<name>[\-\w]+)\]')

@register.filter
@stringfilter
def inline_images(value):
    new_value = value
    it = regex.finditer(value)
    for m in it:
        try:
            image = Image.objects.get(name=name)
            new_value = new_value.replace(m.group(), '<img src="%s%s" width="%d" height="%d" alt="%s" /><p><em>%s</em></p>' % ('http://mysite.com', thumbnail.absolute_url, thumbnail.width(), thumbnail.height(), image.title, image.title))
        except InlineImage.DoesNotExist:
            pass
    return new_value