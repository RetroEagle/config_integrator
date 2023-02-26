import toml

# TODO
# load all values
# overwrite changed values
# store changed values in old file
# "diff" file format that stores the differences of multiple files in file.rec_category.var format
# e.g. "skyblock.diff" all configs changed from default for a skyblock pack

def parse(filename):
    f = open(filename, "r")
    return toml.loads(f.read())

def main():
    config = parse("general.toml")
    # for i in config:
    #     for j in config:
    #         print(j)
    for i in config.items():
        for j in i.items():
            print(j)
        # print(i)
        # print()


if __name__ == "__main__":
    main()
