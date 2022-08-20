from django import template
import markdown
from django.utils.safestring import mark_safe

from store.models import Category, Store

register = template.Library()


@register.simple_tag
def get_all_categories():
    return Category.objects.all()


@register.simple_tag
def get_all_products(category_id=None):
    return Store.objects.all() if not category_id else Store.objects.filter(category_id=category_id)


@register.simple_tag
def get_menu():
    return [{"title": "Login", "url_name": "login"},
            {"title": "Support", "url_name": "support"},
            {"title": "About", "url_name": "about"}]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
