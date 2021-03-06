from django.shortcuts import render_to_response
from django.template.context import RequestContext
from test_bootstrap.forms import TestForm

def test_form(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        form.is_valid()
    else:
        form = TestForm()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
    }))