from django.contrib import admin
from apps.academy.models import Settings, Contacts, Achievement, Teacher, AboutPage,\
 AboutObjects, AboutObjects2, CoursesProgram, Courses, CoursesModel, CoursesPage, CourseApplication, TypeCourse

# Register your models here.
admin.site.register(Settings)
admin.site.register(TypeCourse)
admin.site.register(CoursesModel)
admin.site.register(Contacts)
admin.site.register(CoursesPage)
admin.site.register(CourseApplication)
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