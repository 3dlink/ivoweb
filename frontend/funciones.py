import json
def form_invalid(form):
    to_json = {}
    to_json.update(success=False)
    if form.errors:
        errors = {}
        fields = {}
        for field_name, text in form.errors.items():
            fields[field_name] = text

        errors.update(fields=fields)
        to_json.update(errors=errors)
    return to_json