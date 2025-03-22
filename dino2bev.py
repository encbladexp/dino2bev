#!/usr/bin/env python3
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

# Fair defaults, choosen for an VW ID3 vs VW Golf VIII and a random gas station
# on a even more random date.
DEFAULT_DIESEL_PRICE = 1.649
DEFAULT_GASOLINE_PRICE = 1.759
DEFAULT_BEV_KWH_PER_100KM = 18.78
DEFAULT_DIESEL_L_PER_100KM = 5.51
DEFAULT_GASOLINE_L_PER_100KM = 7.39
DEFAULT_DIESEL_TAX = 228
DEFAULT_GASOLINE_TAX = 76
DEFAULT_BEV_TAX = 0
# what I got in 2024 from Carbonify
DEFAULT_THG_QUOTE = 90
# average in germany
DEFAULT_KM_PER_YEAR = 12545

argparser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
ice_args_parser = argparser.add_argument_group("Gasoline/Diesel €/l")
ice_args_parser.add_argument(
    "--diesel-price", type=float, default=DEFAULT_DIESEL_PRICE, help="Diesel €/l"
)
ice_args_parser.add_argument(
    "--gasoline-price", type=float, default=DEFAULT_GASOLINE_PRICE, help="Gasoline €/l"
)
consumption_args_parser = argparser.add_argument_group(
    "Consumption l/100km or kWh/100km"
)
consumption_args_parser.add_argument(
    "--diesel-per-100km",
    type=float,
    default=DEFAULT_DIESEL_L_PER_100KM,
    help="Diesel l/100km",
)
consumption_args_parser.add_argument(
    "--gasoline-per-100km",
    type=float,
    default=DEFAULT_GASOLINE_L_PER_100KM,
    help="Gasoline l/100km",
)
consumption_args_parser.add_argument(
    "--kwh-per-100km",
    type=float,
    default=DEFAULT_BEV_KWH_PER_100KM,
    help="Electricity kWh/100km",
)
tax_args_parser = argparser.add_argument_group("Taxes €/year")
tax_args_parser.add_argument(
    "--diesel-tax", type=float, default=DEFAULT_DIESEL_TAX, help="Diesel tax €/year"
)
tax_args_parser.add_argument(
    "--gasoline-tax",
    type=float,
    default=DEFAULT_GASOLINE_TAX,
    help="Gasoline tax €/year",
)
tax_args_parser.add_argument(
    "--bev-tax", type=float, default=DEFAULT_BEV_TAX, help="BEV tax €/year"
)
argparser.add_argument(
    "--thg-quote",
    type=float,
    default=DEFAULT_THG_QUOTE,
    help="THG quote / CO2 compensation €/year",
)
argparser.add_argument(
    "--distance", type=float, default=DEFAULT_KM_PER_YEAR, help="Distance km/year"
)


def calculate(
    price_per_liter: float,
    l_per_100km: float,
    distance_per_year: float,
    ice_tax_per_year: float,
    bev_tax_per_year: float,
    thg_per_year: float,
    kwh_per_100km: float,
) -> float:
    """
    This function does the math we need, it does it in a way that people could
    easily cross check, so we use comments and explain what we are doing!
    """
    # Distance per year is a total number, we need it per 100km
    distance_in_100km = distance_per_year / 100
    # Let's start what costs our Diesel or Gasoline per year
    ice_consumption_cost_per_year = price_per_liter * l_per_100km * distance_in_100km
    # Now we add the taxes
    ice_cost_per_year = ice_consumption_cost_per_year + ice_tax_per_year
    # Now we add the THG quote, while it is an advantage for an BEV, we could
    # simply add as disadvantage for an ICE. An alternate solution would be
    # to break the THG quote down to our yearly distance, but the result will
    # be the same.
    ice_cost_per_year_with_thg = ice_cost_per_year + thg_per_year
    # Now we need to worry about an (possible) tax of our BEV:
    bev_cost_per_year = ice_cost_per_year_with_thg + bev_tax_per_year
    bev_cost_per_100km = bev_cost_per_year / distance_in_100km
    bev_cost_per_kwh = bev_cost_per_100km / kwh_per_100km
    return bev_cost_per_kwh


def format_euro(number: float) -> str:
    return f"{number:.2f}€"


if __name__ == "__main__":
    args = argparser.parse_args()
    cost_per_kwh_diesel = calculate(
        price_per_liter=args.diesel_price,
        l_per_100km=args.diesel_per_100km,
        distance_per_year=args.distance,
        ice_tax_per_year=args.diesel_tax,
        bev_tax_per_year=args.bev_tax,
        thg_per_year=args.thg_quote,
        kwh_per_100km=args.kwh_per_100km,
    )
    print(
        (
            "The Diesel ICE compares to the BEV at a price of "
            f"{format_euro(cost_per_kwh_diesel)} per kWh"
        )
    )
    cost_per_kwh_gasoline = calculate(
        price_per_liter=args.gasoline_price,
        l_per_100km=args.gasoline_per_100km,
        distance_per_year=args.distance,
        ice_tax_per_year=args.gasoline_tax,
        bev_tax_per_year=args.bev_tax,
        thg_per_year=args.thg_quote,
        kwh_per_100km=args.kwh_per_100km,
    )
    print(
        (
            "The Gasoline ICE compares to the BEV at a price of "
            f"{format_euro(cost_per_kwh_gasoline)} per kWh"
        )
    )
