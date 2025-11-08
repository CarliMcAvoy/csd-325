import csv
from datetime import datetime

from matplotlib import pyplot as plt


print('Hello! If you would like to see the daily HIGH temperatures for 2018, enter "High". If you would like to\n'
      'see the daily LOW temperatures for 2018, enter "Low". If you would like to quit the program, enter "Exit".')


def main():

    try:
        action = str(input('> '))

        if action == 'High':
            High()

        if action == 'Low':
            Low()

        if action == 'Exit':
            print('Thanks for using matplotlib! Goodbye.')

    except ValueError:
        print('ERROR: Enter a valid input.')
        return main()

def High():

    print('Here is a plot of the high temperatures for 2018.')

    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

    # Get dates and high temperatures from this file.
        dates, highs = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)

# Plot the high temperatures.
#plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

# Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
    return main()

def Low():

    print('Here is a plot of the low temperatures for 2018.')

    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and high temperatures from this file.
        dates, lows = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            low = int(row[6])
            lows.append(low)

        # Plot the high temperatures.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        # Format plot.
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
    return main()

main()
