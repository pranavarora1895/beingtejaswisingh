from contactme.models import MyInfo

def subject_renderer(request):
    return {
        'my_info': MyInfo.objects.order_by('-created_date').first(),
    }