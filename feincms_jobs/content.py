from django.db import models
from django.template.loader import render_to_string

from models import Job


class JobContent(models.Model):
    job = models.ForeignKey(Job)

    class Meta:
        abstract = True

    def render(self):
        context = {'job': self.job}
        template_names = (
                'feincms_jobs/job_detail_%d.html' % self.job.pk,
                'feincms_jobs/job_detail.html'
        )
        return render_to_string(template_names, context)
