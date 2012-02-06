from django.db import models

from feincms import settings


class Job(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=511, blank=True, default='')
    long_description = models.TextField()
    qualifications = models.TextField(blank=True, default='')
    contact_email = models.EmailField()

    feincms_item_editor_context_processors = (
        lambda x: settings.FEINCMS_RICHTEXT_INIT_CONTEXT,
    )
    feincms_item_editor_includes = {
        'head': [settings.FEINCMS_RICHTEXT_INIT_TEMPLATE],
    }

    def __unicode__(self):
        return self.title
