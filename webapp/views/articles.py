from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from cat import Pets
from cat import Menu_actions

cat1 = ""
menu_list = []

def cat_view(request: WSGIRequest):
    global cat1
    global menu_list
    if request.method == "GET":
        return render(request, 'cat.html')
    print(request.POST)
    cat_name = request.POST.get('name')
    print('cat_name=', cat_name)
    if cat1 == "":
        cat1 = Pets(cat_name)
        acts = Menu_actions()
        acts.set_menu()
        menu_list = acts.menu_act
    action = request.POST.get('action')
    if action:
        number = int(action)
        cat1.action_to_cat(number)

    curr_state = cat1.get_state()

    pict = curr_state[1] + '.jpg'
    state = curr_state[0]
    period = int(curr_state[2])
    happiness = cat1.happiness
    satiety = cat1.satiety

    context = {
        'menus': menu_list,
        'photo': pict,
        'name': cat1.name,
        'age': cat1.age,
        'happiness': happiness,
        'satiety': satiety,
        'state': state,
        'period': period,
    }
    return render(request, 'cat.html', context=context)
