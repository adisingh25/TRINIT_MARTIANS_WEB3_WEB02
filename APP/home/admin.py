from django.contrib import admin
from .models import Doctor,CERTIFICATE,certificateissue,downloadcertificate


# Register your models here.
admin.site.register(Doctor)
admin.site.register(CERTIFICATE)
admin.site.register(certificateissue)
admin.site.register(downloadcertificate)
