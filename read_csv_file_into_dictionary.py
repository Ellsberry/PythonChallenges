import csv

def read_csv_into_dictionary(file):
    print("read csv file program line 4  ",file)
    dictionary = {}
    try:
        with open(file, newline="") as dictfile:
            reader = csv.reader(dictfile)
            next(reader, None)              # skip the header row
            dictionary = dict(reader)     # pull in each row as a key_value pair
            good_dictionary = True
    except Exception as e:
        print(str(e))
        good_dictionary = False
    return dictionary, good_dictionary


if __name__ == "__main__":
    dictionary, good_result = read_csv_into_dictionary("HTML Tags and Descriiptions.csv")
    if good_result:
        for key, value in dictionary.items():
            print("{:<15} {:<65}".format(key, value))


