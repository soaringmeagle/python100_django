from django.contrib import admin

# Register your models here.

from .models import Teacher, Subject


class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'sex', 'birth', 'good_count')
    search_fields = ('name',)
    ordering = ('no',)


class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'intro', 'is_hot')
    search_fields = ('name',)
    ordering = ('no',)


admin.site.register(Teacher, TeacherModelAdmin)
admin.site.register(Subject, SubjectModelAdmin)
