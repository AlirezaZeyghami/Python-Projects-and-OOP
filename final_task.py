from abc import ABC, abstractmethod
import requests


class Joke(ABC):
    def __init__(self, **kwargs):
        super().__init__()

    @abstractmethod
    def get_random_joke(self):
        pass


class A(Joke):
    def __init__(self, **kwargs):
        super().__init__()

    def get_random_joke(self):
        url = "https://manatee-jokes.p.rapidapi.com/manatees/random"
        headers = {
            "x-rapidapi-key":
            "a59fcabc31msh9a1a141ae9a9ffbp156d36jsn63b769645cc3",
            "x-rapidapi-host": "manatee-jokes.p.rapidapi.com"
        }
        response_manatee = requests.get(url, headers=headers)
        fun_one = response_manatee.json()
        return [fun_one[k] for k in ('setup', 'punchline')]


class B(Joke):
    def __init__(self, **kwargs):
        super().__init__()

    def get_random_joke(self):
        url = "https://jokeapi-v2.p.rapidapi.com/joke/Any"
        querystring = {"format": "json", "contains": "C%23", "idRange": "0-150",
                       "blacklistFlags": "nsfw,racist"}
        headers = {
            "x-rapidapi-key":
            "a59fcabc31msh9a1a141ae9a9ffbp156d36jsn63b769645cc3",
            "x-rapidapi-host": "jokeapi-v2.p.rapidapi.com"
        }
        response_joke = requests.get(url, headers=headers, params=querystring)
        fun_two = response_joke.json()
        return [fun_two[k] for k in ('setup', 'delivery')]


class C(Joke):
    def __init__(self, **kwargs):
        super().__init__()

    def get_random_joke(self):
        url = "https://dad-jokes7.p.rapidapi.com/dad-jokes/joke-of-the-day"
        headers = {
            "x-rapidapi-key":
            "a59fcabc31msh9a1a141ae9a9ffbp156d36jsn63b769645cc3",
            "x-rapidapi-host": "dad-jokes7.p.rapidapi.com"
        }
        response_dad = requests.get(url, headers=headers)
        fun_three = response_dad.json()
        return fun_three['joke']


if __name__ == "__main__":
    get_manatee_joke = A()
    joke_manatee = get_manatee_joke.get_random_joke()
    print(joke_manatee)

    get_joke = B()
    joke_joke = get_joke.get_random_joke()
    print(joke_joke)

    get_dad = C()
    joke_dad = get_dad.get_random_joke()
    print(joke_dad)
