def information_to_list(f_name):
    """Берёт информацию из файла и преобразовывает её в список"""
    with open(f_name) as f:
        result = []
        for i in f:
            result.append(i.strip('\n'))
    return result


class User:
    """Информация о человеке"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def read_information(self):
        """Выводит информацию о пользователе"""
        return f"{self.first_name} {self.last_name}, {self.age}"


    def enter_to_file(self):
        """Записывает информацию в файл"""
        file_name = 'txt_files/information_about_all_users.txt'
        with open(file_name, 'a') as f:
            f.write(f"{self.first_name} {self.last_name}, {self.age}\n")


    def checking_file(self):
        """Проверяет, есть ли информация о пользователе в файле"""
        information = f"{self.first_name} {self.last_name}, {self.age}"
        try:
            file_name = 'txt_files/information_about_all_users.txt'
            with open(file_name) as f:
                users = f.read()
        except FileNotFoundError:
            print("File created.")
        else:
            return True if information in users else False
