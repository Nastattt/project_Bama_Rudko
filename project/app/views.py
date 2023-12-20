from django.shortcuts import render, get_object_or_404, redirect

from .forms import FilmForm
from .models import Film


# Вывод всех фильмов
def all_films(request):
    films = Film.objects.all()
    return render(request, 'all_films.html', {'films': films})


# Вывод одного фильма по pk
def detail_film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'detail_film.html', {'film': film})


# Создание одного фильма
def create_film(request):
    if request.method == 'POST':
        # Если пришел POST запрос, то проверяем поля из формы на валидность
        form = FilmForm(request.POST)
        if form.is_valid():
            # Если данные валидны, то создаем объект
            form.save()
            return redirect("all-films")
    else:
        # Если отправляем GET запрос, то просто отрисовывается пустая форма
        form = FilmForm()
    return render(request, 'add_film.html', {'form': form})


# Редактирование фильма по pk
def edit_film(request, pk):
    film = get_object_or_404(Film, pk=pk)

    if request.method == 'POST':
        # Либо сохраним новые данные (request.POST),
        # либо сохраним те, что получили из объекта film (instance=film)
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect("all-films")
    else:
        # Форма заполнится данными из полученного объекта film
        form = FilmForm(instance=film)

    return render(request, 'edit_film.html', {'form': form})


# Удаление фильма по pk
def delete_film(request, pk):
    film = get_object_or_404(Film, pk=pk)

    if request.method == 'POST':
        film.delete()
        return redirect('all-films')

    return render(request, 'delete_film.html', {'film': film})