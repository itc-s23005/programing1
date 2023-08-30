次のような４つの属性をもつ、Personというクラスを作成してください。ただし、生成されるインスタンスは、さまざまな名前や国籍、生年、住所の場合がありうることを想定してください。更に、これらの属性を示すためのshow_attributes()というメソッドをもたせてください

名前　国籍　生年　住所

名前　英語
名前　name
国籍　nationality
生年　birth
住所　address


class Person:
    def __init__(self,
                name = '',
                nationality = '',
                birth = '',
                address = ''):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address

    def show_attributes(self):
        print("名前", self.name)
        print("国籍", self,nationality)
        print("生まれた年:", self.birth)
        print("住んでいるところ:", self,address)
