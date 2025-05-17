from django.shortcuts import redirect, render
from landing_qatar import settings
from .forms import ConsultationRequestForm
from django.utils import translation
from django.views.decorators.http import require_GET


def index(request):
    # 1) Достаём код языка из сессии (его кладёт туда switch_language)
    lang_code = request.session.get(translation.LANGUAGE_SESSION_KEY)
    # 2) Если есть — активируем его непосредственно сейчас
    if lang_code:
        translation.activate(lang_code)
        request.LANGUAGE_CODE = lang_code

    # далее — ваша обычная логика
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
    nxt  = request.GET.get("next", "/")
    if lang in dict(settings.LANGUAGES):
        request.session[translation.LANGUAGE_SESSION_KEY] = lang
        translation.activate(lang)
    return redirect(nxt)