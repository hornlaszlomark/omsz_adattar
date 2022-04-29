# OMSZ Adattár - https://odp.met.hu/

🇬🇧 Download weather and climate data from the public ftp of the Hungarian Meteorological Service (source: Hungarian Meteorological Service)
🇭🇺 Időjárás és éghajlati adatok letöltés az Országos Meteorológiai Szolgálat nyilvános ftp szerverőről (Forrás: Országos Meteorológiai Szolgálat)

```python
from omsz_adattar import Weather

# initialize 'Weather' class
weather = Weather()

# download all available data
weather.download(freq='hourly')

```


#TODO:
- [ ] ☁️ Weather class
- [ ] 🛰️ Satellite class
- [ ] add numpy docstrings

weather<br>
- weather_reports <br>
  - synoptic<br>
      - hungary<br>
        - 10_minutes<br>
          - csv<br>
        - avg_daily<br>
          - csv<br>
        - daily<br>
          - csv<br>
        - daily_rain<br>
          - csv<br>
        - gas_daily<br>
          - csv<br>
        - hourly<br>
          - csv<br>
        - meta<br>
        - monthly<br>
          - csv<br>
