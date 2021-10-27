import logging
import json


class User:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def user_json(self):
        user_data = {'name': self.name,
                     'surname': self.surname,
                     'age': self.age,
                     'gender': self.gender}

        with open(f'{self.name}_{self.surname}.json', 'w') as u:
            json.dump(user_data, u, indent=2)
        return f'{self.name}_{self.surname}'


class Calculator:
    @staticmethod
    def calculate():
        while True:
            number1 = input('Number_1     ')
            sign = input('Sign     ')
            number2 = input('Number_2     ')
            out = eval(f'{number1}{sign}{number2}')
            print(out)
            logging.info('calculate')
            logging.info(f'{number1}{sign}{number2} = {out}')
            choice = input('If you want to continue insert 1, otherwise insert other key to exit     ')
            if choice != '1':
                break


class Converter:
    data = {'b': 1, "kb": 1024, 'mb': 1024 ** 2, 'gb': 1024 ** 3, 'tb': 1024 ** 4, 'pb': 1024 ** 5}
    weight = {'pounds': 1, 'kg': 2.2}
    height = {'centimeter': 1, 'inches': 2.54, 'feet': 30.48, 'meter': 100}
    length = {'millimeter': 1, 'centimeter': 10, 'decimeter': 100, 'meter': 1000, 'kilometer': 100000}
    area = {'m2': 1, 'a': 100, 'ha': 10000, 'km2': 1000000}
    types = {'1': data, '2': weight, '3': height, '4': length, '5': area}

    @staticmethod
    def convert():
        while True:
            print(' data - 1 \n weight - 2 \n height - 3 \n length - 4 \n area - 5 \n age - 6 \n discount - 7')
            choose_type = input('Please choose from the types     ')
            logging.info('convert')
            if choose_type in Converter.types.keys():
                a = Converter.types[choose_type]
                for i in a.keys():
                    print(i)
                converter = (input('type_1     '), input('type_2     '))
                count = int(input('count     '))
                out = count * Converter.types[choose_type][converter[0]] / Converter.types[choose_type][converter[1]]
                logging.info(
                    f'{count}{Converter.types[choose_type]} --> {Converter.types[choose_type]} = {out}')
                print(out)
            elif choose_type == '6':
                age = int(input('Year of birth     '))
                out = 2021 - age
                logging.info(f'2021 - {age} = {out}')
                print(out)
            else:
                original_price = int(input('Original price     '))
                discount = int(input('Discount(% off)     '))
                out = original_price * (1 - discount / 100)
                logging.info(f'{original_price} * (1 - {discount} / 100) = {out}')
                print(out)
            choice = input('If you want to continue insert 1, otherwise insert other key     ')
            if choice != '1':
                break


class SpellChecker:
    @staticmethod
    def text_import():
        logging.info('text import')
        text = input(
            ' If you want to type the text, insert 1. \n If you want to read the text from file, insert other key     ')
        if text == '1':
            result = input('Please type the text here      ')
        else:
            path = input('Please insert the path to the file here     ')
            with open(f'{path}', 'r', encoding="utf8", errors='ignore') as f:
                result = f.read()

        return result

    @staticmethod
    def correction():
        while True:
            text = SpellChecker.text_import()
            text_split = text.split()
            new_text = text_split[0].capitalize()
            index = 1
            while index < len(text_split):
                if text_split[index] == 'i':
                    new_text += ' I'
                    index += 1
                elif (text_split[index][-1] in '.?!') and (text_split[index] != text_split[-1]):

                    new_text += f' {text_split[index]}' + f' {text_split[index + 1].capitalize()}'
                    index += 2
                else:
                    new_text += f' {text_split[index]}'
                    index += 1

            text_saving = input('Please input text file name for saving')
            with open(f"{text_saving}.txt", 'w') as output:
                output.write(new_text)

            logging.info('text saving')

            print(new_text)
            choice = input('If you want to continue insert 1, otherwise insert other key     ')
            if choice != '1':
                break


class Interface:
    @staticmethod
    def interface():
        print('Pleas input your personal information')
        user = User(input('name     '), input('surname     '), input('age     '), input('gender     '))
        logging.basicConfig(filename=f"{user.user_json()}.log", level=logging.INFO)

        while True:
            choose = input(' Calculator - 1 \n Converter - 2 \n Text correction - other key     ')
            if choose == '1':
                Calculator.calculate()
            elif choose == '2':
                Converter.convert()
            else:
                SpellChecker.correction()

            choice = input('Continue - 1, Exit - other key     ')
            if choice != '1':
                break


#Interface.interface()
