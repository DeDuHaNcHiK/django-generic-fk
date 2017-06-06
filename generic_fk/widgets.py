# coding: utf-8
from itertools import chain

from django import forms
from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe


class ContentTypeSelect(forms.Select):
    def __init__(self, lookup_id='lookup_id_object_id', raw_fk='id_object_id', attrs=None, choices=()):
        self.lookup_id = lookup_id
        self.raw_fk = raw_fk
        super(ContentTypeSelect, self).__init__(attrs, choices)

    def render(self, name, value, attrs=None, renderer=None):
        output = super(ContentTypeSelect, self).render(name, value, attrs, renderer=None)

        choices = self.choices
        choiceoutput = ' var %s_choice_urls = {' % (attrs['id'],)
        for choice in choices:
            try:
                ctype = ContentType.objects.get(pk=int(choice[0]))
                choiceoutput += '    \'%s\' : \'../../../%s/?_to_field=%s\',' % (
                    str(choice[0]),
                    ctype.model,
                    ctype.model_class()._meta.pk.name
                )
            except:
                pass
        choiceoutput += '};'

        output += (
            '<script type="text/javascript">'
            '(function($) {'
            '  $(document).ready( function() {'
            '%(choiceoutput)s'
            '    $(\'#%(id)s\').change(function (){'
            '        $(\'#%(fk_id)s\').attr(\'href\',%(id)s_choice_urls[$(this).val()]);'
            '        $(\'#%(raw_fk)s\').val(\'\');'
            '        $(\'#%(raw_fk)s\').parent(\'div\').find(\'strong\').text(\'\');'
            '    });'
            '  });'
            '})(django.jQuery);'
            '</script>' % {
                'choiceoutput': choiceoutput,
                'id': attrs['id'],
                'fk_id': self.lookup_id,
                'raw_fk': self.raw_fk
            }
        )
        return mark_safe(u''.join(output))
