from api_client import PrivatBankAPIClient
from datetime import datetime, timedelta

class CurrencyRateService:
    def __init__(self, api_client: PrivatBankAPIClient):
        self.api_client = api_client

    async def get_currency_rates(self, days: int):
        if days > 10:
            raise ValueError("You can only fetch data for up to 10 days.")
        
        results = []
        for i in range(days):
            date = (datetime.now() - timedelta(days=i)).strftime("%d.%m.%Y")
            data = await self.api_client.get_exchange_rates(date)
            if data:
                rates = self.extract_rates(data)
                results.append({date: rates})
        return results

    def extract_rates(self, data):
        rates = {}
        for rate in data.get('exchangeRate', []):
            if rate['currency'] in ['USD', 'EUR']:
                rates[rate['currency']] = {
                    'sale': rate['saleRate'],
                    'purchase': rate['purchaseRate']
                }
        return rates
