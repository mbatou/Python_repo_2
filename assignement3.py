from abc import ABC, abstractmethod

class ProductAbstract:
    create_product = ''
    edit_product = ''
    get_product_by_id = ''
    get_all_product = ''
    upload_product_image = ''
    delete_product = ''

class ProductManager():
    @abstractmethod
    def get_product_by_id(self):
        pass
    def edit_product(self):
        pass
    def create_product(self):
        pass
    def get_all_product(self):
        pass
    def upload_product_image(self):
        pass
    def delete_product(self):
        pass

# trying to add a new class by calling the abstractmethod above

class trainee(ProductManager):
    def get_product_by_id(self):
        pass
    def edit_product(self):
        pass
    def create_product(self):
        pass
    def get_all_product(self):
        pass
    def upload_product_image(self):
        pass
    def delete_product(self):
        pass

new_trainee = ProductManager()
new_trainee.edit_product()
print("new trainee is on work")
