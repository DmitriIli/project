from .models import Machine


def get_titles(data):
    """Получить заголовки таблицы"""
    ls = [item for item in data[0].keys()]

    titles = [Machine._meta.get_field(
        f'{name}').verbose_name for name in ls]
    return titles


def get_machine_list_for_is_anonymous():
    """ возвращает список машин для неавторизованного пользователя"""
    context, data = {}, []

    data = Machine.objects.all().values('modelMachine', 'factoryNumberMachine', 'engine', 'factoryNumberEngine', 'transmission',
                                        'factoryNumberTransmission', 'driveAxel', 'factoryNumberDriveAxel', 'steringAxel', 'factoryNumberSteringAxel')

    context = {'data': data, 'titles': get_titles(data)}
    return context


def get_machine_list_for_client(user):
    """ возвращает список машин для клиента"""
    context, data = {}, []
    data = Machine.objects.filter(
        client__clientuser__user=user).values()
    context = {'data': data, 'titles': get_titles(data)}
    return context


def get_machine_list_for_service_company_user(user):
    """ возвращает список машин для серивисной компании"""
    context, data = {}, []
    data = Machine.objects.filter(
        serviceCompany__servicecompanyuser__user=user).values()
    context = {'data': data, 'titles': get_titles(data)}
    return context


def get_machine_list_for_manager():
    """ возвращает список машин для менеджера"""
    context, data = {}, []
    data = Machine.objects.all().values()
    context = {'data': data, 'titles': get_titles(data)}
    return context


def get_machines_list_by_users_group(user):
    """ возвращает список машин в зависимости от прав пользователя"""
    context, data, titles = {}, [], []
    print(type(user))
    print(user)
    if user.is_anonymous:
        data = Machine.objects.all().values('modelMachine', 'factoryNumberMachine', 'engine', 'factoryNumberEngine', 'transmission',
                                            'factoryNumberTransmission', 'driveAxel', 'factoryNumberDriveAxel', 'steringAxel', 'factoryNumberSteringAxel')
    elif user.groups.filter(name='Client').count():
        data = Machine.objects.filter(
            client__clientuser__user=user).values()

    elif user.groups.filter(name='ServiceCompany').count():
        data = Machine.objects.filter(
            serviceCompany__servicecompanyuser__user=user).values()

    elif user.groups.filter(name='Manager').count():
        data = Machine.objects.all().values()

    else:
        print(f'root')

    ls = [item for item in data[0].keys()]

    titles = [Machine._meta.get_field(
        f'{name}').verbose_name for name in ls]

    context = {'data': data, 'titles': titles}
    return context


def get_titles(data):
    """Получить заголовки таблицы"""
    ls = [item for item in data[0].keys()]

    titles = [Machine._meta.get_field(
        f'{name}').verbose_name for name in ls]
    return titles
