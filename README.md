## Custom Labels Translator

###### With this python script you can create a '.csv' file of all the custom labels in your Salesforce Org, organized in dynamic columns based on the number of languages you want to translate into.

#### Prerequisites

- Visual Studio Code.
  
- SFDX Extension for VS Code.
  
- Python 3.8.5
  

#### Setting up

From Visual Studio Code, enter the following code in package.xml file:

```xml
<types>
   <members>*</members>
   <name>CustomLabels</name>
</types>
<types>
   <members>*</members>
   <name>Translations</name>
</types>
```

Save the file, right click on it and click on: *SFDX: Retrieve Source in Manifest from Org*.

Now you can see, in your project folder, the following folders with their files:

- labels
  
  - CustomLabels.labels-meta.xml
    
- translations
  
  - en_US.translations-meta.xml
    

#### Create .csv file with all custom labels

First of all, you've to download this script from this [link](https://github.com/NikCantelli/Salesforce/archive/refs/heads/main.ziphttps://github.com/NikCantelli/Salesforce/archive/refs/heads/main.zip). Extract the folder "Salesforce-main", then copy the file "**CustomLabels-meta.xml**" from your project folder to this folder.

Now, just run the scripts with this command:

```shell
python3 main.py 
```

And you will see something like this:

```textile
##########################################
######## Custom Labels Translator ########
##########################################
################ by: Nicola Cantelli #####

Choose which operation you want to perform:
[1] - Create ".csv" file from ".xml"
[2] - Create ".xml" files of translation from ".csv"
```

Now you've to choose an option, enter:

1. If you want to create a .csv file with all the custom labels of your project
  
2. If you want to create the appropriate .xml files of the translations
  

#### [1] - Create ".csv" file from ".xml"

If you choose this option you will see this:

```textile
Enter the file path or, if you're in the same folder, enter the name:
File name/path >> CustomLabels.labels-meta.xml
```

As you can see, you will be asked to enter the name of the file you want to parser, so, if the file is in the script folder, you've just to enter the name, otherwise you've to enter all the entire path of the file.

After this step, you will be asked for the number of languages in which you want to translate your custom labels:

```textile
How many languages ​​do you want to translate the labels into?
Enter the number >> 3
```

In this example, i chose 3, but you can choose any number you want.

```textile
Enter languages:
For example: ENGLISH -> EN
Enter abbreviation >> IT
Enter abbreviation >> ES
Enter abbreviation >> FR
```

After entering all the languages, as in the image above, you will see that this message will appear: *The file: "Labels.csv" was created successfully!* and the script will close.

You can see, that in the script folder a new file: "Labels.csv" was created and it should look like this:

At this point you just have to translate the custom labels with the appropriate language in the correct cell.

Now you're ready to convert your file into different file .xml to add into your project.

#### [2] - Create ".xml" files of translation from ".csv"

Once you have translated all the custom labels into the languages you need, you just have to convert the .csv file into different .xml files that you will add to the translations folder of your project.

So to do this, you need to re-run the script and enter option 2.

You will be asked to enter the name of the .csv file you wish to convert, and all you have to do is enter the file named "Labels.csv", in this way:

```textile
Enter the file name/path to read >> Labels.csv
```

After entering the name of the file you want to convert, this text will appear:

```textile
--- Processed 302 lines ---

The file: "it.translation-meta.xml" was created successfully.
The file: "es.translation-meta.xml" was created successfully.
The file: "fr.translation-meta.xml" was created successfully.
```

translation files in .xml, at this point you just have to copy them in the translations folder of your project and that's it.

Thanks for reading!
