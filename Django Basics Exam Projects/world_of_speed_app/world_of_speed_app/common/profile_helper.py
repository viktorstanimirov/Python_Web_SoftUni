from world_of_speed_app.profiles.models import Profile


def get_profile():
    return Profile.objects.first()
