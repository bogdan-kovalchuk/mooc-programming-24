def load_recipes(filename: str) -> list:
    with open(filename) as f:
        return [r.splitlines() for r in f.read().split("\n\n") if r.strip()]


def search_by_name(filename: str, word: str) -> list:
    recipes = load_recipes(filename)
    return [recipe[0] for recipe in recipes if word.lower() in recipe[0].lower()]


def search_by_time(filename: str, prep_time: int) -> list:
    recipes = load_recipes(filename)
    return [
        f"{recipe[0]}, preparation time {recipe[1]} min"
        for recipe in recipes
        if prep_time >= int(recipe[1])
    ]


def search_by_ingredient(filename: str, ingredient: str) -> list:
    recipes = load_recipes(filename)
    return [
        f"{recipe[0]}, preparation time {recipe[1]} min"
        for recipe in recipes
        if ingredient in recipe[2:]
    ]
