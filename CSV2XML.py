import csv
import os

class Inverter:
    customLabelsTranslated = [] # Array of all labels translated
    languages = [] # Array of languages of labels translated

    def setLanguages(self, languages):
        self.languages = languages
    
    def getLanguages(self):
        return self.languages

    def setLabels(self, customLabelsTranslated):
        self.customLabelsTranslated = customLabelsTranslated
    
    def getLabels(self):
        return self.customLabelsTranslated

    def readFromCSV(self):
        customLabelsTranslated = self.getLabels()
        with open('Labels.csv', 'r') as csv_file:
            header = []
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    h = {", ".join(row)}
                    header = h.pop()
                    header = header.split(", ")
                    line_count += 1
                    del header[0]
                translations = []
                for lan in header:
                    language = row[lan]
                    translations.append(language)
                label = {
                    "API Name" : row["API Name"],
                    "Translations" : translations
                }
                customLabelsTranslated.append(label)
                line_count += 1
            self.setLanguages(header)
            self.setLabels(customLabelsTranslated)
            print(f'--- Processed {line_count} lines ---\n')
            
    def createFiles(self):
        languages = self.getLanguages()
        del languages[0]
        labels = self.getLabels()
        sizeLan = len(languages)
        dirName = "Translations/"
        if not os.path.exists(dirName):
            os.makedirs(dirName)
            print("Directory " , dirName ,  " Created.")
        for lan in range(sizeLan):
            fName = dirName+languages[lan]+"-Labels.xml"
            fileOut = open(fName, "w")
            for lab in labels:
                standardString = "<customLabels>\n\t<label>labelTranslated</label>\n\t<name>apiName</name>\n</customLabels>\n"
                apiName = lab["API Name"]
                value = lab["Translations"][lan]
                standardString = standardString.replace("labelTranslated", value)
                standardString = standardString.replace("apiName", apiName)
                fileOut.write(standardString)
            fileOut.close()
            if os.stat(fName).st_size != 0:
                print("The file: \""+languages[lan]+"-Labels.xml\" was created successfully.")
            else:
                print("\nSorry, something went wrong\nPlease, try again")

    def invert(self):
        self.readFromCSV()
        self.createFiles()
        
        