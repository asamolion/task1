from datetime import datetime


class Record:
    """ Represents a single weather record in the madrid csv file """

    def __init__(self,
                 date,
                 max_temp, mean_temp, min_temp,
                 max_dew, mean_dew, min_dew,
                 max_humidity, mean_humidity, min_humidity,
                 max_sea_pressure, mean_sea_pressure, min_sea_pressure,
                 max_visibility, mean_visibility, min_visibility,
                 max_wind_speed, mean_wind_speed,
                 max_gust_speed,
                 precipitation,
                 cloud_cover,
                 events,
                 wind_direction):
        """ Constructor function

        Keyword arguments:
        date -- datetime object (YYYY-MM-DD)
        max_temp, mean_temp, min_temp --  unit (Celsius)
        max_dew, mean_dew, min_dew -- unit (Celsius)
        max_humidity, mean_humidity, min_humidity -- value of humidity
        max_sea_pressure, mean_sea_pressure, min_sea_pressure -- unit (Pascal)
        max_visibility, mean_visibility, min_visibility -- unit (km)
        max_wind_speed, mean_wind_speed -- unit (km/h)
        max_gust_speed -- unit (km/h)
        precipitation -- unit (mm)
        cloud_cover -- unit (okta)
        events -- list of weather related eventsax
        wind_direction -- unit (degrees
        """
        self.date = datetime.strptime(
            ' '.join(date.split('-')), "%Y %m %d").date()
        self.max_wind_speed = int(max_wind_speed)
        self.mean_wind_speed = int(mean_wind_speed)
        self.max_gust_speed = int(
            max_gust_speed) if max_gust_speed.isdigit() else 0
        self.precipitation = float(precipitation)
        self.cloud_cover = int(cloud_cover) if cloud_cover.isdigit() else 0
        self.events = events.split('-')
        self.wind_direction = int(
            wind_direction) if wind_direction.isdigit() else 0
        self.data_dict = {
            'date': self.date,
            'max_temp': int(max_temp) if max_temp.isdigit() else 0,
            'mean_temp': int(mean_temp) if mean_temp.isdigit() else 0,
            'min_temp': int(min_temp) if min_temp.isdigit() else 0,
            'max_dew': int(max_dew) if max_temp.isdigit() else 0,
            'mean_dew':  int(mean_dew) if mean_temp.isdigit() else 0,
            'min_dew': int(min_dew) if min_temp.isdigit() else 0,
            'max_humidity': int(max_humidity) if max_humidity.isdigit() else 0,
            'mean_humidity':  int(mean_humidity) if mean_humidity.isdigit() else 0,
            'min_humidity': int(min_humidity) if max_humidity.isdigit() else 0,
            'max_sea_pressure': int(max_sea_pressure),
            'mean_sea_pressure': int(mean_sea_pressure),
            'min_sea_pressure': int(min_sea_pressure),
            'max_visibility': int(max_visibility) if max_visibility.isdigit() else 0,
            'mean_visibility': int(mean_visibility) if mean_visibility.isdigit() else 0,
            'min_visibility': int(min_visibility) if min_visibility.isdigit() else 0
        }

    def __iter__(self):
        """ iterator method """
        return iter([self.date,
                     self.data_dict['max_temp'], self.data_dict['mean_temp'],
                     self.data_dict['min_temp'], self.data_dict['max_dew'],
                     self.data_dict['mean_dew'], self.data_dict['min_dew'],
                     self.data_dict['max_humidity'], self.data_dict['mean_humidity'],
                     self.data_dict['min_humidity'], self.data_dict['max_sea_pressure'],
                     self.data_dict['mean_sea_pressure'], self.data_dict['min_sea_pressure'],
                     self.data_dict['max_visibility'], self.data_dict['mean_visibility'],
                     self.data_dict['min_visibility'], self.max_wind_speed,
                     self.mean_wind_speed, self.max_gust_speed,
                     self.precipitation, self.cloud_cover, self.events, self.wind_direction])


""" Utility functions """


def mean(numbers):
    """ returns the mean of a list of numbers """
    return int(sum(numbers)) / max(len(numbers), 1)
