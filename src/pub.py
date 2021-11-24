class Pub:
    
    def __init__(self, name, till, drinks, foods):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.foods = foods

    def find_drink_by_name(self, name):
        for drink in self.drinks:
            if name.lower() == drink.name.lower():
                return drink

    def add_drink(self, drink):
        self.drinks.append(drink)

    def remove_drink(self, drink_name):
        self.drinks.remove(self.find_drink_by_name(drink_name))

    def find_food_by_name(self, name):
        for food in self.foods:
            if name.lower() == food.name.lower():
                return food

    def add_food(self, food):
        self.foods.append(food)

    def remove_food(self, food_name):
        self.foods.remove(self.find_food_by_name(food_name))

    def get_id(self, customer):
        if customer.age >= 18:
            return True
        else: return False

    def sell_drink(self, customer, drink_name):
        drink = self.find_drink_by_name(drink_name)

        if drink is not None:
            if customer.can_afford(drink) and customer.get_drunkeness() < 8:
                if self.get_id (customer):
                    customer.increase_drunkeness(drink)
                    customer.stomach.append(drink)
                    customer.wallet -= drink.price
                    self.till += drink.price
                    self.drinks.remove(drink)
                elif not drink.alco_status: 
                    customer.stomach.append(drink)
                    customer.wallet -= drink.price
                    self.till += drink.price
                    self.drinks.remove(drink)
        
    def sell_food(self, customer, food):
        customer.wallet -= food.price
        customer.drunkeness -= food.sober_effect
        self.till += food.price