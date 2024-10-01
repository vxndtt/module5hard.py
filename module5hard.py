import time


class User:
    def __init__(self, nickname: str, password, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __eq__(self, other):
        return self.password == other.password

    def __hash__(self):
        return hash(self.password)


class Video:
    def __init__(self, title: str, duration: int, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
                print(f'Вход выполнен, {nickname}')

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
            print(f'Вход выполнен, {nickname}')
        else:
            print(f'Пользователь {nickname} уже существует')
            return

    def log_out(self):
        self.current_user = None
        return self.current_user

    def add(self, *new_videos):
        for title in new_videos:
            if title not in self.videos:
                self.videos.append(title)
            else:
                break

    def get_videos(self, word):
        word = word.lower()
        result = []
        for video in self.videos:
            if word in video.title.lower():
                result.append(video)
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        if self.current_user.age < 18: #and adult_mode = True
            print('Вам нет 18 лет, пожалуйста покиньте страницу.')
            return
        if title in self.videos:
            print(f'Видео {title} воспроизводится')
            return
            #дополнение


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
