from bot.client import get_client
from bot.logging_config import setup_logger

logger = setup_logger()


def place_market_order(symbol, side, quantity):
    try:
        client = get_client()

        logger.info(
            f"MARKET ORDER | Symbol={symbol} Side={side} Qty={quantity}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"API RESPONSE: {response}")

        return response

    except Exception as e:
        logger.error(f"Market order failed: {e}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        client = get_client()

        logger.info(
            f"LIMIT ORDER | Symbol={symbol} Side={side} Qty={quantity} Price={price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"API RESPONSE: {response}")

        return response

    except Exception as e:
        logger.error(f"Limit order failed: {e}")
        raise