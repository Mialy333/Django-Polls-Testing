from django.contrib import admin

from .models import Choice, Question

""" Une question, 3 choix """


class ChoiceInline(admin.TabularInline):
    """ TabulaInline: pour optimiser l'affichage en tableau des objets liés sans prendre trop de place """
    model = Choice
    extra = 3
    """ Penser à intégrer un test unitaire pour être sûre d'avoir uniquement 3 choix d'affiché """

class QuestionAdmin(admin.ModelAdmin):
     fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
     inlines = [ChoiceInline]
     list_display = ["question_text", "pub_date", "was_published_recently"]
     list_filter=["pub_date"]
     search_fields=["question_text"]


admin.site.register(Question, QuestionAdmin)