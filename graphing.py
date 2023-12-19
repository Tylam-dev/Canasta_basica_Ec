import matplotlib.pyplot as plt
from getYearCanasta import canastaPerYear

years, canasta = canastaPerYear()

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

generate_bar_chart(years, canasta)