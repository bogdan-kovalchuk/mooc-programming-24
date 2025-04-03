import math
from itertools import combinations


def get_station_data(filename: str) -> dict:
    with open(filename) as f:
        next(f)
        stations = {}
        for station in f:
            station = station.split(";")
            stations[station[3]] = (float(station[0]), float(station[1]))
    return stations


def distance(stations: dict, station1: str, station2: str) -> float:
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km


def greatest_distance(stations: dict) -> tuple:
    return max(
        ((s1, s2, distance(stations, s1, s2)) for s1, s2 in combinations(stations, 2)),
        key=lambda x: x[2],
    )
