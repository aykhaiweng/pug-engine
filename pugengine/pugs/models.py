from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import ArrayField

from core.models import BaseModel


class Pug(BaseModel):
    """
    Keeps information of a Pug
    """
    name = models.CharField(
        _("Name"),
        max_length=128,
        help_text=_("Holds the name of the Pug")
    )
    owner = models.CharField(
        _("Owner"),
        max_length=128, null=True,
        help_text=_("discord.Member.id"),
        db_index=True
    )
    players = ArrayField(
        models.CharField(max_length=128, blank=True),
        default=list, blank=True, null=True,
        help_text=_("Array of discord.Member.id(s) that belong to this Pug"),
        db_index=True
    )
    guild = models.CharField(
        _("Guild"),
        max_length=128,
        help_text=_("The discord.Guild.id that this pug was created in"),
        db_index=True
    )
    text_channel = models.CharField(
        _("Text Channel"),
        max_length=128,
        help_text=_("The discord.TextChannel.id that this pug was created in"),
        db_index=True
    )
    max_size = models.PositiveIntegerField(
        _("Max Size"), help_text=_("Holds the max size of this Pug"),
        default=10
    )
    OPEN = 1
    STARTED = 2
    CLOSED = 3
    STATUS_CHOICES = (
        (OPEN, _("Open")),
        (STARTED, _("Started")),
        (CLOSED, _("Closed")),
    )
    status = models.PositiveIntegerField(
        _("Status"),
        help_text=_("Status of this Pug"),
        choices=STATUS_CHOICES,
        default=1
    )

    class Meta:
        verbose_name = _("Pug")
        verbose_name_plural = _("Pugs")
        ordering = ['-created_at']

    def __repr__(self):
        return ("<Pug("
                f"guild={self.guild} "
                f"text_channel={self.text_channel}) "
                f"name={self.name} "
                f"owner={self.owner})"
                ")>")


class Team(BaseModel):
    """
    Keeps information of a Team
    """
    pug = models.ForeignKey(
        "Pug", verbose_name=_("Pug"),
        on_delete=models.CASCADE,
        help_text=_("Pug that this team belongs to")
    )
    name = models.CharField(
        _("Name"),
        max_length=128,
        help_text=_("Name of the Team")
    )
    captain = models.CharField(
        _("Captain"),
        max_length=128, null=True,
        help_text=_("discord.Member.id"),
        db_index=True
    )
    players = ArrayField(
        models.CharField(max_length=128, blank=True),
        default=list, blank=True, null=True,
        help_text=_("Array of discord.Member.id(s) that belong to this Team"),
        db_index=True
    )
    voice_channel = models.CharField(
        _("Voice Channel"),
        max_length=128,
        help_text=_("The discord.VoiceChannel.id that this pug will use"),
        db_index=True
    )

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")
        ordering = ['-created_at']

    def __repr__(self):
        return ("<Team("
                f"pug={self.pug} "
                f"name={self.name} "
                f"captain={self.captain} "
                f"voice_channel={self.voice_channel}"
                ")>")
