from django.contrib import admin


from .models import Birthday


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )

    empty_value_display = 'Не задано'


admin.site.register(Birthday, BirthdayAdmin)
