from django.contrib import admin
from .models import UserAccount, CustomerFeedback, Return

admin.site.register(UserAccount)
admin.site.register(CustomerFeedback)
admin.site.register(Return)
