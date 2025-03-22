# What is dino2bev?

I often tend to have discussions about my BEV, and I often did some math about
what would be a comparable kWh price for a given car and its consumption.

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
compare an VW ID3 with an VW Golf VIII.

# Project Information

* We are using metric units
* We are using Euro as currency
