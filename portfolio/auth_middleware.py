# portfolio/auth_middleware.py
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
import logging

# Set up logging to help debug
logger = logging.getLogger(__name__)

class Auth0Middleware(MiddlewareMixin):
    def process_request(self, request):
        # Log the current path to debug
        logger.debug(f"Auth0Middleware checking path: {request.path}")

        # Define paths that should be accessible without authentication
        public_paths = [
            '/',              # Home page
            '/login',         # Auth0 login
            '/callback',      # Auth0 callback
            '/logout',        # Logout
            '/admin',         # Django admin (already has its own auth)
            # Add any other public paths here
        ]

        # Check if the current path should be public - exact matching wasn't working
        # This may be the issue - let's be more explicit about the path matching
        if (request.path == '/'
                or any(request.path.startswith(path + '/') or request.path == path for path in public_paths)
        ):
            logger.debug(f"Path {request.path} is public, allowing access")
            return None

        # Check if path starts with /projects
        if request.path.startswith('/projects'):
            # Check if user is authenticated (has a session)
            if not request.session.get('user'):
                logger.debug(f"User not authenticated, redirecting to login")
                # User is not authenticated, redirect to login
                return redirect(reverse('login'))
            else:
                logger.debug(f"User is authenticated, allowing access to {request.path}")

        # User is authenticated or not a protected path, continue to the view
        return None