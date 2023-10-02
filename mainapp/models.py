import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Garage(models.Model):
    """
    Модель ангара авиакомпании.

    :param name: Название ангара
    :type name: str
    """
    name = models.CharField(max_length=255, verbose_name='Название ангара')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Возвращает абсолютный URL для данного ангара.
        :return: Абсолютный URL ангара
        :rtype: str
        """
        return reverse('garage', kwargs={'gr_id': self.pk})

    def bool_fix(self):
        """
        Проверяет, нуждается ли ангар в ремонте (наличие ВС в ангаре, требующих ремонта).
        :return: True, если требуется ремонт, иначе False
        :rtype: bool
        """
        query = Aircraft.objects.all()
        for item in query:
            if item.garage_id == self.pk:
                if item.bool_fix():
                    return True
                else:
                    return False
        return False

    def bool_control(self):
        """
        Проверяет, нуждается ли ангар в обслуживании (наличие ВС в ангаре, требующих обслуживания).
        :return: True, если требуется обслуживание, иначе False
        :rtype: bool
        """
        query = Aircraft.objects.all()
        for item in query:
            if item.garage_id == self.pk:
                if item.bool_control():
                    return True
                else:
                    return False
        return False

class Aircraft(models.Model):
    """
    Модель воздушного судна в ангаре.

    :param type: Тип ВС
    :type type: str
    :param name: Бортовой номер
    :type name: str
    :param garage: Ангар
    :type garage: Garage
    """
    type = models.CharField(max_length=255, verbose_name='Тип ВС', default='пусто')
    name = models.CharField(max_length=255, verbose_name='Бортовой номер', unique=True)
    garage = models.ForeignKey(Garage, verbose_name='Ангар', on_delete=models.CASCADE, related_name='arcr')

    def __str__(self):
        return "{} : {}".format(self.name, self.type)

    def get_absolute_url(self):
        """
        Возвращает абсолютный URL для данного воздушного судна.
        :return: Абсолютный URL воздушного судна
        :rtype: str
        """
        return reverse('arcr', kwargs={'ar_id': self.pk})

    def bool_fix(self):
        """
        Проверяет, нуждается ли воздушное судно в ремонте (наличие узлов и агрегатов, требующих ремонта).
        :return: True, если требуется ремонт, иначе False
        :rtype: bool
        """
        query = Unit.objects.all()
        for item in query:
            if item.aircraft_id == self.pk:
                if item.bool_fix():
                    return True
                else:
                    return False
        return False

    def bool_control(self):
        """
        Проверяет, нуждается ли воздушное судно в обслуживании (наличие узлов и агрегатов, требующих обслуживания).
        :return: True, если требуется обслуживание, иначе False
        :rtype: bool
        """
        query = Unit.objects.all()
        for item in query:
            if item.aircraft_id == self.id:
                if item.bool_control():
                    return True
                else:
                    return False
        return False

class Unit(models.Model):
    """
    Модель узла или агрегата воздушного судна.

    :param name: Название агрегата
    :type name: str
    :param aircraft: ВС
    :type aircraft: Aircraft
    :param parttype: Код запчасти
    :type parttype: int
    :param repairdate: Дата последнего ремонта
    :type repairdate: datetime.date
    :param controldate: Дата последнего обслуживания
    :type controldate: datetime.date
    :param time_to_fix: Интервал ремонта (дни)
    :type time_to_fix: int
    :param time_to_control: Интервал обслуживания (дни)
    :type time_to_control: int
    :param comment: Комментарий
    :type comment: str
    """
    name = models.CharField(max_length=255, verbose_name='Название агрегата', unique=False)
    aircraft = models.ForeignKey(Aircraft, verbose_name='ВС', on_delete=models.CASCADE, related_name='unt')
    parttype = models.IntegerField(verbose_name="Код запчасти", unique=False)
    repairdate = models.DateField(verbose_name='Дата последнего ремонта', default='0000-00-00')
    controldate = models.DateField(verbose_name='Дата последнего обслуживания', default='0000-00-00')
    time_to_fix = models.IntegerField(verbose_name='Интервал ремонта (дни)', default=1)
    time_to_control = models.IntegerField(verbose_name='Интервал обслуживания (дни)', default=1)
    comment = models.CharField(max_length=1000, verbose_name='Комментарий', null=True)

    def __str__(self):
        return "{} : {} : {}".format(self.name, self.aircraft.name, self.aircraft.type)

    def get_absolute_url(self):
        """
        Возвращает абсолютный URL для данного узла или агрегата.
        :return: Абсолютный URL узла или агрегата
        :rtype: str
        """
        return reverse('unt', kwargs={'un_id': self.pk})

    def calculate_fixdate(self):
        """
        Рассчитывает дату следующего ремонта.
        :return: Дата следующего ремонта
        :rtype: datetime.date
        """
        return self.repairdate + datetime.timedelta(days=self.time_to_fix)

    def calculate_controldate(self):
        """
        Рассчитывает дату следующего обслуживания.
        :return: Дата следующего обслуживания
        :rtype: datetime.date
        """
        return self.controldate + datetime.timedelta(days=self.time_to_control)

    def bool_control(self):
        """
        Проверяет, нуждается ли узел или агрегат в обслуживании (просрочено ли обслуживание).
        :return: True, если требуется обслуживание, иначе False
        :rtype: bool
        """
        controldate = self.controldate + datetime.timedelta(days=self.time_to_control)
        if controldate < datetime.date.today():
            return True
        else:
            return False

    def bool_fix(self):
        """
        Проверяет, нуждается ли узел или агрегат в ремонте (просрочен ли ремонт).
        :return: True, если требуется ремонт, иначе False
        :rtype: bool
        """
        fixdate = self.repairdate + datetime.timedelta(days=self.time_to_fix)
        if fixdate < datetime.date.today():
            return True
        else:
            return False
