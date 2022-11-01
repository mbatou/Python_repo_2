from abc import ABC, abstractmethod

class Product:
    id = 0
    name = ''
    description = ''
    type = ''
    price = 0.0
    image = ''

    def __init__(self, id, name, description, type, price, image):
        pass

class ProductAbstract(ABC):

    @abstractmethod
    def create_product(self, product: Product):
        pass
    
    @abstractmethod
    def edit_product(self, id):
        pass
    
    @abstractmethod
    def get_product_by_id(self, id):
        pass
    
    @abstractmethod
    def upload_product_image(self, image):
        pass

    @abstractmethod
    def delete_product(self, id):
        pass

class ProductManager(ProductAbstract):

    def __init__(self, product: Product):
        self.product = product

    def create_product(self):
        print(f'{self.product.name} has been added to the warehouse')

    def edit_product(self):
        print(f'Product id - {self.product.id} has been added')

    def get_product_by_id(self):
        pass
    
    def upload_product_image(self):
        print('Product image has been uploaded: ' + self.product.image)
    
    def delete_product(self):
        pass

product = Product(1, 'CocaCola', 'The new way to save you from heat', 'baverage', 100.00, 'https://www.coca-colacompany.com/')

product_manager = ProductManager(product)
product_manager.create_product()
product_manager.edit_product()
product_manager.get_product_by_id()
product_manager.upload_product_image()
product_manager.delete_product()