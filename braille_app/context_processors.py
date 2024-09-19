from .models import UserProfile

def user_profile(request):
    user_profile = None
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.filter(user=request.user.id).first()
       
    return {'user_profile': user_profile}