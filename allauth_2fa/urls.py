from django.conf.urls import url

from allauth_2fa import views

urlpatterns = [
    url(r"^two-factor-authenticate/?$",
        views.TwoFactorAuthenticate.as_view(),
        name="two-factor-authenticate"),

    url(r"^two_factor/setup/?$",
        views.TwoFactorSetup.as_view(),
        name="two-factor-setup"),

    url(r"^two_factor/backup_tokens/?$",
        views.TwoFactorBackupTokens.as_view(),
        name="two-factor-backup-tokens"),

    url(r"^two_factor/remove/?$",
        views.TwoFactorRemove.as_view(),
        name="two-factor-remove"),
]


"""
The below code, run in Django shell, can generate a new device
and give a one time code in the console if an admin gets locked
out and needs to re-enable a new device. Replace (id=1) with the
userid for the admin in question. Afterward, the admin should 
create a new device on their phone, and after verifying it delete 
the temp device created by the code below.
"""
"""

from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.oath import totp

from users.models import CustomUser as User


user = User.objects.get(id=1)
device = TOTPDevice.objects.create(user=user)
token = totp(device.bin_key)

print('user', user)
print('6 digit token', token)

"""