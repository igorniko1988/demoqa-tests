from dataclasses import dataclass
from pathlib import Path
from demoqa_tests.helpers import resourse
import pytest
from faker import Faker


fake = Faker()


@dataclass
class User:
    firstname: str
    lastname: str
    useremail: str
    gender: str
    hobbie: str
    subject: str = 'Maths'
    text: str = "Meet push whole"
    dateofbirth: str = "17 July,1963"
    usernumber: str = "8012831232"
    state: str = "Haryana"
    city: str = "Karnal"
    picture: str = resourse.get_file("test_file.txt")
