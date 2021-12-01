# Django Admin Suit Menu


Main work is done and inspired by suit menu.
in this package I take out the menu ordering and adjusting syntax in a separate app to make it easy for order and adjust menus in the django admin.

How to use
----------

* Add 'admin_custom_menu' to INSTALLED_APPS
* Add menu settings to `ADMIN_MENU_CONFIG`
* Use the templatetag `{% load custom_menu %} {% render_navigation_menu %}`
* This will use the template `admin/smart_menu.html` to render the menu. Overrideable of course.


ADMIN_MENU_CONFIG example
-------------------------

Configuration sample you can use as a start:


```python

  # Django Suit configuration example

  ADMIN_MENU_CONFIG = {
      'MENU_ICONS': {
         'sites': 'icon-leaf',
         'auth': 'icon-lock',
      },
      'MENU_OPEN_FIRST_CHILD': True, # Default True
      'MENU_EXCLUDE': ('auth.group',),
      'MENU': (
          'sites',
          {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
          {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
          {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
      ),
  }
```