from django.contrib import admin
from .models import Book, Review, Profile

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'min_age', 'genre', 'location', 'rating','rec')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','age','fav_genres','bio')

admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Profile, ProfileAdmin)