from django.core.exceptions import PermissionDenied    
from django.utils.deprecation import MiddlewareMixin

class FilterIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        allowed_ips = ['127.0.0.1','192.168.1.1', '123.123.123.123',] 
        ip = request.META.get('REMOTE_ADDR') 
        if ip not in allowed_ips:
            raise PermissionDenied
        return None