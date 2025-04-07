class Product:
    def __init__(self, name:str, price:float,in_stock:bool):
        self.name = name
        self.price = price
        self.in_stock = in_stock

if __name__ == "__main__":
    external_data = {
        "name": "example",
        "price": 100,
        "in_stock": 5
    }
    product = Product(
        name=external_data.get("name"),
        price=external_data.get("price"),
        in_stock=external_data.get("in_stock")
    )
    print(product.in_stock) #yine de 5 döner
#ornek_product=Product("örnek", 100, 5)
        #print(ornek_product.in_stock)
#typeları farklı versek te sorun olmaz pydantic bunu önlemek için kullanılır