import pandas as pd
import matplotlib.pyplot as plt


csv_dateipfad = 'data.csv'

daten = pd.read_csv(csv_dateipfad)
aufzugsstart_zeit = 11
aufzugsende_zeit = 28

# Zeit und Beschleunigung in Z-Richtung extrahieren
zeit = daten['Time (s)']
beschleunigung_z = daten['Acceleration z (m/s^2)']

# Diagramm erstellen
plt.plot(zeit, beschleunigung_z, label='Beschleunigung in Z-Richtung')
plt.title('Aufzugfahrt von 2 nach KG')
plt.xlabel('Zeit in s)')
plt.ylabel('Beschleunigung in Z-Richtung in m/s^2')
plt.axvline(x=aufzugsstart_zeit, color='g', linestyle='--', label='Fahrt Start')
plt.axvline(x=aufzugsende_zeit, color='r', linestyle='--', label='Fahrt Ende')
plt.legend()
plt.grid(True)
plt.show()
