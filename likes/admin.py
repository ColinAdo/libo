from django.contrib import admin

from .models import LikeReview

# Like reviews admin
class LikeReviewAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'review',
        'date',
    ]


admin.site.register(LikeReview, LikeReviewAdmin)
