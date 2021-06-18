from CSV2XML import Inverter
from XML2CSV import Converter   
import os

def main():
    print("##########################################")
    print("######## Custom Labels Translator ########")
    print("##########################################")
    print("################ by: Nicola Cantelli #####")

    print("\nChoose which operation you want to perform:")
    print("[1] - Create \".csv\" file from \".xml\" file")
    print("[2] - Create \".xml\" files of translation from \".csv\" file")
    x = input("\nEnter value >> ")
    x = int(x)
    if x == 1:
        c = Converter()
        c.convert()
    elif x == 2:
        i = Inverter()
        i.invert()
    else:
        os.system("clear")
        print("Invalid Input!\n")
        main()



if __name__ == "__main__":
    main()
