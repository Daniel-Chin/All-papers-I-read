import index
import tags

def main():
    filter = input('filter=')
    tag = tags.__getattribute__(filter)
    for p in index.__dict__.values():
        try:
            if tag not in p.tags:
                continue
        except AttributeError:
            continue
        print(p.bib)
        print()

main()
