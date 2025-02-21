from django.shortcuts import render, get_object_or_404, redirect
from .models import Character

""" Create your views here. """
# Menampilkan daftar karakter
def character_list(request):
    characters = Character.objects.all()
    return render(request, 'character_list.html', {'characters': characters})

# Menampilkan detail karakter
def character_detail(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    return render(request, 'character_detail.html', {'character': character})

# Menambahkan karakter baru
def add_character(request):
    if request.method == "POST":
        name = request.POST.get('name')
        level = request.POST.get('level', 1)
        hp = request.POST.get('hp', 100)
        atk = request.POST.get('atk', 10)
        defense = request.POST.get('defense', 5)
        spd = request.POST.get('spd', 10)
        stm = request.POST.get('stm', 50)
        mtx = request.POST.get('mtx', 5)

        Character.objects.create(
            name=name, level=level, hp=hp, atk=atk, defense=defense,
            spd=spd, stm=stm, mtx=mtx
        )
        return redirect('character_list')

    return render(request, 'add_character.html')
