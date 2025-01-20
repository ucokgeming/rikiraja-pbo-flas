class Product:
    """
    Kelas untuk merepresentasikan produk di toko.
    """
    def __init__(self, id, name, price, stock):
        """
        Inisialisasi atribut produk.
        
        :param id: ID produk
        :param name: Nama produk
        :param price: Harga produk
        :param stock: Jumlah stok produk
        """
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        """
        Representasi string dari produk untuk debugging.
        """
        return f"<Product {self.name} (ID: {self.id}, Harga: {self.price}, Stok: {self.stock})>"

# Daftar awal produk (peralatan komputer)
products = [
    Product(1, 'Keyboard Mechanical', 500000, 15),
    Product(2, 'Mouse Gaming', 300000, 20),
    Product(3, 'Monitor LED 24 Inch', 2000000, 10),
    Product(4, 'Headset Gaming', 750000, 8),
    Product(5, 'RAM DDR4 16GB', 1200000, 12),
    Product(6, 'SSD 1TB', 1500000, 7),
    Product(7, 'Power Supply 650W', 850000, 5),
    Product(8, 'Casing CPU RGB', 1000000, 9),
    Product(9, 'Motherboard ATX', 1800000, 4),
    Product(10, 'VGA NVIDIA RTX 3060', 6000000, 3),
]
