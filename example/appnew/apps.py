from django.apps import AppConfig


class AppnewConfig(AppConfig):
    name = 'example.appnew'

    def ready(self):
        import example.appnew.signals #noqa
