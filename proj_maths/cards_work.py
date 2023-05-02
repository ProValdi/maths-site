
def get_cards_for_table():
    cards = []
    print("initiate read file")
    with open("./static/cards.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            cnt, source, target, learned = line.split(";")
            cards.append([cnt, source, target, learned[:-1]])
            print("{} {} {} {}".format(cnt, source, target, learned[:-1]))
    return cards

def modify_card(index, value):
    print("here")
    with open("./static/cards.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        terms = existing_terms[1:]

        terms_sorted = ["" for x in range(len(terms) + 1)]

        for item in terms:
            print(item)
            cnt, source, target, learned = item.split(";")
            cnt = int(cnt)
            print("{}==={}".format(cnt, index))

            if cnt == int(index):
                print("HERE")
                terms_sorted[cnt] = '{};{};{};{}'.format(cnt, source, target, value)
            else:
                terms_sorted[cnt] = item
                print(terms_sorted)

        print(terms_sorted)

        terms_sorted[0] = title

        print(terms_sorted)
        with open("./static/cards.csv", "w", encoding="utf-8") as f:
            f.write("\n".join(terms_sorted))


def write_card(new_source, new_target) -> int:
    with open("./static/cards.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]

    for terms in old_terms:
        cnt, source, target, learned = terms.split(";")
        if source == new_source or target == new_target:
            return 1

    new_term_line = f"{len(old_terms)+1};{new_source};{new_target};0"
    terms_sorted = old_terms + [new_term_line]
    new_terms = [title] + terms_sorted
    with open("./static/cards.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_terms))

    return 0
