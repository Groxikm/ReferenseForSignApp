import csv


class AutorisationServise:

    def __init__(self) -> None:
        self._filename = 'authorisation_service\\credentials.csv'
        self.username_password_dict = {}

        try:
            with open(self._filename, mode='r') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    if len(row) >= 2:
                        self.username_password_dict[row[0]] = row[1]
        except FileNotFoundError:
            print("Файл не найден")

    def check_credentials(self, login: str, password: str) -> bool:
        if login in self.username_password_dict:
            return self.username_password_dict[login] == password
        return False
