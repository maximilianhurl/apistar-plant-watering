# APIStar Plant Watering

Demo project for apistar that stores plant watering schedules.

## Running locally

Note: requires pyenv to be installed
    
    ./build

    createdb plantstar

    apistar run --port=8000

## Running in production

    gunicorn app:app --workers=2 --bind=0.0.0.0:8000 --pid=pid --worker-class=meinheld.gmeinheld.MeinheldWorker