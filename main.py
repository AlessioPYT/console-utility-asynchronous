import asyncio
from rate_service import CurrencyRateService
from api_client import PrivatBankAPIClient
from utils import parse_arguments

async def main():
    try:
        days = parse_arguments()
    except ValueError as e:
        print(e)
        return
    
    api_client = PrivatBankAPIClient()
    rate_service = CurrencyRateService(api_client)
    
    try:
        rates = await rate_service.get_currency_rates(days)
        print(rates)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    asyncio.run(main())
