# Binance Futures Testnet Trading Bot

A modular Python CLI application for placing cryptocurrency futures orders on the Binance Futures Testnet (USDT-M).

Built as part of a Python Developer internship assignment focused on:
- API integration
- CLI development
- validation
- logging
- error handling
- clean software structure

---

# Features

## Core Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Binance Futures Testnet integration
- Command-line interface using Typer
- Input validation
- Structured logging
- Exception handling
- Clean modular architecture

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.x | Core language |
| python-binance | Binance API SDK |
| Typer | CLI framework |
| python-dotenv | Environment variable management |
| logging | Logging system |

---

# Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── exceptions.py
│
├── logs/
│   └── trading_bot.log
│
├── .env
├── .gitignore
├── cli.py
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/your-username/trading-bot.git
cd trading-bot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Binance Futures Testnet Setup

## Create Testnet Account

Use Binance Futures Testnet:

https://testnet.binancefuture.com

---

## Generate API Credentials

1. Login to Binance Futures Testnet
2. Open API Management
3. Generate:
   - API Key
   - Secret Key

---

## Create .env File

Create a `.env` file in the root directory:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

---

# Running the Application

---

# MARKET Order Example

## BUY MARKET Order

```bash
python cli.py BTCUSDT BUY MARKET 0.001
```

---

## SELL MARKET Order

```bash
python cli.py BTCUSDT SELL MARKET 0.001
```

---

# LIMIT Order Example

## BUY LIMIT Order

```bash
python cli.py BTCUSDT BUY LIMIT 0.001 --price 100000
```

---

## SELL LIMIT Order

```bash
python cli.py BTCUSDT SELL LIMIT 0.001 --price 120000
```

---

# Example Output

```text
===== ORDER REQUEST =====

Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.001

===== ORDER RESPONSE =====

Order ID     : 123456789
Status       : FILLED
Executed Qty : 0.001
Avg Price    : 105432.10

✅ Order placed successfully
```

---

# Logging

All API requests, responses, and errors are logged to:

```text
logs/trading_bot.log
```

Example log:

```text
2026-05-20 23:10:01 | INFO | MARKET ORDER | Symbol=BTCUSDT Side=BUY Qty=0.001
2026-05-20 23:10:02 | INFO | API RESPONSE: {...}
```

---

# Validation & Error Handling

The application validates:

- order side
- order type
- quantity
- price for LIMIT orders

Handled errors include:

- invalid user input
- API failures
- network issues
- Binance exceptions

---

# Architecture Overview

## client.py
Handles Binance client creation and configuration.

## orders.py
Contains reusable order placement functions.

## validators.py
Handles CLI input validation.

## logging_config.py
Configures structured logging.

## cli.py
CLI entry point using Typer.

---

# Security Notes

- API credentials are stored using environment variables
- `.env` file is excluded using `.gitignore`
- No secrets are hardcoded

---

# Assumptions

- Binance Futures Testnet is available
- User has valid API credentials
- User has sufficient testnet balance

---

# Sample Log Files Included

This repository includes:
- MARKET order log
- LIMIT order log

inside the `logs/` directory.

---

# Future Improvements

Possible future enhancements:
- Stop-Limit orders
- OCO orders
- Docker support
- Web dashboard
- Real-time market monitoring
- Order history
- Position management

---

# Author

Srujan Naik

---

# License

This project is created for educational and internship evaluation purposes.