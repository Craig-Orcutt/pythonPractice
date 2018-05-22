stocks = {
  "AAPL" : "Apple",
  "ADTN" : "Adtran",
  "NKE" : "Nike",
  "SBUX" : "Starbucks",
  "AABA" : "Altaba"
}

purchases = [
  ('AAPL', 95, '4-april-2001', 25),
  ('SBUX', 143, '3-march-2003', 44),
  ('AAPL', 245, '9-september-2004', 456),
  ('NKE', 132, '4-july-2004', 321),
  ('ADTN', 77, '13-july-2000', 23),
  ('AABA', 99, '21-august-2013',65)
]


def printPurchases(purchase, stock):
  for comps in purchase:
    for key,name in stock.items():
      if comps[0] == key:
        stock_price = comps[1]*comps[3]
        print(name + " sold " + '${}'.format(stock_price) + " worth of shares on " + "{}".format(comps[2]) )

printPurchases(purchases, stocks)

