from .models import UserProfile

def user_profile(request):
    print("Context processor function called")
    user_profile = None
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.filter(user=request.user.id).first()
        print(user_profile.is_faculty)
    return {'user_profile': user_profile}