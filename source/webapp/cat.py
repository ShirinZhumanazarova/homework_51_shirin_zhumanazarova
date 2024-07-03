from random import randint

CAT_IMAGE_PATH_1 = "images/image1.jpeg"
CAT_IMAGE_PATH_2 = "images/image2.jpeg"
CAT_IMAGE_PATH_3 = "images/image3.jpeg"
class Cat:
    name = ""
    age = 1
    avatar = CAT_IMAGE_PATH_2
    satiety = 40
    happiness = 40
    is_sleep = False


    @classmethod
    def get_image(cls):
        if cls.happiness > 64:
            cls.avatar = CAT_IMAGE_PATH_1
        elif 33 < cls.happiness < 65:
            cls.avatar = CAT_IMAGE_PATH_2
        else:
            cls.avatar = CAT_IMAGE_PATH_3

    @classmethod
    def play(cls):
        if not cls.is_sleep:
            cls.happiness += 15
            cls.satiety -= 10
            cls.get_image()
            if cls.happiness > 100:
                cls.happiness = 100
            if cls.satiety < 0:
                cls.satiety = 0
            chance = randint(1, 3)
            if chance == 3:
                cls.happiness = 0
                cls.get_image()
                if cls.happiness < 0:
                    cls.happiness = 0
        else:
            cls.is_sleep = False
            cls.happiness -= 5
            cls.get_image()
            if cls.happiness < 0:
                cls.happiness = 0

    @classmethod
    def feed(cls):
        if not cls.is_sleep:
            cls.satiety += 15
            cls.happiness += 5
            cls.get_image()
            if cls.happiness > 100:
                cls.happiness = 100
            if cls.satiety > 100:
                cls.satiety = 100
            if cls.satiety > 100:
                cls.happiness -= 30
                cls.get_image()


    @classmethod
    def sleep(cls):
        cls.is_sleep = True

