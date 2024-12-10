
# Weather Script

This Python script fetches weather information for a list of places using the wttr.in service.


## Features
- Fetches weather information for multiple locations.
- Outputs weather data in plain text format.
- Handles errors gracefully when the request fails.

## Requirements
- Python 3.8 or later.
- `requests` library (install via `pip install requests`).

## Setup
1. Clone the repository or download the script.
2. Install the required library:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Update the `places` list in the `weather.py` script with the locations you want to query.
2. Run the script:
   ```bash
   python weather.py
   ```

## Parameters
The script uses the wttr.in service. You can customize the weather information by modifying the `params` dictionary in the script. For more details on available options, visit:
[wttr.in Help Page](https://wttr.in/:help)

## Example Output
```
Череповец

     \  /       Переменная облачность
   _ /"".-.     -2(-8) °C
     \_(   ).   ↗ 4 м/c
     /(___(__)  10 км
                0.0 мм
                        ┌─────────────┐
┌───────────────────────┤ Вт. 10 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│      .-.      Слабый переохл…│
│  _ /"".-.     -2(-8) °C      │     (   ).    -1(-7) °C      │
│    \_(   ).   ↗ 5-7 м/c      │    (___(__)   ↗ 5-7 м/c      │
│    /(___(__)  10 км          │     ‘ * ‘ *   10 км          │
│               0.0 мм | 0%    │    * ‘ * ‘    0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Ср. 11 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Умеренный снег │      .-.      Слабый переохл…│
│     (   ).    +1(-5) °C      │     (   ).    -1(-7) °C      │
│    (___(__)   → 6-10 м/c     │    (___(__)   → 7-10 м/c     │
│    * * * *    5 км           │     ‘ * ‘ *   10 км          │
│   * * * *     0.2 мм | 100%  │    * ‘ * ‘    0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Чт. 12 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Облачно        │               Пасмурно       │
│      .--.     -5(-11) °C     │      .--.     -6(-11) °C     │
│   .-(    ).   ↘ 5-7 м/c      │   .-(    ).   ↘ 3-6 м/c      │
│  (___.__)__)  10 км          │  (___.__)__)  10 км          │
│               0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
```

## Notes
- Make sure to have an active internet connection.
- The locations are URL-encoded to support non-ASCII characters.

## License
This project is licensed under the MIT License.
