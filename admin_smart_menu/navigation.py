from __future__ import unicode_literals

from django.template.loader import get_template


class Menu(object):

    @classmethod
    def get_menu(cls, context, request):
        from .templatetags.suit_menu import get_menu as suit_get_menu
        context['app_list'] = suit_get_menu(context, request)
        return get_template('admin/smart_menu.html').render(context.flatten())
