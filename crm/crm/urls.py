"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('App.accounts.urls','accounts'))),

    #Change password
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
Necesitamos 4 vistas diferentes:

password_reset : formulario donde el usuario envía la dirección de correo electrónico

password_reset_done : Página que se muestra al usuario después de enviar el formulario de correo electrónico. Por lo general, con instrucciones para abrir la cuenta de correo electrónico, buscar en la carpeta de correo no deseado, etc. Y pedirle al usuario que haga clic en el enlace que recibirá.

password_reset_confirm : el enlace que se envió por correo electrónico al usuario. Esta vista validará el token y mostrará un formulario de contraseña si el token es válido o un mensaje de error si el token no es válido (por ejemplo, ya se usó o venció).

password_reset_complete : página que se muestra al usuario después de que la contraseña se haya cambiado correctamente.
"""