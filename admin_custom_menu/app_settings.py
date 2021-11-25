from django.conf import settings

NAVIGATION_CLASS = getattr(settings, 'NAVIGATION_CLASS', 'admin_custom_menu.navigation.Menu')
