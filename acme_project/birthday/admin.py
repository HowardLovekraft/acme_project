from django.contrib import admin


from .models import Birthday, Tag


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )

    empty_value_display = 'Не задано'


class TagAdmin(admin.ModelAdmin):
    empty_value_display = 'Не заданы'


admin.site.register(Birthday, BirthdayAdmin)
admin.site.register(Tag, TagAdmin)