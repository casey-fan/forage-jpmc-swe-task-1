import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for i in quotes:
        self.assertEqual(getDataPoint(i), (i['stock'], i['top_bid']['price'], i['top_ask']['price'], (i['top_bid']['price']+i['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for i in quotes:
        self.assertEqual(getDataPoint(i), (i['stock'], i['top_bid']['price'], i['top_ask']['price'], (i['top_bid']['price']+i['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_priceA_zero(self):
     quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'} ]
     prices={}
     for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        if (stock =="DEF"):
          prices['DEF'] = price
        else:
          prices["ABC"] =0
     for i in quotes:
        self.assertEqual(getRatio(prices['ABC'], prices['DEF']),(prices['ABC']/ prices['DEF']))
  
  def test_getRatio_priceB_zero(self):
     quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'} ]
    #  prices={}
    #  for quote in quotes:
    #     stock, bid_price, ask_price, price = getDataPoint(quote)
    #     if (stock =="DEF"):
    #       prices['ABC'] = price
    #     else:
    #       prices["DEF"] =0
    #  ratio = getRatio(prices['ABC'], prices['DEF'])
    #  print(ratio)

     try:
      getRatio(120, 0)
      self.fail("Expected ZeroDivisionError")
     except ZeroDivisionError as e:
      self.assertEqual(str(e), "The price_b cannot be zero.")
 
    #  self.assertEqual(ratio, ZeroDivisionError)

        

if __name__ == '__main__':
    unittest.main()
