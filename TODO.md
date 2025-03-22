```
>>> id3_verbrauch = 18.78
>>> golf_verbrauch_benzin = 7.39
>>> golf_verbrauch_diesel = 5.51
>>> benzin_pro_l = 1.759
>>> diesel_pro_l = 1.649
>>> golf_verbrauch_benzin * benzin_pro_l / id3_verbrauch
0.6921730564430244
>>> golf_verbrauch_diesel * diesel_pro_l / id3_verbrauch
0.48381203407880713
>>> golf_steuer_diesel = 228
>>> golf_steuer_benzin = 76
>>> fahrleistung_pro_jahr = 18_000 / 100 # um auf 100km umzurechnen
>>> ((golf_verbrauch_benzin * benzin_pro_l * fahrleistung_pro_jahr) + golf_steuer_benzin) / fahrleistung_pro_jahr / id3_verbrauch
0.7146556028872322
>>> ((golf_verbrauch_diesel * diesel_pro_l * fahrleistung_pro_jahr) + golf_steuer_diesel) / fahrleistung_pro_jahr / id3_verbrauch
0.5512596734114305
>>> thg_quote_2024 = 90
>>> ((golf_verbrauch_benzin * benzin_pro_l * fahrleistung_pro_jahr) + golf_steuer_benzin + thg_quote_2024) / fahrleistung_pro_jahr / id3_verbrauch
0.7412796710448466
>>> ((golf_verbrauch_diesel * diesel_pro_l * fahrleistung_pro_jahr) + golf_steuer_diesel + thg_quote_2024) / fahrleistung_pro_jahr / id3_verbrauch
0.577883741569045
>>> fahrleistung_pro_jahr = 12_000 / 100
>>> ((golf_verbrauch_benzin * benzin_pro_l * fahrleistung_pro_jahr) + golf_steuer_benzin + thg_quote_2024) / fahrleistung_pro_jahr / id3_verbrauch
0.7658329783457577
>>> ((golf_verbrauch_diesel * diesel_pro_l * fahrleistung_pro_jahr) + golf_steuer_diesel + thg_quote_2024) / fahrleistung_pro_jahr / id3_verbrauch
0.6249195953141639
>>> fahrleistung_pro_jahr = 8_000 / 100
>>> ((golf_verbrauch_benzin * benzin_pro_l * fahrleistung_pro_jahr) + golf_steuer_benzin + thg_quote_2024) / fahrleistung_pro_jahr / id3_verbrauch
0.8026629392971244
>>> ((golf_verbrauch_diesel * diesel_pro_l * fahrleistung_pro_jahr) + golf_steuer_diesel + thg_quote_2024) / fahrleistung_pro_jahr / id3_verbrauch
0.6954733759318422
```