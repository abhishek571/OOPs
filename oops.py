class Abhi:
    def __init__(self):
        print("WELCOME TO OUR SHOP")
    
    def color(self):
        print("the color is color")

    def Buy(self):
        print(f"Do you Want to BUY?")


class ABC(Abhi):
     def Product(self):
        print('Product is tshirt')

   

nm=ABC()
 
nm.color()
nm.Product()
nm.Buy()

