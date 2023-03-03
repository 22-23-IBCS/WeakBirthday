class CurrencyConverter:

     def __init__(self):
         self.countries = {"China" : 7,
                           "Canada" : 0.75,
                           "Russia" : 0.014,
                           "India" : 0.012,
                           "Brazil" : 0.19,
                           "South Korea" : 0.00079,
                           "France" : 1.07}

     def ConvertFromUS(self, x, country):
           x = x * self.countries[country]
           return x

     def GeneralConvert(self, x, country, country2):
          x = x * (self.countries[country] + 1)
          x = x * self.countries[country2]
          return x
          


def main():
     C = CurrencyConverter()
     L = ["China", "Canada", "Russia", "India", "Brazil", "South Korea", "France"]
     print(L)
     x = int(input("What is the amount you want to convert?\n"))
     y = input("Are you converting from US dollars?\n1. Yes\n2. No\n")
     b = input("What currency are you converting to?\n")
     if y == 2:
          a = input("What currency are you converting from?\n")
          print(C.GeneralConvert(x, a, b))
     else:
          print(C.ConvertFromUS(x, b))

    
    
if __name__ == "__main__":
    main()
