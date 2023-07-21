from person_class import Person

class Enemy(Person):
    def __init__(self, weapon, first_name, last_name, health_score, friend):
        self.weapon = weapon
        super().__init__(first_name, last_name, health_score, friend)

    def heart(self, other):
        if self.weapon == "rock":
            other.health_score -= 10
        elif self.weapon == "knife":
            other.health_score -= 5
        else:
            other.health_score -= 2
        print(other.health_score)


Anna = Person("Anna", "Annovna", 98, False)
Alex = Enemy("rock", "Alex", "Alexon", 98, False)
Alex.heart(Anna)