def read_process_csv(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        data = [line.strip().split(',') for line in in_file]
    return data


def count_champions(data):
    champions = {}
    for record in data:
        name = record[1]
        champions[name] = champions.get(name, 0) + 1
    return champions


def extract_countries(data):
    countries = {record[2] for record in data}
    return countries


def main(filename):
    data = read_process_csv(filename)
    champions = count_champions(data)
    countries = extract_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

    sorted_countries = sorted(list(countries))
    countries_str = ', '.join(sorted_countries)
    print(f"\nThese {len(sorted_countries)} countries have won Wimbledon:\n{countries_str}")
