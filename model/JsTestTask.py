class JsTestTask:

    def __init__(self, name, image, price):
        self.name = name
        self.image = image
        self.price = price

    def __repr__(self):
        return "\nName: {0}, price: {1}, image_url: '{2}'".format(self.name, self.price, self.image)
