from datetime import date

from app.models.users_model import User

dummy_users = [
    User(
        name="Alex",
        current_country="Japan",
        birth_country="Taiwan",
        gender="FEMALE",
        spoken_language=["JAPANESES", "ENGLISH"],
        learning_language=["CHINESE"],
        birthday=date(1995, 1, 1),
    ),
    User(
        name="Bob",
        current_country="Taiwan",
        birth_country="Taiwan",
        gender="MALE",
        spoken_language=["CHINESE", "ENGLISH"],
        learning_language=["JAPANESES"],
        birthday=date(1992, 11, 3),
    ),
]
