from django.shortcuts import render

from profiles.models import Profile
import logging

logger = logging.getLogger(__name__)

# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur
# ex, sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d
def index(request):
    """
        View function for displaying the list of all user profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra
# vulputate. Sed tincidunt, dolor id facilisis fringilla, eros leo
# tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi
# tristique senectus et netus et males
def profile(request, username):
    """
    View function for displaying the details of a specific user's profile.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        logger.info(f"Profile viewed: {username}")
        return render(request, 'profiles/profile.html', context)

    except Profile.DoesNotExist:
        logger.error(f"Profile for username {username} not found!")
        return render(request, '404.html', status=404)
