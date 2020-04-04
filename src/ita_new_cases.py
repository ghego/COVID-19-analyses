import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

dfita = pd.read_csv('../data/pcm-dpc_COVID-19/dati-regioni/dpc-covid19-ita-regioni.csv')
dfita['data'] = pd.to_datetime(dfita['data'])

pvt = dfita.drop(['stato', 'codice_regione', 
                  'lat', 'long', 
                  'note_it', 'note_en'], axis=1).groupby(['data']).sum()

tss = pvt.diff(axis=0)

cols = ['totale_casi', 'dimessi_guariti', 'deceduti']

fig, ax = plt.subplots(figsize=(10,6))
for c in cols:
    ax.bar(tss.index, tss[c])
ax.xaxis.set_major_locator(mdates.WeekdayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
ax.set_title('Italy')
ax.set_ylabel('Count')
ax.set_xlabel('Date')
ax.legend(cols)
fig.savefig("../images/italy_new_cases.png")