import typer

from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

app = typer.Typer()


@app.command()
def trade(
    symbol: str = typer.Argument(...),
    side: str = typer.Argument(...),
    order_type: str = typer.Argument(...),
    quantity: float = typer.Argument(...),
    price: float = typer.Option(None, "--price")
):
    """
    Place Binance Futures Testnet order
    """

    try:
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)

        if order_type == "LIMIT":
            price = validate_price(price)

        print("\n===== ORDER REQUEST =====")
        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {quantity}")

        if price:
            print(f"Price       : {price}")

        if order_type == "MARKET":
            response = place_market_order(
                symbol,
                side,
                quantity
            )

        else:
            response = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print("\n===== ORDER RESPONSE =====")

        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice')}")

        print("\n✅ Order placed successfully")

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    app()