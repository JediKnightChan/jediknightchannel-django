from django.db import models
from .dialogue_parser import parse_dual_lang_xml_file, parse_dual_lang_json_file


def dialogue_file_upload(instance, filename):
    return 'translation/{0}/{1}'.format(instance.to_path(), filename)


class GameClass(models.Model):
    """Game class, such as Sith Inquisitor or Jedi Knight."""
    ru_name = models.CharField(max_length=50)
    en_name = models.CharField(max_length=50)
    index = models.PositiveSmallIntegerField()
    fraction = models.CharField(max_length=20)

    def __str__(self):
        return self.ru_name


class ClassStoryPlanet(models.Model):
    """Planet, where class story takes action, such as Tython or Korriban."""
    parent_game_class = models.ForeignKey(GameClass, on_delete=models.CASCADE, related_name="planets")
    ru_name = models.CharField(max_length=50)
    en_name = models.CharField(max_length=50)
    index = models.PositiveSmallIntegerField()

    def __str__(self):
        return "{}: {}".format(self.parent_game_class.ru_name, self.ru_name)


class NPCDialogue(models.Model):
    """Conversation with NPC, such as Lord Zash or Overseer Harkun."""
    parent_planet = models.ForeignKey(ClassStoryPlanet, on_delete=models.CASCADE, related_name="dialogues")
    npc_name = models.CharField(max_length=100)
    dialogue_file = models.FileField(upload_to=dialogue_file_upload)

    def __str__(self):
        return "{}/{}/{}".format(self.parent_planet.parent_game_class, self.parent_planet, self.npc_name)

    def to_path(self):
        class_dir = self.parent_planet.parent_game_class.en_name
        planet_dir = self.parent_planet.en_name
        return "{}/{}".format(class_dir, planet_dir)

    def get_dialogue_strings_pairs(self):
        return parse_dual_lang_xml_file(self.dialogue_file.path)


class CommonGameFile(models.Model):
    """Text game file containing general information, such as names of NPC or class skills."""
    name = models.CharField(max_length=50, unique=True)
    content_file = models.FileField(upload_to="translation/common/")

    def __str__(self):
        return self.name

    def get_content_strings_pairs(self):
        return parse_dual_lang_json_file(self.content_file.path)