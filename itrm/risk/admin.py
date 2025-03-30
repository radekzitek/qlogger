from django.contrib import admin
from .models import RiskCategoryLevel1, RiskCategoryLevel2, Risk, Asset, Control, MitigationAction, ProgressTracking, Tag

admin.site.register(RiskCategoryLevel1)
admin.site.register(RiskCategoryLevel2)
admin.site.register(Risk)
admin.site.register(Asset)
admin.site.register(Control)
admin.site.register(MitigationAction)
admin.site.register(ProgressTracking)
admin.site.register(Tag)
