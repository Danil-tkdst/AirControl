from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView
from .models import *
from django.db.models import Count

class GaragesShow(ListView):
    """
    Представление для отображения списка ангаров с количеством воздушных судов в каждом ангаре.

    :attribute queryset: Запрос для получения списка ангаров с подсчетом числа воздушных судов в каждом ангаре.
    :attribute template_name: Имя шаблона для отображения списка ангаров.
    :attribute context_object_name: Имя переменной контекста, в которой будет храниться список ангаров.
    """
    queryset = Garage.objects.annotate(num_ar=Count('arcr'))
    template_name = 'Garages.html'
    context_object_name = 'garages'

class AircraftsShow(ListView):
    """
    Представление для отображения списка воздушных судов в выбранном ангаре.

    :attribute template_name: Имя шаблона для отображения списка воздушных судов.
    :attribute context_object_name: Имя переменной контекста, в которой будет храниться список воздушных судов.
    """
    template_name = 'Aircrafts.html'
    context_object_name = 'aircrafts'

    def get_queryset(self):
        """
        Возвращает список воздушных судов в выбранном ангаре с подсчетом числа узлов и агрегатов у каждого воздушного судна.

        :return: QuerySet воздушных судов с подсчитанным числом узлов и агрегатов.
        :rtype: QuerySet
        """
        return Aircraft.objects.filter(garage_id=self.kwargs['gr_id']).annotate(num_un=Count('unt'))

class UnitsShow(ListView):
    """
    Представление для отображения списка узлов и агрегатов в выбранном воздушном судне.

    :attribute model: Модель узлов и агрегатов.
    :attribute template_name: Имя шаблона для отображения списка узлов и агрегатов.
    :attribute context_object_name: Имя переменной контекста, в которой будет храниться список узлов и агрегатов.
    """
    model = Unit
    template_name = 'Units.html'
    context_object_name = 'units'

    def get_queryset(self):
        """
        Возвращает список узлов и агрегатов в выбранном воздушном судне.

        :return: QuerySet узлов и агрегатов в выбранном воздушном судне.
        :rtype: QuerySet
        """
        return Unit.objects.filter(aircraft_id=self.kwargs['ar_id'])

def edit(request, un_id):
    """
    Представление для редактирования информации об узле или агрегате воздушного судна.

    :param request: Запрос пользователя.
    :type request: HttpRequest
    :param un_id: Идентификатор узла или агрегата.
    :type un_id: int

    :return: Ответ с формой для редактирования информации или переадресация на предыдущую страницу после сохранения.
    :rtype: HttpResponse
    """
    try:
        unt = Unit.objects.get(id=un_id)

        if request.method == "POST":
            unt.repairdate = request.POST.get("repairdate")
            unt.controldate = request.POST.get("controldate")
            unt.comment = request.POST.get("comment")
            unt.save()
            return HttpResponse('<script>history.go(-2);</script>')
        else:
            return render(request, "Edit.html", {"unt": unt})
    except Unit.DoesNotExist:
        return HttpResponseNotFound("<h2>unit not found</h2>")
