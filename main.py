""" Task 1 assigned my Hamza Gul.
Looking into git, basic Python, and csv data
manipulation using Python
"""
import csv
from collections import OrderedDict
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

        record_by_max_temp = sorted(  # sorts the record_list by max_temp descending
            self.record_list, key=lambda x: x.max_temp, reverse=True)

        record_by_min_temp = sorted(  # sorts the record_list by min_temp ascending
            self.record_list, key=lambda x: x.min_temp)

        max_10_temps = set([])
        min_10_temps = set([])
        for row in record_by_max_temp:
            max_10_temps.add(row.max_temp)
            if len(max_10_temps) == 10:
                break
        for row in record_by_min_temp:
            min_10_temps.add(row.min_temp)
            if len(min_10_temps) == 10:
                break

        max_10_temps = sorted(max_10_temps, reverse=True)
        min_10_temps = sorted(min_10_temps)

        max_temp_date_dict = OrderedDict()
        min_temp_date_dict = OrderedDict()

        for temp in max_10_temps:
            date_record = [
                record.date for record in self.record_list if record.max_temp == temp]
            date_count = len(date_record)
            if date_count == 1:
                max_temp_date_dict[temp] = date_record[0].strftime("%Y-%m-%d")
            else:
                max_temp_date_dict[temp] = date_count

        for temp in min_10_temps:
            date_record = [
                record.date for record in self.record_list if record.min_temp == temp]
            date_count = len(date_record)
            if date_count == 1:
                min_temp_date_dict[temp] = date_record[0].strftime("%Y-%m-%d")
            else:
                min_temp_date_dict[temp] = date_count

        temp_dict = {
            'max_temp': max_temp_value,
            'max_date': max_temp_date,
            'mean_temp': mean_temp_value,
            'min_temp': min_temp_value,
            'min_date': min_temp_date,
            'max_temp_date_dict': max_temp_date_dict,
            'min_temp_date_dict': min_temp_date_dict
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

        record_by_max_dew = sorted(  # sorts the record_list by max_dew descending
            self.record_list, key=lambda x: x.max_dew, reverse=True)

        record_by_min_dew = sorted(  # sorts the record_list by min_dew ascending
            self.record_list, key=lambda x: x.min_dew)

        max_10_dews = set([])
        min_10_dews = set([])
        for row in record_by_max_dew:
            max_10_dews.add(row.max_dew)
            if len(max_10_dews) == 10:
                break
        for row in record_by_min_dew:
            min_10_dews.add(row.min_dew)
            if len(min_10_dews) == 10:
                break

        max_10_dews = sorted(max_10_dews, reverse=True)
        min_10_dews = sorted(min_10_dews)

        max_dew_date_dict = OrderedDict()
        min_dew_date_dict = OrderedDict()

        for dew in max_10_dews:
            date_record = [
                record.date for record in self.record_list if record.max_dew == dew]
            date_count = len(date_record)
            if date_count == 1:
                max_dew_date_dict[dew] = date_record[0].strftime("%Y-%m-%d")
            else:
                max_dew_date_dict[dew] = date_count

        for dew in min_10_dews:
            date_record = [
                record.date for record in self.record_list if record.min_dew == dew]
            date_count = len(date_record)
            if date_count == 1:
                min_dew_date_dict[dew] = date_record[0].strftime("%Y-%m-%d")
            else:
                min_dew_date_dict[dew] = date_count

        dew_dict = {
            'max_dew': max_dew_value,
            'max_date': max_dew_date,
            'mean_dew': mean_dew_value,
            'min_dew': min_dew_value,
            'min_date': min_dew_date,
            'max_dew_date_dict': max_dew_date_dict,
            'min_dew_date_dict': min_dew_date_dict
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

        record_by_max_humidity = sorted(  # sorts the record_list by max_humidity descending
            self.record_list, key=lambda x: x.max_humidity, reverse=True)

        record_by_min_humidity = sorted(  # sorts the record_list by min_humidity ascending
            self.record_list, key=lambda x: x.min_humidity)

        max_10_humidities = set([])
        min_10_humidities = set([])
        for row in record_by_max_humidity:
            max_10_humidities.add(row.max_humidity)
            if len(max_10_humidities) == 10:
                break
        for row in record_by_min_humidity:
            min_10_humidities.add(row.min_humidity)
            if len(min_10_humidities) == 10:
                break

        max_10_humidities = sorted(max_10_humidities, reverse=True)
        min_10_humidities = sorted(min_10_humidities)

        max_humidity_date_dict = OrderedDict()
        min_humidity_date_dict = OrderedDict()

        for humidity in max_10_humidities:
            date_record = [
                record.date for record in self.record_list if record.max_humidity == humidity]
            date_count = len(date_record)
            if date_count == 1:
                max_humidity_date_dict[humidity] = date_record[0].strftime(
                    "%Y-%m-%d")
            else:
                max_humidity_date_dict[humidity] = date_count

        for humidity in min_10_humidities:
            date_record = [
                record.date for record in self.record_list if record.min_humidity == humidity]
            date_count = len(date_record)
            if date_count == 1:
                min_humidity_date_dict[humidity] = date_record[0].strftime(
                    "%Y-%m-%d")
            else:
                min_humidity_date_dict[humidity] = date_count

        humidity_dict = {
            'max_humidity': max_humidity_value,
            'max_date': max_humidity_date,
            'mean_humidity': mean_humidity_value,
            'min_humidity': min_humidity_value,
            'min_date': min_humidity_date,
            'max_humidity_date_dict': max_humidity_date_dict,
            'min_humidity_date_dict': min_humidity_date_dict
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

        record_by_max_sea_pressure = sorted(  # sorts the record_list by max_sea_pressure descending
            self.record_list, key=lambda x: x.max_sea_pressure, reverse=True)

        record_by_min_sea_pressure = sorted(  # sorts the record_list by min_sea_pressure ascending
            self.record_list, key=lambda x: x.min_sea_pressure)

        max_10_humidities = set([])
        min_10_humidities = set([])
        for row in record_by_max_sea_pressure:
            max_10_humidities.add(row.max_sea_pressure)
            if len(max_10_humidities) == 10:
                break
        for row in record_by_min_sea_pressure:
            min_10_humidities.add(row.min_sea_pressure)
            if len(min_10_humidities) == 10:
                break

        max_10_humidities = sorted(max_10_humidities, reverse=True)
        min_10_humidities = sorted(min_10_humidities)

        max_sea_pressure_date_dict = OrderedDict()
        min_sea_pressure_date_dict = OrderedDict()

        for sea_pressure in max_10_humidities:
            date_record = [
                record.date for record in self.record_list if record.max_sea_pressure == sea_pressure]
            date_count = len(date_record)
            if date_count == 1:
                max_sea_pressure_date_dict[sea_pressure] = date_record[0].strftime(
                    "%Y-%m-%d")
            else:
                max_sea_pressure_date_dict[sea_pressure] = date_count

        for sea_pressure in min_10_humidities:
            date_record = [
                record.date for record in self.record_list if record.min_sea_pressure == sea_pressure]
            date_count = len(date_record)
            if date_count == 1:
                min_sea_pressure_date_dict[sea_pressure] = date_record[0].strftime(
                    "%Y-%m-%d")
            else:
                min_sea_pressure_date_dict[sea_pressure] = date_count

        sea_pressure_dict = {
            'max_sea_pressure': max_sea_pressure_value,
            'max_date': max_sea_pressure_date,
            'mean_sea_pressure': mean_sea_pressure_value,
            'min_sea_pressure': min_sea_pressure_value,
            'min_date': min_sea_pressure_date,
            'max_sea_pressure_date_dict': max_sea_pressure_date_dict,
            'min_sea_pressure_date_dict': min_sea_pressure_date_dict
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

        record_by_max_visibility = sorted(  # sorts the record_list by max_visibility descending
            self.record_list, key=lambda x: x.max_visibility, reverse=True)

        record_by_min_visibility = sorted(  # sorts the record_list by min_visibility ascending
            self.record_list, key=lambda x: x.min_visibility)

        max_10_humidities = set([])
        min_10_humidities = set([])
        for row in record_by_max_visibility:
            max_10_humidities.add(row.max_visibility)
            if len(max_10_humidities) == 10:
                break
        for row in record_by_min_visibility:
            min_10_humidities.add(row.min_visibility)
            if len(min_10_humidities) == 10:
                break

        max_10_humidities = sorted(max_10_humidities, reverse=True)
        min_10_humidities = sorted(min_10_humidities)

        max_visibility_date_dict = OrderedDict()
        min_visibility_date_dict = OrderedDict()

        for visibility in max_10_humidities:
            date_record = [
                record.date for record in self.record_list if record.max_visibility == visibility]
            date_count = len(date_record)
            if date_count == 1:
                max_visibility_date_dict[visibility] = date_record[0].strftime(
                    "%Y-%m-%d")
            else:
                max_visibility_date_dict[visibility] = date_count

        for visibility in min_10_humidities:
            date_record = [
                record.date for record in self.record_list if record.min_visibility == visibility]
            date_count = len(date_record)
            if date_count == 1:
                min_visibility_date_dict[visibility] = date_record[0].strftime(
                    "%Y-%m-%d")
            else:
                min_visibility_date_dict[visibility] = date_count

        visibility_dict = {
            'max_visibility': max_visibility_value,
            'max_date': max_visibility_date,
            'mean_visibility': mean_visibility_value,
            'min_visibility': min_visibility_value,
            'min_date': min_visibility_date,
            'max_visibility_date_dict': max_visibility_date_dict,
            'min_visibility_date_dict': min_visibility_date_dict
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

    def write_summary_to_file(self, file_name):
        """ writes the summary of weather data to the output file """
        with open(file_name, 'w') as the_file:
            temp_dict = self.get_temp_data()
            the_file.write("Maximum temperature was {:d} on {}\n".format(
                temp_dict['max_temp'], temp_dict['max_date']))
            the_file.write("Mean temperature was {:d}\n".format(
                temp_dict['mean_temp']))
            the_file.write("Minimum temperature was {:d} on {}\n".format(
                temp_dict['min_temp'], temp_dict['min_date']))

            the_file.write("The 10 highest temperatures recorded were:\n")
            max_temp_date_dict = temp_dict['max_temp_date_dict']
            for temp in max_temp_date_dict:
                if str(max_temp_date_dict[temp]).isdigit():
                    the_file.write("{0}: on {1} days\n".format(
                        temp, max_temp_date_dict[temp]))
                else:
                    the_file.write("{0}: on {1}\n".format(
                        temp, max_temp_date_dict[temp]))

            the_file.write("The 10 lowest temperatures recorded were:\n")
            min_temp_date_dict = temp_dict['min_temp_date_dict']
            for temp in min_temp_date_dict:
                if str(min_temp_date_dict[temp]).isdigit():
                    the_file.write("{0}: on {1} days\n".format(
                        temp, min_temp_date_dict[temp]))
                else:
                    the_file.write("{0}: on {1}\n".format(
                        temp, min_temp_date_dict[temp]))
            the_file.write('\n')

            dew_dict = self.get_dew_data()
            the_file.write("Maximum dew was {:d} on {}\n".format(
                dew_dict['max_dew'], dew_dict['max_date']))
            the_file.write("Mean dew was {:d}\n".format(dew_dict['mean_dew']))
            the_file.write("Minimum dew was {:d} on {}\n".format(
                dew_dict['min_dew'], dew_dict['min_date']))

            the_file.write("The 10 highest dew points recorded were:\n")
            max_dew_date_dict = dew_dict['max_dew_date_dict']
            for dew in max_dew_date_dict:
                if str(max_dew_date_dict[dew]).isdigit():
                    the_file.write("{0}: on {1} days\n".format(
                        dew, max_dew_date_dict[dew]))
                else:
                    the_file.write("{0}: on {1}\n".format(
                        dew, max_dew_date_dict[dew]))

            the_file.write("The 10 lowest dew points recorded were:\n")
            min_dew_date_dict = dew_dict['min_dew_date_dict']
            for dew in min_dew_date_dict:
                if str(min_dew_date_dict[dew]).isdigit():
                    the_file.write("{0}: on {1} days\n".format(
                        dew, min_dew_date_dict[dew]))
                else:
                    the_file.write("{0}: on {1}\n".format(
                        dew, min_dew_date_dict[dew]))
            the_file.write('\n')

            humidity_dict = self.get_humidity_data()
            the_file.write("Maximum humidity was {:d} on {}\n".format(
                humidity_dict['max_humidity'], humidity_dict['max_date']))
            the_file.write("Mean humidity was {:d}\n".format(
                humidity_dict['mean_humidity']))
            the_file.write("Minimum humidity was {:d} on {}\n".format(
                humidity_dict['min_humidity'], humidity_dict['min_date']))
            the_file.write("The 10 highest humidity points recorded were:\n")
            max_humidity_date_dict = humidity_dict['max_humidity_date_dict']
            for humidity in max_humidity_date_dict:
                if str(max_humidity_date_dict[humidity]).isdigit():
                    the_file.write("{0}: on {1} days\n".format(
                        humidity, max_humidity_date_dict[humidity]))
                else:
                    the_file.write("{0}: on {1}\n".format(
                        humidity, max_humidity_date_dict[humidity]))

            the_file.write("The 10 lowest humidity points recorded were:\n")
            min_humidity_date_dict = humidity_dict['min_humidity_date_dict']
            for humidity in min_humidity_date_dict:
                if str(min_humidity_date_dict[humidity]).isdigit():
                    the_file.write("{0}: on {1} days\n".format(
                        humidity, min_humidity_date_dict[humidity]))
                else:
                    the_file.write("{0}: on {1}\n".format(
                        humidity, min_humidity_date_dict[humidity]))
            the_file.write('\n')

            sea_pressure_dict = self.get_sea_pressure_data()
            the_file.write("Maximum sea_pressure was {:d} on {}\n".format(
                sea_pressure_dict['max_sea_pressure'], sea_pressure_dict['max_date']))
            the_file.write("Mean sea pressure was {:d}\n".format(
                sea_pressure_dict['mean_sea_pressure']))
            the_file.write("Minimum sea_pressure was {:d} on {}\n".format(
                sea_pressure_dict['min_sea_pressure'], sea_pressure_dict['min_date']))
            the_file.write("The 10 highest sea pressure readings recorded were:\n")
            max_sea_pressure_date_dict = sea_pressure_dict['max_sea_pressure_date_dict']
            for sea_pressure in max_sea_pressure_date_dict:
                if str(max_sea_pressure_date_dict[sea_pressure]).isdigit():
                    the_file.write("{0}: on {1} days\n".format(
                        sea_pressure, max_sea_pressure_date_dict[sea_pressure]))
                else:
                    the_file.write("{0}: on {1}\n".format(
                        sea_pressure, max_sea_pressure_date_dict[sea_pressure]))

            the_file.write("The 10 lowest sea pressure readings recorded were:\n")
            min_sea_pressure_date_dict = sea_pressure_dict['min_sea_pressure_date_dict']
            for sea_pressure in min_sea_pressure_date_dict:
                if str(min_sea_pressure_date_dict[sea_pressure]).isdigit():
                    the_file.write("{0}: on {1} days\n".format(
                        sea_pressure, min_sea_pressure_date_dict[sea_pressure]))
                else:
                    the_file.write("{0}: on {1}\n".format(
                        sea_pressure, min_sea_pressure_date_dict[sea_pressure]))
            the_file.write('\n')

            visibility_dict = self.get_visibility_data()
            the_file.write("Maximum visibility was {:d} on {}\n".format(
                visibility_dict['max_visibility'], visibility_dict['max_date']))
            the_file.write("Mean visibility was {:d}\n".format(
                visibility_dict['mean_visibility']))
            the_file.write("Minimum visibility was {:d} on {}\n".format(
                visibility_dict['min_visibility'], visibility_dict['min_date']))
            the_file.write("The 10 highest visibility readings recorded were:\n")
            max_visibility_date_dict = visibility_dict['max_visibility_date_dict']
            for visibility in max_visibility_date_dict:
                if str(max_visibility_date_dict[visibility]).isdigit():
                    the_file.write("{0}: on {1} days\n".format(
                        visibility, max_visibility_date_dict[visibility]))
                else:
                    the_file.write("{0}: on {1}\n".format(
                        visibility, max_visibility_date_dict[visibility]))
            the_file.write("The 10 lowest visibility readings recorded were:\n")
            min_visibility_date_dict = visibility_dict['min_visibility_date_dict']
            for visibility in min_visibility_date_dict:
                if str(min_visibility_date_dict[visibility]).isdigit():
                    the_file.write("{0}: on {1} days\n".format(
                        visibility, min_visibility_date_dict[visibility]))
                else:
                    the_file.write("{0}: on {1}\n".format(
                        visibility, min_visibility_date_dict[visibility]))
            the_file.write('\n')

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
    csv_reader = CSV('madrid.csv')
    csv_reader.get_temp_data()
    csv_reader.write_summary_to_file('output.txt')


if __name__ == "__main__":
    main()
