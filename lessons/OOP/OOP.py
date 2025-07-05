class ShoppingCart:
    
    def __init__(attr):
        attr.items = []
    
    def addItem(attr,name:str,qty:int,price:float):
        attr.items.append({
            name:name,
            qty:qty,
            price:price
        })
    
    def removeItem(attr,name:str):
        for item in attr.items:
            if item[0] == name:
                attr.items.remove(item)
                break

    # def numbers(*num:int,**kaargs):
    #   return num

    def calculateTotal(attr) -> float:
        total = 0

        for name,qty,price in attr.items:
            total += (qty * price)
        
        return total
    
    def summary(attr):
        print("Cart content\n")

        for name, qty, price in attr.items:
            print(f"{name}: {qty} @ Ksh {price}")
        print(f"\nTotal: Ksh. {attr.calculateTotal():.2f}")

class TaxedCart(ShoppingCart):
    def __init__(self, tax_rate: float):
        super().__init__()
        self.tax_rate = tax_rate
    
    def calculate_total(self) -> float:
        """Override to add tax on the initial total."""
        initial_total = super().calculate_total()
        tax = initial_total * self.tax_rate
        return initial_total + tax

if __name__ == "__main__":
    cart:ShoppingCart = ShoppingCart()
    cart.addItem("Mangoes",10,20)
    cart.addItem("Guava",86,10)
    cart.addItem("Apples",1200,10)

    cart.summary()

    print("\n>>> Ordinary Cart <<<\n")
    cart.summary()