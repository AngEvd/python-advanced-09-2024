def draw_cards(*args, **kwargs):
    monster_cards, spell_cards = [], []
    result = ""
    for arg in args:
        if arg[1] == "monster":
            monster_cards.append(arg[0])
        elif arg[1] == "spell":
            spell_cards.append(arg[0])

    for key, value in kwargs.items():
        if value == "monster":
            monster_cards.append(key)
        elif value == "spell":
            spell_cards.append(key)

    monster_cards.sort(reverse=True)
    spell_cards.sort()

    if monster_cards:
        result += "Monster cards:\n"
        for monster in monster_cards:
            result += f"  ***{monster}\n"

    if spell_cards:
        result += "Spell cards:\n"
        for spell in spell_cards:
            result += f"  $$${spell}\n"

    return result


print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))