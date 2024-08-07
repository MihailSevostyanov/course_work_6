import bleach
import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f'/media/{path}'
    return '#'


def markdown_comment(value):
    return bleach.clean(
        markdown.markdown(value, extensions=['nl2br']),
        strip=True,
        tags=['strong', 'p', 'b', 'li', 'blockquote', 'br'])


@register.filter
def comment_markdown(value):
    return mark_safe(markdown_comment(value))
