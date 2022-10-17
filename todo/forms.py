from dataclasses import fields
from distutils.log import error
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status')
        labels = {
            'title': _('Judul'),
            'description': _('Description'),
            'status': _('Status')
        }

        error_message = {
            'title': {
                'required': _("Judul harus diisi"),
            },
            'description':{
                'required': _("Deskripsi harus diisi")
            },
        }