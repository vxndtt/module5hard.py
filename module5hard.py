import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = int(password)
        self.age = int(age)

    def __eq__(self, other):
        return self.password == other.password

    def __hash__(self):
        return hash(self.password)


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user['nickname'] == nickname and user['password'] == password:
                self.current_user = user
                print(f'Вход выполнен, {nickname}')
                return

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.users.append(nickname)
            print(f'Регистрация и вход выполнены, {nickname}')
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        return self.current_user is None

    def add(self, *video):
        for video in self.videos:
            if video == video.name:
                break
            else:
                self.videos.append(Video)
            return self.videos

    def get_videos(self, word):
        for title in self.videos:
            if word in title.lower():
                self.videos.append(title)
                return self.videos

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт чтобы смотреть видео')
        elif title in self.videos:
            if '18+' in title and self.age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу.')
            else:
                print(f'Видео {title} воспроизводится')



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
