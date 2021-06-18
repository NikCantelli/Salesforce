import csv

class Converter:
    customLabels = [] # Array of dictionary of labels
    languages = [] # Array of languages of labels to translate
    def __init__(self):
        return

    def setCustomLabels(self, customLabels):
        self.customLabels = customLabels
    
    def getCustomLabels(self):
        return self.customLabels

    def setLanguages(self, languages):
        self.languages = languages
    
    def getLanguages(self):
        return self.languages

    def readXML(self, filePath):
        fullNames = [] #Array of Custom Labels API Name
        values = [] #Array of Custom Labels values
        customLabels = self.getCustomLabels()
        startFullName = "<fullName>"
        endFullName = "</fullName>"
        startValue = "<value>"
        endValue = "</value>"
        fIn = open(filePath)
        for line in fIn:
            line = line.strip()
            if line.startswith(startFullName):
                line = line.replace(startFullName, "")
                line = line.replace(endFullName, "")
                fullName = line
                fullNames.append(fullName)
            if line.startswith(startValue):
                line = line.replace(startValue, "")
                line = line.replace(endValue, "")
                value = line
                values.append(value)

        sizeFN = len(fullNames)
        sizeV = len(values)

        if sizeFN == sizeV:
            for i in range(sizeFN):
                label = {
                    "fullName" : fullNames[i],
                    "value" : values[i]
                }
                customLabels.append(label)
        self.setCustomLabels(customLabels)

    def chooseLanguages(self):
        languages = self.getLanguages()
        print("How many languages ​​do you want to translate the labels into?")
        nLang = input("Enter the number >> ")
        print("Enter languages:\nFor example: ENGLISH -> EN")
        for lan in range(int(nLang)):
            lan = input("Enter abbreviation >> ")
            languages.append(lan)
        self.setLanguages(languages)

    def createCSV(self):
        self.chooseLanguages()
        languages = self.getLanguages()
        customLabels = self.getCustomLabels()
        with open("Labels.csv", mode="w") as csv_file:
            header = ["API Name", "EN"]
            for lan in languages:
                header.append(lan)
            writer = csv.DictWriter(csv_file, fieldnames=header)
            writer.writeheader()
            for label in customLabels:
                item = {
                    "API Name" : label["fullName"],
                    "EN" : label["value"],
                }
                for lan in languages:
                    item.update({
                        lan : ""
                    })
                writer.writerow(item)
            if csv_file:
                print("\nThe file: \"Labels.csv\" was created successfully!")
            else:
                print("\nSorry, something went wrong\nPlease, try again")

    def convert(self):
        print("\nEnter the file path or, if you're in the same folder, enter the name:")
        filePath = input("File name/path >> ")
        self.readXML(filePath)
        self.createCSV()





    

