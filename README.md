# What is dino2bev?

I often tend to have discussions about my BEV, and I often did some math about
what would be a comparable kWh price for a given car and its consumption.

# Features

* Knows about what we tend to call THG Quote in Germany
* Knows about Diesel and Gasoline, as well as different Taxes
* Does not need any fancy libraries or packages except pure Python

# Usage

Let's just assume you only want to change our distance a little bit:
```bash
./dino2bev.py --distance 8000
```

Which would generate this output:
```
The Diesel ICE compares to the BEV at a price of 0.70€ per kWh
The Gasoline ICE compares to the BEV at a price of 0.80€ per kWh
You are going to save money if you are able to get electricy cheaper ;)
```

Just checkout `./dino2bev.py --help`, it has plenty of options. By default we
compare an VW ID3 with an VW Golf VIII. Below an maybe outdated overview of
what is possible:
```
usage: dino2bev.py [-h] [--diesel-price DIESEL_PRICE] [--gasoline-price GASOLINE_PRICE]
                   [--diesel-per-100km DIESEL_PER_100KM] [--gasoline-per-100km GASOLINE_PER_100KM]
                   [--kwh-per-100km KWH_PER_100KM] [--diesel-tax DIESEL_TAX] [--gasoline-tax GASOLINE_TAX]
                   [--bev-tax BEV_TAX] [--thg-quote THG_QUOTE] [--distance DISTANCE]

options:
  -h, --help            show this help message and exit
  --thg-quote THG_QUOTE
                        THG quote / CO2 compensation €/year (default: 90)
  --distance DISTANCE   Distance km/year (default: 12545)

Gasoline/Diesel €/l:
  --diesel-price DIESEL_PRICE
                        Diesel €/l (default: 1.649)
  --gasoline-price GASOLINE_PRICE
                        Gasoline €/l (default: 1.759)

Consumption l/100km or kWh/100km:
  --diesel-per-100km DIESEL_PER_100KM
                        Diesel l/100km (default: 5.51)
  --gasoline-per-100km GASOLINE_PER_100KM
                        Gasoline l/100km (default: 7.39)
  --kwh-per-100km KWH_PER_100KM
                        Electricity kWh/100km (default: 18.78)

Taxes €/year:
  --diesel-tax DIESEL_TAX
                        Diesel tax €/year (default: 228)
  --gasoline-tax GASOLINE_TAX
                        Gasoline tax €/year (default: 76)
  --bev-tax BEV_TAX     BEV tax €/year (default: 0)
```

# Requirements

Python >= 3.12, most likely even older versions, will work well.

# Project Information

* We are using metric units
* We are using Euro as currency
