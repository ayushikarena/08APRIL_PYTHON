from django.conf import settings

def project_name_processor(request):
    return {
        'PROJECT_NAME': getattr(settings, 'PROJECT_NAME', 'SmartCityHub')
    }
