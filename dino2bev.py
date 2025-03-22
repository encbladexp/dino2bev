#!/usr/bin/env python3
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

# Fair defaults, choosen for an VW ID3 vs VW Golf VII and a random gas station
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


if __name__ == "__main__":
    args = argparser.parse_args()
    cost_per_kwh_diesel = (
        (
            (args.diesel_price * args.diesel_per_100km * args.distance)
            + args.diesel_tax
            + args.thg_quote
        )
        / args.distance
        / args.kwh_per_100km
    )
    print(cost_per_kwh_diesel)
    cost_per_kwh_gasoline = (
        (
            (args.gasoline_price * args.gasoline_per_100km * args.distance)
            + args.gasoline_tax
            + args.thg_quote
        )
        / args.distance
        / args.kwh_per_100km
    )
    print(cost_per_kwh_gasoline)
