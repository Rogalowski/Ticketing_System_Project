"""Ticket_System_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static  # static ROOT import
from django.conf import settings  # static ROOT import
from ticket_app.views import HomeView, TicketCreate, TicketView, TicketEditView, \
    TicketList, UserLoginView, UserLogoutView, UserDetailsView, UserSettingsEditView, \
        CorrespondenceDeleteView, RegisterView, activate_user



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home_index"),
    path('tickets/<str:department>/', TicketList.as_view(), name="ticket_list"),
    path('create_ticket/', TicketCreate.as_view(), name="ticket_create"),
    # path('ticket/<int:ticket_id>/create_corespondence', TicketCorespondenceCreate.as_view(), name="corespondence_create"),  # Creation View migrates tt direct, TicketView
    path('ticket/<int:ticket_id>', TicketView.as_view(), name="ticket"),
    path('ticket_edit/<int:ticket_id>', TicketEditView.as_view(), name="ticket_edit"),
    # path('ticket_edit2/<int:ticket_id>', TicketEditView2.as_view(), name="ticket_edit2"),
    path('ticket/<int:ticket_id>/delete/<int:correspondence_id>', CorrespondenceDeleteView.as_view(), name="correspondence_delete"),

    path('login_home/', UserLoginView.as_view(), name="user_login_home"),
    path('logout_home/', UserLogoutView.as_view(), name="user_logout_home"),
    path('user_details/<str:current_user>/', UserDetailsView.as_view(), name="user_details"),
    path('user_edit_settings/<str:current_user>/', UserSettingsEditView.as_view(), name="user_edit_settings"),
    path('register/', RegisterView.as_view(), name="register_view"),
    path('activate_user/<uidb64>/<token>',  activate_user, name="activate"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # static files ROOT
