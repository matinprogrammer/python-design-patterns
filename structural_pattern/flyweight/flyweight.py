"""
    Flyweight Pattern
"""

class CarModel:
    """Flyweight class representing shared car models."""
    _models = {}  # Dictionary to store shared models

    def __new__(cls, name, engine, color):
        key = (name, engine, color)
        if key not in cls._models:
            cls._models[key] = super(CarModel, cls).__new__(cls)
            cls._models[key]._initialized = False
        return cls._models[key]

    def __init__(self, name, engine, color):
        if self._initialized:
            return
        self.name = name
        self.engine = engine
        self.color = color
        self._initialized = True

class Car:
    """Context class that contains unique car information."""
    def __init__(self, model, license_plate):
        self.model = model  # Shared Flyweight object
        self.license_plate = license_plate  # Unique state

    def display_info(self):
        print(f"Car {self.license_plate}: {self.model.name}, Engine: {self.model.engine}, Color: {self.model.color}")

# Client code
if __name__ == '__main__':
    # Creating shared car models (Flyweights)
    model_sedan_red = CarModel("Sedan", "V6", "Red")
    model_sedan_blue = CarModel("Sedan", "V6", "Blue")
    model_suv_black = CarModel("SUV", "V8", "Black")

    # Creating cars with shared models
    car1 = Car(model_sedan_red, "ABC123")
    car2 = Car(model_sedan_red, "DEF456")
    car3 = Car(model_sedan_blue, "GHI789")
    car4 = Car(model_suv_black, "JKL012")

    # Checking if shared models are reused
    print(f"car1 and car2 share the same model: {car1.model is car2.model}")  # True
    print(f"car1 and car3 share the same model: {car1.model is car3.model}")  # False

    # Displaying car information
    car1.display_info()
    car2.display_info()
    car3.display_info()
    car4.display_info()
