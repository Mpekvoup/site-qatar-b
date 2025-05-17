from django.shortcuts import redirect, render
from landing_qatar import settings
from .forms import ConsultationRequestForm
from django.utils import translation
from django.views.decorators.http import require_GET


def index(request):
    # 1) Получаем код языка из сессии вручную
    lang_code = request.session.get('django_language')
    if lang_code:
        translation.activate(lang_code)
        request.LANGUAGE_CODE = lang_code

    if request.method == "POST":
        form = ConsultationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                "index.html",
                {"form": ConsultationRequestForm(), "success": True},
            )
    else:
        form = ConsultationRequestForm()

    return render(request, "index.html", {"form": form})


@require_GET
def switch_language(request):
    lang = request.GET.get("lang")
    nxt = request.GET.get("next", "/")
    if lang in dict(settings.LANGUAGES):
        request.session['django_language'] = lang
        translation.activate(lang)
    return redirect(nxt)
