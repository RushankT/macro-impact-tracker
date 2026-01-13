"""
Configuration file for Macro Impact Tracker
Defines supported countries, macro events, and market instruments
"""

COUNTRIES = {
    "US": {
        "country_name": "united states",
        "currency": "USD",
        "macro_events": [
            "CPI",
            "Non Farm Payrolls"
        ],
        "assets": {
            "equities": "SPY",        # S&P 500 ETF
            "rates": "^TNX",          # US 10Y Treasury Yield
            "fx": "DXY",              # Dollar Index
            "volatility": "^VIX"      # VIX
        },
        "market_timezone": "US/Eastern"
    },

    "INDIA": {
        "country_name": "india",
        "currency": "INR",
        "macro_events": [
            "CPI",
            "Repo Rate"
        ],
        "assets": {
            "equities": "^NSEI",      # NIFTY 50
            "rates": "IN10YR",        # India 10Y G-Sec (may change later)
            "fx": "USDINR=X",         # USD/INR
            "volatility": "^INDIAVIX" # India VIX
        },
        "market_timezone": "Asia/Kolkata"
    }
}
