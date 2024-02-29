from sympy import quo
from tqdm import tqdm

from index import allPapers

def main():
    with open('refactored.py', 'w', encoding='utf-8') as f:
        def p(*a, **kw):
            print(*a, **kw, file=f)
        for key, value in tqdm(allPapers()):
            for k in value.__dict__.keys():
                k: str
                if k.startswith('__'):
                    continue
                if k in ['apa', 'bib', 'short', 'abstract', 'tags', 'my_notes']:
                    continue

            def extract(key_: str):
                try:
                    return getattr(value, key_)
                except AttributeError:
                    return None
            
            def write(
                key_: str, quotes: str = "'''", 
                quote_prefix: str = '', 
                verbose_none: bool = False, 
            ):
                value = extract(key_)
                if value is None:
                    if not verbose_none:
                        return
                    v = 'None'
                else:
                    v = quote_prefix + quotes + value + quotes
                p(' ' * 4, f'{key_} = ', v, ', ', sep='')
            
            p(key, '= Paper(')

            shorts = extract('short')
            if shorts is None:
                shorts = []
            if isinstance(shorts, str):
                shorts = [shorts]
            else:
                shorts = list(shorts)
            if shorts:
                p(' ' * 4, f'shorts = {repr(shorts)}, ', sep='')

            write('apa', quote_prefix='r', verbose_none=True)

            write('bib', quote_prefix='r', verbose_none=True)

            write('abstract', verbose_none=True)

            raw_tags = extract('tags')
            if raw_tags is None:
                raw_tags = []
            tags = []
            for tag in raw_tags:
                tags.append(tag.__name__)
            tags = ', '.join(tags)
            p(' ' * 4, f'tags = [{tags}], ', sep='')

            write('my_notes', quote_prefix='r')

            p(')')
            p()

if __name__ == "__main__":
    main()
