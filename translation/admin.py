from django.contrib import admin
from .models import GameClass, ClassStoryPlanet, NPCDialogue, CommonGameFile

admin.site.register(GameClass)
admin.site.register(ClassStoryPlanet)
admin.site.register(NPCDialogue)

admin.site.register(CommonGameFile)