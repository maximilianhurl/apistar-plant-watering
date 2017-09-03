from apistar import Include, Route, typesystem
from apistar.backends import django_orm
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
from constants import WATER_PERIOD_CHOICES
from typing import List


# types

class WaterPeriod(typesystem.Enum):
    enum = list([choice[0] for choice in WATER_PERIOD_CHOICES])


class Plant(typesystem.Object):
    properties = {
        'id': typesystem.string(max_length=100),
        'name': typesystem.string(max_length=500),
        'water_period': WaterPeriod,
    }


class WriteablePlant(typesystem.Object):
    properties = {
        'name': typesystem.string(max_length=500),
        'water_period': WaterPeriod,
    }


# views

def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def list_plants(session: django_orm.Session) -> List[Plant]:
    queryset = session.Plant.objects.all()
    return [Plant(plant) for plant in queryset]


def create_plant(session: django_orm.Session, plant: WriteablePlant) -> Plant:
    if plant:
        new_plant = session.Plant.objects.create(**plant)
        return Plant(new_plant)
    return {'message': 'Plant object required'}


# settings

routes = [
    Route('/', 'GET', welcome),
    Route('/plants', 'GET', list_plants),
    Route('/plants', 'POST', create_plant),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

settings = {
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'plantstar',
            'HOST': 'localhost',
            'USER': '',
            'PASSWORD': ''
        }
    },
    'INSTALLED_APPS': ['django_project', ]
}

app = App(
    routes=routes,
    settings=settings,
    commands=django_orm.commands,
    components=django_orm.components
)


if __name__ == '__main__':
    app.main()
