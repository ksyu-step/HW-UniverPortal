from config import app
from views.home_controller import HomeController
from views.users_controller import UsersController



if __name__ == '__main__':

    hc = HomeController()
    uc = UsersController()

    app.run(port=12345)  # Для второго приложения открываем другой порт
