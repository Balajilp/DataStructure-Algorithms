shares = { "DIVI'S_LAB":{"DATE_OF_BUY":"01-11-2022", "Quantity":9, "BUY_PRICE":3698, "BUY_BROKERAGE":0, "STT_CHARGE":33, "OTHER_CHARGE":6.35, 
           "TOTAL_PRICE":33282, "TOTAL_BUY_PRICE_INCLUDING_TAX": 33321.35},

           "MANAPPURAM":{"DATE_OF_BUY":"16-12-2022", "Quantity":20, "BUY_PRICE":117.05, "BUY_BROKERAGE":0, "STT_CHARGE":2.34, "OTHER_CHARGE":0.45, 
           "TOTAL_PRICE":2341, "TOTAL_BUY_PRICE_INCLUDING_TAX": 2343.79}, 

           "MUTHOOT_FINANCE":{"DATE_OF_BUY":"16-12-2022", "Quantity":2, "BUY_PRICE":1082.60, "BUY_BROKERAGE":0, "STT_CHARGE":2.41, "OTHER_CHARGE":0.41, 
           "TOTAL_PRICE":2165.2, "TOTAL_BUY_PRICE_INCLUDING_TAX": 2168.02},

           "KALYAN_JEWELLERS":{"DATE_OF_BUY":"16-12-2022", "Quantity":15, "BUY_PRICE":125.40, "BUY_BROKERAGE":0, "STT_CHARGE":1.88, "OTHER_CHARGE":0.36, 
           "TOTAL_PRICE":1881, "TOTAL_BUY_PRICE_INCLUDING_TAX": 1883.24},

           "TMB":{"DATE_OF_BUY":"16-12-2022", "Quantity":9, "BUY_PRICE":511.55, "BUY_BROKERAGE":0, "STT_CHARGE":4.60, "OTHER_CHARGE": 0.88, 
           "TOTAL_PRICE":4603.95, "TOTAL_BUY_PRICE_INCLUDING_TAX": 4609.43},

           "WIPRO":{"DATE_OF_BUY":"16-12-2022", "Quantity":12, "BUY_PRICE":391.35, "BUY_BROKERAGE":0, "STT_CHARGE":4.70, "OTHER_CHARGE":0.94, 
           "TOTAL_PRICE":4696.2, "TOTAL_BUY_PRICE_INCLUDING_TAX": 4701.84},

           "TECH_MAHINDRA":{"DATE_OF_BUY":"16-12-2022", "Quantity":4, "BUY_PRICE":1015.85, "BUY_BROKERAGE":0, "STT_CHARGE":4.06, "OTHER_CHARGE":0.78, 
           "TOTAL_PRICE":4063.4, "TOTAL_BUY_PRICE_INCLUDING_TAX": 4068.24}
           }

import pandas as pd 
shares_data = pd.DataFrame(shares).T 
print(shares_data)

