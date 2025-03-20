from .models import Company

def all_companies(request):
    companies = Company.objects.all()
    return {'companies': companies}