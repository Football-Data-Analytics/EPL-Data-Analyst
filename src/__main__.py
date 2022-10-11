import ScraperFC as sfc

scraper = sfc.FBRef()

data = scraper.get_season_link(2023, 'EPL')
scraper.close()

print(data)