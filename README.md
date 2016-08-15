# AvitoParser
For parsing ads on avito.ru

## Example


    from avitoparser import AvitoParser

    base_url = "https://www.avito.ru/rossiya/velosipedy/dorozhnye"
    search_word = "bianchi"

    parser = AvitoParser(base_url, search_word, filter='price')
    ads = parser.dump_ads()
    print(ads[0])

`>> {'link': 'https://www.avito.ru/krasnodar/velosipedy/bianchi_italiya_163291575', 'image': 'https://40.img.avito.st/140x105/343374340.jpg', 'price': '60000', 'description': 'Bianchi (италия)'}`
