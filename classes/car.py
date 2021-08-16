class Car:
    def __init__(self, max_speed):
        self._speed = 0
        self.max_speed = max_speed

    def get_speed(self):
        return self._speed

    def accelerate(self, speed_increase):
        self._make_noise("VROOM!")
        new_speed = self._speed + speed_increase
        self._speed = min(self.max_speed, new_speed)

    def brake(self, speed_decrease):
        self._make_noise("Screeeeech!")
        if self._speed - speed_decrease < 0:
            self._speed = 0
        else:
            self._speed -= speed_decrease

    def _make_noise(self, noise):
        print(noise)

c = Car(180)
c.accelerate(20)
print(c.get_speed()) # 20
c.accelerate(15)
print(c.get_speed()) # 35