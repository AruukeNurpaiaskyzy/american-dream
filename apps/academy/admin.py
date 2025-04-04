from django.contrib import admin
from apps.academy.models import Settings, Contacts, Achievement, Teacher, AboutPage, AboutObjects, AboutObjects2, CoursesProgram, Courses

# Register your models here.
admin.site.register(Settings)
# admin.site.register(Course)
admin.site.register(Contacts)
class AchievementInline(admin.TabularInline):
    model = Achievement
    extra = 1

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience')
    inlines = [AchievementInline]

admin.site.register(AboutPage)
admin.site.register(AboutObjects)
admin.site.register(AboutObjects2)
class CoursesProgramInline(admin.TabularInline):
    model = CoursesProgram
    extra = 1
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'direction', 'price', 'monthly_price')
    inlines = [CoursesProgramInline]