from collections import namedtuple

Location = namedtuple('Location', 'latitude longitude timezone')

locations = {
    'Los Angeles': Location(latitude=34.052234, longitude=-118.243685, timezone='America/Los_Angeles'),
    'New York City': Location(latitude=40.712775, longitude=-74.005973, timezone='America/New_York'),
    # 'London': Location(latitude=51.507351, longitude=-0.127758)
}
