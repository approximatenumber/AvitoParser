# AvitoParser
For parsing ads on avito.ru

## Examples

Print the ad with the highest price:

```python
from avitoparser import AvitoParser

base_url = "https://www.avito.ru/rossiya/velosipedy/dorozhnye"
search_word = "bianchi"

parser = AvitoParser(base_url, search_word, filter='price')
ads = parser.dump_ads()
print(ads[0])
```

You`ll get:

```python
{'link': 'https://www.avito.ru/moskva/velosipedy/karbonovyy_shosseynyy_velosiped_bianchi_oltre_xr2_787297601',
  'price': '247500',
  'description': 'Карбоновый шоссейный велосипед Bianchi Oltre XR2',
  'image': 'https://33.img.avito.st/140x105/2692545733.jpg'
}
```
