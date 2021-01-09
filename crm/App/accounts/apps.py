from django.apps import AppConfig

class AccountsConfig(AppConfig):
    name = 'App.accounts'

    def ready(self):
        import App.accounts.signals