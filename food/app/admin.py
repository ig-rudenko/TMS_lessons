from django.contrib import admin
from django.contrib.sessions.models import Session

from users.models import User
from .models import Ingredient, Recipe


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()

    list_display = ['session_key', '_session_data', 'expire_date']


class IsMemberUserFilter(admin.SimpleListFilter):
    title = 'Название фильтра'
    parameter_name = 'is_member'

    def lookups(self, request, model_admin):
        qs = User.objects.filter(is_member=True)
        return (
            (u.username, u.username) for u in qs
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(user__username=self.value())
        return queryset


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "user"]
    list_filter = [IsMemberUserFilter]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
