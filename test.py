# # # # # # # # # # import json
# # # # # # # # # # from os import read
# # # # # # # # # # from pprint import pprint
# # # # # # # # # # from random import choice, randint
# # # # # # # # # # from uuid import uuid4
# # # # # # # # # #
# # # # # # # # # # js = """{
# # # # # # # # # #     'nimadir': [
# # # # # # # # # #         {12:12},
# # # # # # # # # #         {12:12},
# # # # # # # # # #         {12:12},
# # # # # # # # # #         {12:12},
# # # # # # # # # #         {12:12},
# # # # # # # # # #         {12:12},
# # # # # # # # # #         {12:12},
# # # # # # # # # #     ]
# # # # # # # # # # }"""
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # class User:
# # # # # # # # # #     def __init__(self):
# # # # # # # # # #         self.username = choice(["ali", "vali", "gani"])
# # # # # # # # # #         self.age = randint(10, 80)
# # # # # # # # # #         self.id = uuid4()
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # data = {
# # # # # # # # # #     "users": []
# # # # # # # # # # }
# # # # # # # # # #
# # # # # # # # # # for i in range(10):
# # # # # # # # # #     data["users"].append(User().__dict__)
# # # # # # # # # #     data["users"][i]["id"] = str(data["users"][i]["id"])
# # # # # # # # # # with open("base.json", "w", encoding="utf-8") as f:
# # # # # # # # # #     json.dump(data, f, indent=4)
# # # # # # # # # #
# # # # # # # # # # with open("base.json", "r", encoding="utf-8") as f:
# # # # # # # # # #     a = json.load(f)
# # # # # # # # # #
# # # # # # # # # # print(read("base.json"))
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # class University:
# # # # # # # # #     def __init__(self, name):
# # # # # # # # #         self.name = name
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # univer1 = University("TATU")
# # # # # # # # # univer2 = University("TDTU")
# # # # # # # # # univer3 = University("SamDU")
# # # # # # # # # University.__delattr__(univer1, "name")
# # # # # # # # # print()
# # # # # # # # # print(University("TATU").name)
# # # # # # # # #
# # # # # # # # # kg = 32
# # # # # # # # #
# # # # # # # # # tonnada = kg / 1000
# # # # # # # # #
# # # # # # # # # print(tonnada)
# # # # # # # # # import math
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # def func(a, b, t):
# # # # # # # # #     y = math.pow(math.e, (-b * t)) * math.sin(a * t + b) - math.pow(abs(b * t + a), 0.5)
# # # # # # # # #     S = b * math.sin(a * math.pow(t, 2) * math.cos(2 * t)) - 1
# # # # # # # # #
# # # # # # # # #     return f"y = {y}\nS = {S}"
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # print(func(-0.5, 1.7, 0.44))
# # # # # # # #
# # # # # # # #
# # # # # # # # # def f(a, b, c):
# # # # # # # # #     cnt = 0
# # # # # # # # #     for i in (a, b, c):
# # # # # # # # #         if i > 0:
# # # # # # # # #             cnt += 1
# # # # # # # # #
# # # # # # # # #     return cnt
# # # # # # # # #
# # # # # # # # # print(f(12, -1, 3))
# # # # # # # # import math
# # # # # # # #
# # # # # # # #
# # # # # # # # def func(n, x, i=2, S=0):
# # # # # # # #     if n == 1:
# # # # # # # #         return 0
# # # # # # # #     elif n == 2:
# # # # # # # #         return -1 ** 2 * x ** (2 * 2) / math.factorial(2 * 2)
# # # # # # # #     if i > n:
# # # # # # # #         return S
# # # # # # # #     S += -1 ** i * x ** (2 * i) / math.factorial(2 * i)
# # # # # # # #     return func(n, x, i=i + 2, S=S)
# # # # # # # #
# # # # # # # #
# # # # # # # # print(func(6, 2))
# # # # # # # #
# # # # # # # # #
# # # # # # # # # def fun(n, x):
# # # # # # # # #     S = 0
# # # # # # # # #     i = 2
# # # # # # # # #     if n == 1:
# # # # # # # # #         return 0
# # # # # # # # #     elif n == 2:
# # # # # # # # #         return -1 ** 2 * x ** (2 * 2) / math.factorial(2 * 2)
# # # # # # # # #     else:
# # # # # # # # #         while i < n:
# # # # # # # # #             S += -1 ** i * x ** (2 * i) / math.factorial(2 * i)
# # # # # # # # #             i += 2
# # # # # # # # #     return S
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # print(fun(10, 2))
# # # # # # #
# # # # # # # # def f(narx):
# # # # # # # #     i = 1.2
# # # # # # # #     narxlar = {}
# # # # # # # #     while i <= 2:
# # # # # # # #         narxlar[f"{i}kg"] = i * narx
# # # # # # # #         i += 0.2
# # # # # # # #         i = round(i, 1)
# # # # # # # #     return narxlar
# # # # # # # #
# # # # # # # #
# # # # # # # # print(f(12))
# # # # # # #
# # # # # # #
# # # # # # # def f(davlat_nomi):
# # # # # # #     qitalar = [
# # # # # # #         {
# # # # # # #             "country": "Afghanistan",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Albania",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Algeria",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "American Samoa",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Andorra",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Angola",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Anguilla",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Antarctica",
# # # # # # #             "continent": "Antarctica"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Antigua and Barbuda",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Argentina",
# # # # # # #             "continent": "South America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Armenia",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Aruba",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Australia",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Austria",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Azerbaijan",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Bahamas",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Bahrain",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Bangladesh",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Barbados",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Belarus",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Belgium",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Belize",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Benin",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Bermuda",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Bhutan",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Bolivia",
# # # # # # #             "continent": "South America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Bosnia and Herzegovina",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Botswana",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Bouvet Island",
# # # # # # #             "continent": "Antarctica"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Brazil",
# # # # # # #             "continent": "South America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "British Indian Ocean Territory",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Brunei",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Bulgaria",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Burkina Faso",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Burundi",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Cambodia",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Cameroon",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Canada",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Cape Verde",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Cayman Islands",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Central African Republic",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Chad",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Chile",
# # # # # # #             "continent": "South America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "China",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Christmas Island",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Cocos (Keeling) Islands",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Colombia",
# # # # # # #             "continent": "South America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Comoros",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Congo",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Cook Islands",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Costa Rica",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Croatia",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Cuba",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Cyprus",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Czech Republic",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Denmark",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Djibouti",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Dominica",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Dominican Republic",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "East Timor",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Ecuador",
# # # # # # #             "continent": "South America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Egypt",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "El Salvador",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "England",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Equatorial Guinea",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Eritrea",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Estonia",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Ethiopia",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Falkland Islands",
# # # # # # #             "continent": "South America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Faroe Islands",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Fiji Islands",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Finland",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "France",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "French Guiana",
# # # # # # #             "continent": "South America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "French Polynesia",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "French Southern territories",
# # # # # # #             "continent": "Antarctica"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Gabon",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Gambia",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Georgia",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Germany",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Ghana",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Gibraltar",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Greece",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Greenland",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Grenada",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Guadeloupe",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Guam",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Guatemala",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Guinea",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Guinea-Bissau",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Guyana",
# # # # # # #             "continent": "South America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Haiti",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Heard Island and McDonald Islands",
# # # # # # #             "continent": "Antarctica"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Holy See (Vatican City State)",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Honduras",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Hong Kong",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Hungary",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Iceland",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "India",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Indonesia",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Iran",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Iraq",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Ireland",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Israel",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Italy",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Ivory Coast",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Jamaica",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Japan",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Jordan",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Kazakhstan",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Kenya",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Kiribati",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Kuwait",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Kyrgyzstan",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Laos",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Latvia",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Lebanon",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Lesotho",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Liberia",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Libyan Arab Jamahiriya",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Liechtenstein",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Lithuania",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Luxembourg",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Macao",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "North Macedonia",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Madagascar",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Malawi",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Malaysia",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Maldives",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Mali",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Malta",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Marshall Islands",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Martinique",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Mauritania",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Mauritius",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Mayotte",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Mexico",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Micronesia, Federated States of",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Moldova",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Monaco",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Mongolia",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Montenegro",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Montserrat",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Morocco",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Mozambique",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Myanmar",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Namibia",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Nauru",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Nepal",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Netherlands",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Netherlands Antilles",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "New Caledonia",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "New Zealand",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Nicaragua",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Niger",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Nigeria",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Niue",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Norfolk Island",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "North Korea",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Northern Ireland",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Northern Mariana Islands",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Norway",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Oman",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Pakistan",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Palau",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Palestine",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Panama",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Papua New Guinea",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Paraguay",
# # # # # # #             "continent": "South America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Peru",
# # # # # # #             "continent": "South America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Philippines",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Pitcairn",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Poland",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Portugal",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Puerto Rico",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Qatar",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Reunion",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Romania",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Russian Federation",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Rwanda",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Saint Helena",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Saint Kitts and Nevis",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Saint Lucia",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Saint Pierre and Miquelon",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Saint Vincent and the Grenadines",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Samoa",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "San Marino",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Sao Tome and Principe",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Saudi Arabia",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Scotland",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Senegal",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Serbia",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Seychelles",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Sierra Leone",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Singapore",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Slovakia",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Slovenia",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Solomon Islands",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Somalia",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "South Africa",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "South Georgia and the South Sandwich Islands",
# # # # # # #             "continent": "Antarctica"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "South Korea",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "South Sudan",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Spain",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Sri Lanka",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Sudan",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Suriname",
# # # # # # #             "continent": "South America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Svalbard and Jan Mayen",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Swaziland",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Sweden",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Switzerland",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Syria",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Tajikistan",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Tanzania",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Thailand",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "The Democratic Republic of Congo",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Togo",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Tokelau",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Tonga",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Trinidad and Tobago",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Tunisia",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Turkey",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Turkmenistan",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Turks and Caicos Islands",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Tuvalu",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Uganda",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Ukraine",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "United Arab Emirates",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "United Kingdom",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "United States",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "United States Minor Outlying Islands",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Uruguay",
# # # # # # #             "continent": "South America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Uzbekistan",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Vanuatu",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Venezuela",
# # # # # # #             "continent": "South America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Vietnam",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Virgin Islands, British",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Virgin Islands, U.S.",
# # # # # # #             "continent": "North America"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Wales",
# # # # # # #             "continent": "Europe"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Wallis and Futuna",
# # # # # # #             "continent": "Oceania"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Western Sahara",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Yemen",
# # # # # # #             "continent": "Asia"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Zambia",
# # # # # # #             "continent": "Africa"
# # # # # # #         },
# # # # # # #         {
# # # # # # #             "country": "Zimbabwe",
# # # # # # #             "continent": "Africa"
# # # # # # #         }
# # # # # # #     ]
# # # # # # #
# # # # # # #     for country in qitalar:
# # # # # # #         if davlat_nomi in country.values():
# # # # # # #             return country["continent"]
# # # # # # #     return None
# # # # # # #
# # # # # # # print("Davlat nomini Ingliz tilida va toliq kiriting. Yoqsa topilmaydi...")
# # # # # # # davlat = input(">>> ")
# # # # # # # print(f(davlat))
# # # # # #
# # # # # #
# # # # # # # def fun(A, B):
# # # # # # #     if A != B:
# # # # # # #         A = max(A, B)
# # # # # # #         B = A
# # # # # # #     else:
# # # # # # #         A, B = 0, 0
# # # # # # #     return f"A={A}\nB={B}"
# # # # # # #
# # # # # # #
# # # # # # # print(fun(1, 2))
# # # # # #
# # # # # #
# # # # # # # def f(n):
# # # # # # #     S = 0
# # # # # # #     while n > 0:
# # # # # # #         S += n % 10
# # # # # # #         n //= 10
# # # # # # #
# # # # # # #     return S
# # # # # # #
# # # # # # #
# # # # # # # for n in range(100_000, 1_000_000):
# # # # # # #     if f(n // 1_000) == f(n % 1_000):
# # # # # # #         print(n)
# # # # # #
# # # # # #
# # # # # # def fun(asos1, asos2, h):
# # # # # #     P = asos1 + asos2 + (h ** 2 + (asos2 - asos1) ** 2) ** 0.5
# # # # # #     S = (asos1 + asos2) / 2 * h
# # # # # #
# # # # # #     return P, S
# # # # # #
# # # # # #
# # # # # # a1 = 10
# # # # # # b1 = 20
# # # # # # h1 = 15
# # # # # #
# # # # # # a2 = 20
# # # # # # b2 = 10
# # # # # # h2 = 13
# # # # # #
# # # # # # P1 = fun(a1, b1, h1)[0]
# # # # # # P2 = fun(a2, b2, h2)[0]
# # # # # #
# # # # # # S1 = fun(a1, b1, h1)[1]
# # # # # # S2 = fun(a2, b2, h2)[1]
# # # # # #
# # # # # # all_perimetr = P1 + P2
# # # # # # all_yuza = S1 + S2
# # # # # # print(all_perimetr, all_yuza)
# # # # #
# # # # #
# # # # # # a = """Bu
# # # # # # ko'p
# # # # # # qatorli
# # # # # # satr"""
# # # # #
# # # # # # print(list(i for i in a if i.isalpha() and i != 'o'))
# # # # #
# # # # #
# # # # # # from PIL import ImageColor
# # # # # # hex = input('Enter HEX value: ')
# # # # # # rgb = ImageColor.getcolor(hex, "RGB")
# # # # # #
# # # # # # print(rgb)
# # # # #
# # # # # # hex = input('Enter HEX value: ').lstrip('#')
# # # # # #
# # # # #
# # # # #
# # # # # # print(int("12", 11))
# # # #
# # # # # hex_ = "#cccccc".lstrip('#')
# # # # #
# # # # # if len(hex_) > 3:
# # # # #     rgb = tuple(int(hex_[i:i+2], 16) for i in (0, 2, 4))
# # # # #     print('RGB value =', rgb)
# # # # # else:
# # # # #     rgb = tuple(int(hex_[i], 16) for i in (0, 1, 2))
# # # # #     print('RGB value =', rgb)
# # # # # #
# # # # # hex_str = "#"
# # # # # for i in rgb:
# # # # #     a = hex(i)
# # # # #     b = a[2:]
# # # # #     hex_str += b
# # # # #
# # # # # print(hex_str)
# # # # #
# # # # #
# # # # # # def f(n):
# # # # # #     if n == 0:
# # # # # #         return 1
# # # # # #     else:
# # # # # #         return n * f(n - 1)
# # # # # #
# # # # # #
# # # # # # print(f(5))
# # # #
# # # # import random
# # # # ball = 0
# # # # while True:
# # # #     if ball == 100:
# # # #         print("Tabriklaymiz 100 ball")
# # # #         break
# # # #     print("===============================")
# # # #     a = random.randint(1, 10)
# # # #     b = random.randint(1, 10)
# # # #     c = random.randint(1, 20)
# # # #     print(f"{a} + {b} = {c}")
# # # #     answer = int(input(">>> "))
# # # #     if a + b == c and answer == 1:
# # # #         ball += 10
# # # #         print(f"Togri sizning ball >>> {ball}")
# # # #     elif a + b != c and answer == 0:
# # # #         ball += 10
# # # #         print(f"Togri sizning ball >>> {ball}")
# # # #     else:
# # # #         if ball > 0:
# # # #             ball -= 10
# # # #         print(f"notogri sizning ball >>> {ball}")
# # # #
# # # import json
# # # from pprint import pprint
# # #
# # # import openpyxl
# # #
# # # #
# # # #
# # # # book = openpyxl.Workbook()
# # # #
# # # # sheet = book.active
# # # #
# # # # sheet["A1"] = "Hello"
# # # # sheet["B1"] = "Hello"
# # # #
# # # # # sheet[1][0].value = "world"
# # # # sheet.cell(row=100, column=10).value = "sss"
# # # #
# # # # book.save("test.xlsx")
# # # # book.close()
# # #
# # # # book = openpyxl.open("test.xlsx")
# # # # sheet = book.active
# # #
# # #
# # # # with open("data.json", "r") as file:
# # # #     data = json.load(file)
# # # #     genres = data["genres"]
# # # #     movies = data["movies"]
# # # #
# # # # book = openpyxl.open("test.xlsx", read_only=True)
# # # #
# # # # sheet = book.active
# # # # cells = sheet["C9": "F14"]
# # # #
# # # # for row in sheet.iter_rows(min_row=145, min_col=7):
# # # #     print(row.value)
# # #
# # # # for year, genres, director, actors in cells:
# # # #     print(year.value, genres.value, director.value, actors.value)
# # #
# # # # sheet["A1"].value = "ID"
# # # # sheet["B1"].value = "TITLE"
# # # # sheet["C1"].value = "YEAR"
# # # # sheet["D1"].value = "GENRES"
# # # # sheet["E1"].value = "DIRECTOR"
# # # # sheet["F1"].value = "ACTORS"
# # # #
# # # # row = 2
# # # # for movie in movies:
# # # #     sheet.cell(row, 1).value = movie["id"]
# # # #     sheet.cell(row, 2).value = movie["title"]
# # # #     sheet.cell(row, 3).value = movie["year"]
# # # #     sheet.cell(row, 4).value = ", ".join(movie["genres"])
# # # #     sheet.cell(row, 5).value = movie["director"]
# # # #     sheet.cell(row, 6).value = movie["actors"]
# # # #     row += 1
# # # #
# # # # book.save("test.xlsx")
# # # # book.close()
# # #
# # # # print(sheet.cell(sheet.max_row, sheet.max_column).value)
# # #
# # #
# # # # for i in range(1, sheet.max_row + 1):
# # # #     for j in range(1, sheet.max_column + 1):
# # # #         if sheet.cell(i, j).value:
# # # #             print(sheet.cell(i, j).value)
# # lst = [55, 123, 435, 5, 23, 76, 907, 89, 489, 111, 3]
# #
# #
# # def fib(n):
# #     if n == 1 or n == 2:
# #         return 1
# #     return fib(n - 1) + fib(n - 2)
# #
# #
# # def search_fibs(lst):
# #     fibs = []
# #     for elem in lst:
# #         for j in range(len(str(elem))):
# #             elem_number = str(elem)[::-1][:j + 1]
# #             i = 1
# #             bol = True
# #             while fib(i) <= int(elem_number) and bol:
# #                 if fib(i) == int(elem_number):
# #                     fibs.append(elem)
# #                     bol = False
# #                 i += 1
# #             if elem in fibs:
# #                 break
# #     return fibs
# #
# #
# # print(search_fibs(lst))
#
#
# # import math
# #
# # a = 1.5
# # b = 15.5
# # x = -2.9
# #
# #
# # def f(a, b, x):
# #     f = math.pow(x ** 2 + b, 0.5) - b ** 2 * math.pow(math.sin(x + a), 3) / x
# #     y = math.cos(x ** 3) ** 2 - x / math.pow(a ** 2 + b ** 2, 0.5)
# #     return f, y
# #
# #
# # print(f(a, b, x))
#
# # A = 13
# # B = 4
#
#
# # def fun(A, B):
# #     if A == 0 or B == 0:
# #         return False
# #     elif A % 2 == 0 and B % 2 == 0 or A % 2 != 0 and B % 2 != 0:
# #         return True
# #     else:
# #         return False
# #
# #
# # print(fun(10, 20))
# # import math
# #
# # R1 = 9
# # R2 = 6
# #
# #
# # def func(R1, R2):
# #     S1 = math.pi * R1 ** 2
# #     S2 = math.pi * R2 ** 2
# #     S3 = S1 - S2
# #     return S3
# #
# #
# # print(func(10, 7))
#
# #
# # a = 10
# # b = -3
# # c = -7
# #
# # musbat_sonlar = 0
# # manfiy_sonlar = 0
# # for i in (a, b, c):
# #     if i < 0:
# #         manfiy_sonlar += 1
# #     elif i > 0:
# #         musbat_sonlar += 1
# #
# # print(musbat_sonlar, manfiy_sonlar)
#
# # A = 12
# # B = 5
# # C = -7
# # amal = input("1. ko‘paytirish, 2. bo‘lish, 3. qo‘shish, 4. ayirish\n>>> ")
# #
# # if not amal.isdigit():
# #     print("ERROR")
# # elif int(amal) == 1:
# #     print("{} * {} * ({}) = {}".format(A, B, C, A*B*C))
# # elif int(amal) == 2:
# #     print("{} / {} / ({}) = {}".format(A, B, C, A/B/C))
# # elif int(amal) == 3:
# #     print("{} + {} + ({}) = {}".format(A, B, C, A+B+C))
# # elif int(amal) == 4:
# #     print("{} - {} - ({}) = {}".format(A, B, C, A-B-C))
# # else:
# #     print("ERROR")
#
#
# # n = int(input(">>> "))
# # x = -0.5
# #
# # S = x
# #
# # for i in range(2, n + 1):
# #     S += (-1) ** i * x ** i / i
# #
# # print(S)
#
# # a = 3
# # b = 6
# #
# # S = 0
# #
# # for i in range(a, b + 1):
# #     S += i
# #
# # print(S)
#
# #
# # matn = matn.replace("r", "").replace("R", "")
# # print(matn)
#
# # matn = "Recursiv funksiyalar juda qiyin misollar"
# #
# # count_spaces = matn.count(" ")
# # print(count_spaces)
# #
# # list1 = [10, 20, 30, 40]
# # list2 = [100, 200, 300, 400]
# # list2.reverse()
# #
# # for i in range(len(list1)):
# #     print(list1[i], list2[i])
#
# # tuple1 = (11, 22)
# # tuple2 = (99, 88)
# #
# #
# # tuple1, tuple2 = tuple2, tuple1
# #
# # print(tuple1, tuple2)
#
# # sampleDict = {
# #     "name": "Kelly",
# #     "age": 25,
# #     "salary": 8000,
# #     "city": "New york"
# # }
# #
# # keys = ["name", "salary"]
# # result = {}
# # for i in keys:
# #     result[i] = sampleDict[i]
# #
# # print(result)
#
# # with open("odamlar.txt", "a") as file:
# #     file.write(" Xayr, odamlar!")
#
#
# toplam = ["hello", "world", "salom", "dunyo"]
