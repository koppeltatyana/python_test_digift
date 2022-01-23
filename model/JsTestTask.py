class JsTestTask:

    def __init__(self, name, image, price):
        self.name = name
        self.image = image
        self.price = price

    def __repr__(self):
        return "Name: {0}, price: {1}, image_url: '{1}'".format(self.name, self.price, self.image)

