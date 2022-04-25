from django.contrib import admin
from bankingSolutuon.models import Lock2, Login
from bankingSolutuon.models import Sign
from bankingSolutuon.models import Credit
from bankingSolutuon.models import Withdraw
from bankingSolutuon.models import SendMoney
from bankingSolutuon.models import MobileRecharge
from bankingSolutuon.models import Operator
from bankingSolutuon.models import ChangePassword,Profile
# Register your models here.
admin.site.register(Login)
admin.site.register(Sign)
admin.site.register(Credit)
admin.site.register(Withdraw)
admin.site.register(SendMoney)
admin.site.register(MobileRecharge)
admin.site.register(Operator)
admin.site.register(ChangePassword)
admin.site.register(Lock2)
admin.site.register(Profile)
