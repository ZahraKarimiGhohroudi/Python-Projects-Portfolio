import secrets
import string
from abc import ABC, abstractmethod
from typing import Optional
import nltk


class PasswordGenerator(ABC):
    """
    Base class for generating password
    """

    @abstractmethod
    def generate(self) -> str:
        """
        Subclasses should override this method to generate password
        """


class RandomPasswordGenerator(PasswordGenerator):
    """
    Class to generate a random password
    """

    def __init__(
        self,
        length: int = 8,
        include_numbers: bool = True,
        include_symbols: bool = True,
    ):
        if length < 8:
            print(f"length must be at least 8, so we will change {length} to 8")
            length = 8

        self.length: int = length

        self.groups: list[str] = [string.ascii_lowercase, string.ascii_uppercase]
        if include_numbers:
            self.groups.append(string.digits)
        if include_symbols:
            self.groups.append(string.punctuation)

        self.characters: str = "".join(self.groups)

    def generate(self):
        """
        Generate a password from specified characters.
        """
        chars = [secrets.choice(group) for group in self.groups]
        chars += [
            secrets.choice(self.characters) for _ in range(self.length - len(chars))
        ]
        secrets.SystemRandom().shuffle(chars)
        return "".join(chars)


class MemorablePasswordGenerator(PasswordGenerator):
    """
    Class to generate a memorable password
    """

    def __init__(
        self,
        num_of_words: int = 4,
        separator: str = "-",
        capitalization: bool = False,
        vocabulary: Optional[list[str]] = None,
    ):
        if num_of_words < 2:
            print(
                f"number of words must be at least 2, so we will change {num_of_words} to 2"
            )
            num_of_words = 2

        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()
        if not vocabulary:
            raise ValueError("vocabulary must not be empty")

        self.num_of_words: int = num_of_words
        self.separator: str = separator
        self.capitalization = capitalization
        self.vocabulary: list[str] = vocabulary

    def generate(self):
        """
        Generate a password from a list of vocabulary words.
        """
        password_words = [
            secrets.choice(self.vocabulary) for _ in range(self.num_of_words)
        ]
        if self.capitalization:
            password_words = [word.capitalize() for word in password_words]

        return self.separator.join(password_words)


class PinCodeGenerator(PasswordGenerator):
    """
    Class to generate a numeric pin code.
    """

    def __init__(self, length: int = 4):
        if length < 4:
            print(f"length must be at least 4, so we will change {length} to 4")
            length = 4
        self.length: int = length

    def generate(self) -> str:
        return "".join([secrets.choice(string.digits) for _ in range(self.length)])


def main():
    pcp = PinCodeGenerator(length=8)
    rpg = RandomPasswordGenerator(16, True, False)
    mpg = MemorablePasswordGenerator(3, "*", True)

    print(f"your pin code is : {pcp.generate()}")
    print(f"your random password is : {rpg.generate()}")
    print(f"your memorable password is : {mpg.generate()}")


if __name__ == "__main__":
    main()
