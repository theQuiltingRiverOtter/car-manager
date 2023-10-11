class CarManager:
    all_cars = {}
    total_cars = 0

    def __init__(self, make: str, model: str, year: int, mileage: int = 0):
        CarManager.total_cars += 1
        self._id = CarManager.total_cars
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = []
        CarManager.all_cars[self._id] = self

    def __repr__(self):
        return f"{self._year} {self._make} {self._model}"

    def __str__(self):
        if len(self._services) == 0:
            return f"{self._year} {self._make} {self._model} with {self._mileage} miles"

        return f"{self._year} {self._make} {self._model} with {self._mileage} miles and the following services:\n{' | '.join(self._services)}"

    @property
    def model(self):
        return self._model

    @model.setter
    def set_model(self, model: str):
        if type(model) == str:
            self._model = model

    @property
    def make(self):
        return self.make

    @make.setter
    def set_make(self, make: str):
        if type(make) == str:
            self._model = make

    @property
    def year(self):
        return self._year

    @year.setter
    def set_year(self, year: int):
        if type(year) == int and year > 1900:
            self._year = year

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def set_mileage(self, mileage):
        if type(mileage) == int and mileage > 0:
            self._mileage = mileage

    @classmethod
    def add_car(self, make, model, year):
        CarManager(make, model, year)

    @classmethod
    def view_all_Cars(self):
        print(CarManager.all_cars)

    @classmethod
    def view_total_number_of_cars(self):
        print(CarManager.total_cars)

    def add_service(self, service: str):
        if type(service) == str:
            self._services.append(service)

    def update_mileage(self, miles: int):
        if type(miles) == int and miles > 0:
            self._mileage += miles


class TerminalApplication:
    def __init__(self):
        pass

    def main_menu(self):
        print("1.Add a car")
        print("2. View all cars")
        print("3. View total number of cars")
        print("4. See a car's details")
        print("5. Service a car")
        print("6. Update mileage")
        print("7. Quit")

    def execute(self):
        self.main_menu()
        while True:
            command = input("What action: ")
            if command == "7":
                break
            elif command == "1":
                make = input("Make: ")
                model = input("Model: ")
                year = int(input("Year: "))
                CarManager.add_car(make, model, year)
            elif command == "2":
                CarManager.view_all_Cars()
            elif command == "3":
                CarManager.view_total_number_of_cars()
            elif command == "4":
                id = int(input("Car ID: "))
                for car in CarManager.all_cars:
                    if car == id:
                        print(CarManager.all_cars[car])
            elif command == "5":
                id = int(input("Car ID: "))
                service = input("Input service performed: ")
                for car in CarManager.all_cars:
                    if car == id:
                        CarManager.all_cars[car].add_service(service)
            elif command == "6":
                id = int(input("Car ID: "))
                mileage = int(input("Input mileage added: "))
                for car in CarManager.all_cars:
                    if car == id:
                        CarManager.all_cars[car].update_mileage(mileage)
            else:
                print("That isn't a command I know")
                self.main_menu()


terminal_app = TerminalApplication()

terminal_app.execute()
