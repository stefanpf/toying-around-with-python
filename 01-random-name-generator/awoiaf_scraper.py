import bs4
import requests


def scrape_names():
    res = requests.get('https://awoiaf.westeros.org/index.php/List_of_characters')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    name_tags = soup.select("div.mw-parser-output > ul > li > a")
    names = [name_tag.getText() for name_tag in name_tags]
    return names


def clean_up_names(list_of_names):
    first_names = []
    last_names = []
    for name in list_of_names:
        name = name.split()
        first_names.append(name[0])
        if len(name) > 1:
            last_name = ' '.join(name[1:])
            last_names.append(last_name)
    return first_names, last_names


def deduplicate_names(list_of_names):
    unique_names = list(set(list_of_names))
    return unique_names


def save_names(list_of_names, filename='test'):
    file = open(f'{filename}.txt', 'w')
    for name in list_of_names:
        file.write(str(name) + '\n')
    file.close()


def main():
    scraped_names = scrape_names()
    cleaned_names = clean_up_names(scraped_names)
    unique_first_names = deduplicate_names(cleaned_names[0])
    unique_last_names = deduplicate_names(cleaned_names[1])
    save_names(unique_first_names, filename='asoiaf_first_names')
    save_names(unique_last_names, filename='asoiaf_last_names')


if __name__ == '__main__':
    main()
