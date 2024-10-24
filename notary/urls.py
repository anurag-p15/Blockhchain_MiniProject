from django.urls import path, re_path  # Updated import

from notary.views import (
    home,
    about,
    ajax_set_ongoing_submissions,
    ajax_list_transaction_history,
    ajax_set_proof,
    ajax_send_mail,
    ajax_get_document_data
)
from profile.views import auth, register, user_logout

urlpatterns = [
    # Common views
    path('', home, name='home'),  # Updated to use path
    path('about/', about, name='about'),  # Updated to use path

    # AJAX views
    path('ajax/ongoing_submissions/', ajax_set_ongoing_submissions, name='ajax_set_ongoing_submissions'),  # Updated to use path
    path('ajax/proof/', ajax_set_proof, name='ajax_set_proof'),  # Updated to use path
    path('ajax/history/list/', ajax_list_transaction_history, name='ajax_list_transaction_history'),  # Updated to use path
    path('ajax/send-mail/', ajax_send_mail, name='ajax_send_mail'),  # Updated to use path
    path('ajax/document-data/', ajax_get_document_data, name='ajax_get_document_data'),  # Updated to use path

    # User profile views
    path('login/', auth, name='login'),  # Updated to use path
    path('register/', register, name='register'),  # Fixed name from 'login' to 'register'
    path('logout/', user_logout, name='logout'),  # Updated to use path
]
