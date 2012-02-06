from feincms import settings
from django.contrib import admin
from django import forms

from models import Job


class JobAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobAdminForm, self).__init__(*args, **kwargs)
        self.fields['long_description'].widget.attrs.update({'class': 'item-richtext'})
        self.fields['qualifications'].widget.attrs.update({'class': 'item-richtext'})


class JobAdmin(admin.ModelAdmin):

    form = JobAdminForm

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context['model'] = obj
        return super(JobAdmin, self).render_change_form(request, context, add, change, form_url, obj)

    def change_view(self, request, object_id, extra_context=None):
        extra_context = {
            'FEINCMS_ADMIN_MEDIA': settings.FEINCMS_ADMIN_MEDIA,
            'FEINCMS_ADMIN_MEDIA_HOTLINKING': settings.FEINCMS_ADMIN_MEDIA_HOTLINKING,
            'FEINCMS_JQUERY_NO_CONFLICT': settings.FEINCMS_JQUERY_NO_CONFLICT,
        }
        extra_context.update(settings.FEINCMS_RICHTEXT_INIT_CONTEXT)
        return super(JobAdmin, self).change_view(request, object_id, extra_context)


admin.site.register(Job, JobAdmin)
