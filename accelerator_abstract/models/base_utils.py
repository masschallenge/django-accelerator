
def finalist_startup_member(user):
    for member in user.startupteammember_set.all():
        if member.startup.is_finalist():
            return True
    return False
