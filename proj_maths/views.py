from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
from . import cards_work


def index(request):
    return render(request, "index.html")


def terms_list(request):
    cards = cards_work.get_cards_for_table()
    print(cards)
    return render(request, "term_list.html", context={"cards": cards})


def cards_list(request):
    cards = cards_work.get_cards_for_table()
    return render(request, "cards_list.html", context={"cards": cards})


def add_term(request):
    return render(request, "term_add.html")


def catch_card(request):
    if request.method == "POST":
        cache.clear()
        result_idx = request.body.decode('UTF-8').split("=")[1]
        cards_work.modify_card(result_idx, 1)



def send_card(request):
    if request.method == "POST":
        cache.clear()
        new_source = request.POST.get("new_source", "")
        new_target = request.POST.get("new_target", "").replace(";", ",")
        context = {}
        if len(new_source) == 0:
            context["success"] = False
            context["comment"] = "Введите русское слово"
        elif len(new_target) == 0:
            context["success"] = False
            context["comment"] = "Введите английский перевод"
        else:
            response = cards_work.write_card(new_source, new_target)
            if not response:
                context["success"] = True
                context["comment"] = "Слово успешно добавлено!"
            else:
                context["success"] = False
                context["comment"] = "Такое слово уже есть!"

        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        add_term(request)


def show_stats(request):
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", stats)
