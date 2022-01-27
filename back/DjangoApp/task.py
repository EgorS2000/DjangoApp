from __future__ import absolute_import, unicode_literals

import os
from datetime import datetime, timedelta
from celery import shared_task
from django import setup
from django.contrib.auth.models import User

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'DjangoApp.settings'
)
setup()


@shared_task(name="test", type="test", ignore_result=True)
def test():
    deleted_accounts = []
    for user in User.objects.all():
        if user.last_login:
            if datetime.utcnow() - user.last_login > timedelta(days=7):
                deleted_accounts.append(user)
    if deleted_accounts:
        for user in deleted_accounts:
            user.delete()
        return "Accounts deleted successful"

    else:
        return "No accounts to delete"
