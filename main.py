from typing import Union
from fastapi import FastAPI
from scraper import Scraper
 
app = FastAPI()
quotes = Scraper()
 
@app.get("/{cat}")
async def read_item(cat):
    # Scrape data for {cat} parameter
    return quotes.scrapedata(cat)