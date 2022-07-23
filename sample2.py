from notice_pressure.app.pressure.infrastructure.pressurerepositoryImpl import (
    PressureRepositoryImpl,
)
import os


os.environ["OPEN_WEATHER_API_TOKEN"] = "94ddc164a4fcb492bee7658f350f47ed"

repository = PressureRepositoryImpl()

print(repository.get_tomorrow_list())
