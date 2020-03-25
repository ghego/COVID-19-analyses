import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

dfita = pd.read_csv('../data/pcm-dpc_COVID-19/dati-regioni/dpc-covid19-ita-regioni.csv')
dfita['data'] = pd.to_datetime(dfita['data'])
dfitapvt = dfita.pivot(columns='denominazione_regione', index='data', values='totale_casi')
ts = dfitapvt.sum(axis=1).diff()

fig, ax = plt.subplots(figsize=(15,7))
ax.bar(ts.index, ts.values)
ax.xaxis.set_major_locator(mdates.WeekdayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
ax.set_title('Italy: New cases')
ax.set_ylabel('Count')
ax.set_xlabel('Date')
fig.savefig("../images/italy_new_cases.png")
