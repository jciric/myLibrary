class Books:
    amount_of_books = 0
    monthly_money: int = 10000
    last_id = 0

    def __init__(self, name, author, category, rating, cost = None):
        self.author = author
        self.name = name
        self.cost = cost
        self.category = category
        self.rating = rating
        self.id = Books.last_id

        Books.amount_of_books += 1
        Books.last_id += 1

    def match(self, filter):
        if filter in self.name:
            print(self.name)
        elif filter in self.author:
            print(self.author)
        elif filter in self.id:
            print("{0} : {1}".format(self.author, self.name))

    @classmethod
    def updated_monthly_money(cls, cost):
        cls.monthly_money = cls.monthly_money - cost



