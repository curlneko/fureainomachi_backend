from datetime import date

from app.models.users_model import User

dummy_users = [
    User(
        name="Alex",
        current_country="JP",
        birth_country="TW",
        gender="FEMALE",
        spoken_language=["ja", "en"],
        learning_language=["zh"],
        birthday=date(1995, 1, 1),
    ),
    User(
        name="Bob",
        current_country="TW",
        birth_country="TW",
        gender="MALE",
        spoken_language=["zh", "en"],
        learning_language=["ja"],
        birthday=date(1992, 11, 3),
    ),
]
