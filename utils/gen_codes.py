with open("codes.txt", "r") as f:
    for line in f.readlines():
        value = line.strip()
        code, name = value.split(" ", 1)
        ugly_name = name.replace("-", "_").replace(" ", "_").upper()
        ugly_name += f"_{code}"
        pretty_name = name.title().replace("-", "").replace(" ", "")
        ugly_entry = f'{ugly_name} = "{value}"'
        pretty_entry = f'{pretty_name} = {ugly_name}'
        print(ugly_entry)
        print(pretty_entry)
        print()
