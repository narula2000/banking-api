from django.contrib.auth.models import User

all_users = User.objects.all()
non_admin_users = all_users.exclude(is_superuser=True)
non_staff_users = non_admin_users.exclude(is_staff=True)

for user in non_staff_users:
    user.delete()
