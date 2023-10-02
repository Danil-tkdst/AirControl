from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Garage, Aircraft, Unit
from datetime import date

class ModelsTestCase(TestCase):
    """
    Тесты для моделей в файле models.py.
    """

    def setUp(self):
        """
        Настройка данных для тестирования моделей.
        """
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Создаем тестовые данные для моделей
        self.garage = Garage.objects.create(name='Тестовый ангар')
        self.aircraft = Aircraft.objects.create(type='Тестовый тип', name='Тестовый бортовой номер', garage=self.garage)
        self.unit = Unit.objects.create(name='Тестовый агрегат', aircraft=self.aircraft, parttype=1,
                                        repairdate=date.today(), controldate=date.today(), time_to_fix=7, time_to_control=14)

    def test_garage_str(self):
        """
        Тест для метода __str__ модели Garage.
        """
        self.assertEqual(str(self.garage), 'Тестовый ангар')

    def test_aircraft_str(self):
        """
        Тест для метода __str__ модели Aircraft.
        """
        self.assertEqual(str(self.aircraft), 'Тестовый бортовой номер : Тестовый тип')

    def test_unit_str(self):
        """
        Тест для метода __str__ модели Unit.
        """
        self.assertEqual(str(self.unit), 'Тестовый агрегат : Тестовый бортовой номер : Тестовый тип')

class ViewsTestCase(TestCase):
    """
    Тесты для представлений в файле views.py.
    """

    def setUp(self):
        """
        Настройка данных для тестирования представлений.
        """
        # Создаем тестового пользователя
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Создаем тестовые данные для моделей
        self.garage = Garage.objects.create(name='Тестовый ангар')
        self.aircraft = Aircraft.objects.create(type='Тестовый тип', name='Тестовый бортовой номер', garage=self.garage)
        self.unit = Unit.objects.create(name='Тестовый агрегат', aircraft=self.aircraft, parttype=1,
                                        repairdate=date.today(), controldate=date.today(), time_to_fix=7, time_to_control=14)

    def test_garages_show_view(self):
        """
        Тест для представления GaragesShow.

        :return: None
        """
        url = reverse('garages')
        self.client.login(username='testuser', password='testpassword')  # Авторизуем пользователя
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовый ангар')

    def test_aircrafts_show_view(self):
        """
        Тест для представления AircraftsShow.

        :return: None
        """
        url = reverse('arcr', args=[self.aircraft.pk])
        self.client.login(username='testuser', password='testpassword')  # Авторизуем пользователя
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Выводим содержимое контекста для отладки
        context = response.context

        # Проверяем, что переменная 'aircraft' доступна в контексте и содержит ожидаемые данные
        self.assertIn('Тестовый бортовой номер', context)


    def test_units_show_view(self):
        """
        Тест для представления AircraftsShow.

        :return: None
        """
        url = reverse('garage', args=[self.garage.pk])
        self.client.login(username='testuser', password='testpassword')  # Авторизуем пользователя
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовый бортовой номер')

    def test_edit_view(self):
        """
        Тест для представления edit.

        :return: None
        """
        url = reverse('unt', args=[self.unit.pk])
        self.client.login(username='testuser', password='testpassword')  # Авторизуем пользователя
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
