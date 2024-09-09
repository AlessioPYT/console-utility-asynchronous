import aiohttp
from datetime import datetime

class PrivatBankAPIClient:
    BASE_URL = "https://api.privatbank.ua/p24api/exchange_rates?json&date="

    async def get_exchange_rates(self, date: str):
        url = f"{self.BASE_URL}{date}"
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    response.raise_for_status()
                    return await response.json()
            except aiohttp.ClientError as e:
                print(f"Error fetching data: {e}")
                return None
