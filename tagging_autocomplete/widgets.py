from django.conf import settings
from django.core.urlresolvers import reverse
from django.forms.widgets import TextInput
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class TagAutocomplete(TextInput):
    def render(self, name, value, attrs=None):
        if not "class" in attrs:
            attrs.update({
                "class" : "vTextField"
            })

        html = super(TagAutocomplete, self).render(name, value, attrs)

        js = render_to_string("tagging_autocomplete/install.html", {
            "field_id": attrs.get("id"),
            "api_url": reverse("tagging_autocomplete_list"),
        })

        return mark_safe("\n".join([html, js]))

    class Media:
        js_base_url = getattr(settings, 'TAGGING_AUTOCOMPLETE_JS_BASE_URL', '%sjs/' % settings.STATIC_URL)

        js = (
            '%sjquery-ui.min.js' % js_base_url,
        )

        css = {
            'screen': ('css/jquery-ui.css',),
        }
