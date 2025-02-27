# auth_decorators.py
from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse

def requires_auth(f):
    @wraps(f)
    def decorated(request, *args, **kwargs):
        # Check if user session exists
        if not request.session.get('user'):
            # User is not authenticated, redirect to login
            return redirect(reverse('login'))

        # User is authenticated, proceed to the view
        return f(request, *args, **kwargs)

    return decorated