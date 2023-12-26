from typing import Any
from django.utils import timezone
from .models import Visitor

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def update_or_create_visitor(self, ip_address):
        visitor, created = Visitor.objects.get_or_create(ip_address=ip_address)
        if not created:
            visitor.last_visit = timezone.now()
            visitor.save()

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_anonymous:
            ip_address = self.get_client_ip(request)
            self.update_or_create_visitor(ip_address)
        
        return response
    
