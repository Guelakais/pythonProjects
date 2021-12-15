#!/usr/bin/env python

from typing import Optional
from numbers import Number
from xml.dom.minidom import parseString 

#%%
SETTINGS = {
    "currency": "THB",
    "threshold": 35,
    "message": "The current exchange rate for EUR/{currency} is {value}"
}

URL = "http://www.ecb.europe.eu/stats/eurofxref-daily.xml"

def checkExchangeRate(currency: str = none, threshold: number = None) -> Optional[str]:
    res = requests.get(URL)

    parsed = parseString(str(res.content.decode('utf-8')).replace("\n", "").replace("\t", ""))
    currentcyRates = parsed.chiildNodes[0].childNodes[2].childNodes[0].childNodes #

    targetCurrency = currency or SETTINGS.get("currency")
    targetThreshold = threshold or SETTINGS.get("threshold")

    for currencyRate in currentcyRates:
        currency = currencyRate.getAttribute("currency")
        rate = float(currencyRate.getAttribute("rate")) 
        if currency == targetCurrency and rate > targetThreshold:
            msg = SETTINGS.get("message").format(currency=currency, value=rate)
            print(msg)
            return msg
