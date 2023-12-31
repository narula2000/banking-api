from django.contrib.auth.models import User

all_users = User.objects.all()
non_admin_non_staff_users = all_users.exclude(is_superuser=True, is_staff=True)

for user in non_admin_non_staff_users:
    user.delete()
