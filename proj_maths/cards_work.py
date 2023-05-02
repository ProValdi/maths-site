def get_cards_for_table():
    cards = []
    print("initiate read file")
    with open("./static/cards.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            cnt, source, target = line.split(";")
            cards.append([cnt, source, target])
            print("{} {} {}".format(cnt, source, target))
    return cards


def write_card(new_source, new_target) -> int:
    with open("./static/cards.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]

    for terms in old_terms:
        cnt, source, target = terms.split(";")
        if source == new_source or target == new_target:
            return 1

    new_term_line = f"{len(old_terms)+1};{new_source};{new_target}"
    terms_sorted = old_terms + [new_term_line]
    new_terms = [title] + terms_sorted
    with open("./static/cards.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_terms))

    return 0
