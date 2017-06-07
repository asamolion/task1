import csv
from record import Record
from record import mean


class CSV:
    """ Class to manipulate the CSV document """

    def __init__(self, file_name):
        """ Constructor

        Keyword arguments:
        file_name -- name/path of csv file to read
        """
        input_file = csv.DictReader(open(file_name))
        self.record_list = []
        for row in input_file:
            new_record = Record(row['date'],
                                row['max_temp'],
                                row['mean_temp'],
                                row['min_temp'],
                                row['max_dew'],
                                row['mean_dew'],
                                row['min_dew'],
                                row['max_humidity'],
                                row['mean_humidity'],
                                row['min_humidity'],
                                row['max_sea_pressure'],
                                row['mean_sea_pressure'],
                                row['min_sea_pressure'],
                                row['max_visibility'],
                                row['mean_visibility'],
                                row['min_visibility'],
                                row['max_wind_speed'],
                                row['mean_wind_speed'],
                                row['max_gust_speed'],
                                row['precipitation'],
                                row['cloud_cover'],
                                row['events'],
                                row['wind_direction'])
            self.record_list.append(new_record)

    def get_temp_data(self):
        """ returns the data of the temperature of the csv file """
        max_temp_value = max(record.max_temp for record in self.record_list)
        max_temp_date = max(
            record.date for record in self.record_list if record.max_temp == max_temp_value)
        mean_temp_value = int(
            mean(list(record.mean_temp for record in self.record_list)))
        min_temp_value = min(record.min_temp for record in self.record_list)
        min_temp_date = min(
            record.date for record in self.record_list if record.min_temp == min_temp_value)

        temp_dict = {
            'max_temp': max_temp_value,
            'max_date': max_temp_date,
            'mean_temp': mean_temp_value,
            'min_temp': min_temp_value,
            'min_date': min_temp_date
        }
        return temp_dict

    def get_dew_data(self):
        """ returns the data of the dew point of the csv file """
        max_dew_value = max(record.max_dew for record in self.record_list)
        max_dew_date = max(
            record.date for record in self.record_list if record.max_dew == max_dew_value)
        mean_dew_value = int(
            mean(list(record.mean_dew for record in self.record_list)))
        min_dew_value = min(record.min_dew for record in self.record_list)
        min_dew_date = min(
            record.date for record in self.record_list if record.min_dew == min_dew_value)

        dew_dict = {
            'max_dew': max_dew_value,
            'max_date': max_dew_date,
            'mean_dew': mean_dew_value,
            'min_dew': min_dew_value,
            'min_date': min_dew_date
        }
        return dew_dict

    def get_humidity_data(self):
        """ returns the data of the humidity point of the csv file """
        max_humidity_value = max(
            record.max_humidity for record in self.record_list)
        max_humidity_date = max(
            record.date for record in self.record_list if record.max_humidity == max_humidity_value)
        mean_humidity_value = int(
            mean(list(record.mean_humidity for record in self.record_list)))
        min_humidity_value = min(
            record.min_humidity for record in self.record_list)
        min_humidity_date = min(
            record.date for record in self.record_list if record.min_humidity == min_humidity_value)

        humidity_dict = {
            'max_humidity': max_humidity_value,
            'max_date': max_humidity_date,
            'mean_humidity': mean_humidity_value,
            'min_humidity': min_humidity_value,
            'min_date': min_humidity_date
        }
        return humidity_dict

    def get_sea_pressure_data(self):
        """ returns the data of the sea_pressure point of the csv file """
        max_sea_pressure_value = max(
            record.max_sea_pressure for record in self.record_list)
        max_sea_pressure_date = max(
            record.date for record in self.record_list if record.max_sea_pressure == max_sea_pressure_value)
        mean_sea_pressure_value = int(
            mean(list(record.mean_sea_pressure for record in self.record_list)))
        min_sea_pressure_value = min(
            record.min_sea_pressure for record in self.record_list)
        min_sea_pressure_date = min(
            record.date for record in self.record_list if record.min_sea_pressure == min_sea_pressure_value)

        sea_pressure_dict = {
            'max_sea_pressure': max_sea_pressure_value,
            'max_date': max_sea_pressure_date,
            'mean_sea_pressure': mean_sea_pressure_value,
            'min_sea_pressure': min_sea_pressure_value,
            'min_date': min_sea_pressure_date
        }
        return sea_pressure_dict

    def get_visibility_data(self):
        """ returns the data of the visibility point of the csv file """
        max_visibility_value = max(
            record.max_visibility for record in self.record_list)
        max_visibility_date = max(
            record.date for record in self.record_list if record.max_visibility == max_visibility_value)
        mean_visibility_value = int(
            mean(list(record.mean_visibility for record in self.record_list)))
        min_visibility_value = min(
            record.min_visibility for record in self.record_list)
        min_visibility_date = min(
            record.date for record in self.record_list if record.min_visibility == min_visibility_value)

        visibility_dict = {
            'max_visibility': max_visibility_value,
            'max_date': max_visibility_date,
            'mean_visibility': mean_visibility_value,
            'min_visibility': min_visibility_value,
            'min_date': min_visibility_date
        }
        return visibility_dict

    def get_wind_speed_data(self):
        """ returns the data of the wind_speed of the csv file """
        max_wind_speed_value = max(
            record.max_wind_speed for record in self.record_list)
        max_wind_speed_date = max(
            record.date for record in self.record_list if record.max_wind_speed == max_wind_speed_value)
        mean_wind_speed_value = int(
            mean(list(record.mean_wind_speed for record in self.record_list)))
        max_gust_speed_value = max(
            record.max_gust_speed for record in self.record_list)
        max_gust_speed_date = max(
            record.date for record in self.record_list if record.max_gust_speed == max_gust_speed_value)

        wind_speed_dict = {
            'max_wind_speed': max_wind_speed_value,
            'max_date': max_wind_speed_date,
            'mean_wind_speed': mean_wind_speed_value,
            'max_gust_speed': max_gust_speed_value,
            'max_gust_date': max_gust_speed_date
        }
        return wind_speed_dict

    def write_to_file(self, file_name):
        """ writes the given record_list to the output file in csv format """
        with open(file_name, 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(['date', 'max_temp', 'mean_temp', 'min_temp',
                             'max_dew', 'mean_dew', 'min_dew',
                             'max_humidity', 'mean_humidity', 'min_humidity',
                             'max_sea_pressure', 'mean_sea_pressure', 'min_sea_pressure',
                             'max_visibility', 'mean_visibility', 'min_visibility',
                             'max_wind_speed', 'mean_wind_speed',
                             'max_gust_speed',
                             'precipitation',
                             'cloud_cover',
                             'events',
                             'wind_direction'])
            for row in self.record_list:
                row.events = '-'.join(row.events)
                writer.writerow(row)

    def write_to_file2(self, file_name):
        """ writes the given record_list to the output file in csv format """
        with open(file_name, 'w') as the_file:
            temp_dict = self.get_temp_data()
            the_file.write("Maximum temperature was {:d} on {}\n".format(
                temp_dict['max_temp'], temp_dict['max_date']))
            the_file.write("Mean temperature was {:d}\n".format(
                temp_dict['mean_temp']))
            the_file.write("Minimum temperature was {:d} on {}\n\n".format(
                temp_dict['min_temp'], temp_dict['min_date']))

            dew_dict = self.get_dew_data()
            the_file.write("Maximum dew was {:d} on {}\n".format(
                dew_dict['max_dew'], dew_dict['max_date']))
            the_file.write("Mean dew was {:d}\n".format(dew_dict['mean_dew']))
            the_file.write("Minimum dew was {:d} on {}\n\n".format(
                dew_dict['min_dew'], dew_dict['min_date']))

            humidity_dict = self.get_humidity_data()
            the_file.write("Maximum humidity was {:d} on {}\n".format(
                humidity_dict['max_humidity'], humidity_dict['max_date']))
            the_file.write("Mean humidity was {:d}\n".format(
                humidity_dict['mean_humidity']))
            the_file.write("Minimum humidity was {:d} on {}\n\n".format(
                humidity_dict['min_humidity'], humidity_dict['min_date']))

            sea_pressure_dict = self.get_sea_pressure_data()
            the_file.write("Maximum sea_pressure was {:d} on {}\n".format(
                sea_pressure_dict['max_sea_pressure'], sea_pressure_dict['max_date']))
            the_file.write("Mean sea pressure was {:d}\n".format(
                sea_pressure_dict['mean_sea_pressure']))
            the_file.write("Minimum sea_pressure was {:d} on {}\n\n".format(
                sea_pressure_dict['min_sea_pressure'], sea_pressure_dict['min_date']))

            visibility_dict = self.get_visibility_data()
            the_file.write("Maximum visibility was {:d} on {}\n".format(
                visibility_dict['max_visibility'], visibility_dict['max_date']))
            the_file.write("Mean visibility was {:d}\n".format(
                visibility_dict['mean_visibility']))
            the_file.write("Minimum visibility was {:d} on {}\n\n".format(
                visibility_dict['min_visibility'], visibility_dict['min_date']))

            wind_speed_dict = self.get_wind_speed_data()
            the_file.write("Maximum wind speed was {:d} on {}\n".format(
                wind_speed_dict['max_wind_speed'], wind_speed_dict['max_date']))
            the_file.write("Mean wind speed was {:d}\n".format(
                wind_speed_dict['mean_wind_speed']))
            the_file.write("Maximum gust speed was {:d} on {}\n\n".format(
                wind_speed_dict['max_gust_speed'], wind_speed_dict['max_gust_date']))
        the_file.close()


def main():
    """ main function """
    csv = CSV('madrid.csv')
    csv.write_to_file2('output.txt')


if __name__ == "__main__":
    main()