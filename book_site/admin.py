from django.contrib import admin
from .models import bookCategory,writers,images,review,UserRank,User,UserAccount

# Register your models here.


admin.site.register(images)

admin.site.register(bookCategory)

class writersAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
admin.site.register(writers,writersAdmin)

class reviewAdmin(admin.ModelAdmin):
    search_fields = ["main_title", "book_title"]
admin.site.register(review,reviewAdmin)

class userAccountAdmin(admin.ModelAdmin):
    search_fields = ["worker"]
admin.site.register(UserAccount, userAccountAdmin)

admin.site.register(User)

admin.site.register(UserRank)

admin.site.site_header = "書帳網頁"