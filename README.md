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

First of all, you've to download this script from this [link](https://github.com/NikCantelli/Salesforce/archive/refs/heads/main.ziphttps://github.com/NikCantelli/Salesforce/archive/refs/heads/main.zip). Extract the folder "Salesforce-main", then copy the file "**CustomLabels.labels-meta.xml**" from your project folder to this folder.

Now, just run the scripts with this command:

```shell
python3 main.py 
```

And you will see something like this:

![](C:\Users\cantellini\Desktop\Start.JPG)

Now you've to choose an option, enter:

1) If you want to create a .csv file with all the custom labels of your project

2) If you want to create the appropriate .xml files of the translations

#### [1] - Create ".csv" file from ".xml"

If you choose this option you will see this:

![](C:\Users\cantellini\AppData\Roaming\marktext\images\2021-06-21-19-25-58-image.png)

As you can see, you will be asked to enter the name of the file you want to parser, so, if the file is in the script folder, you've just to enter the name, otherwise you've to enter all the entire path of the file.

After this step, you will be asked for the number of languages in which you want to translate your custom labels:

![](C:\Users\cantellini\AppData\Roaming\marktext\images\2021-06-21-19-29-49-image.png)

In this example, i chose 3, but you can choose any number you want.

![](C:\Users\cantellini\AppData\Roaming\marktext\images\2021-06-21-19-31-22-image.png)

After entering all the languages, as in the image above, you will see that this message will appear: *The file: "Labels.csv" was created successfully!* and the script will close.

You can see, that in the script folder a new file: "Labels.csv" was created and it should look like this:

![](https://github.com/NikCantelli/Salesforce/blob/main/CSV-Example.png)

At this point you just have to translate the custom labels with the appropriate language in the correct cell.

Now you're ready to convert your file into different file .xml to add into your project.

#### [2] - Create ".xml" files of translation from ".csv"

Once you have translated all the custom labels into the languages you need, you just have to convert the .csv file into different .xml files that you will add to the translations folder of your project.

So to do this, you need to re-run the script and enter option 2.



You will be asked to enter the name of the .csv file you wish to convert, and all you have to do is enter the file named "Labels.csv", in this way:

![](C:\Users\cantellini\AppData\Roaming\marktext\images\2021-06-21-19-48-20-image.png)

After entering the name of the file you want to convert, this screen will appear:

![](C:\Users\cantellini\AppData\Roaming\marktext\images\2021-06-21-19-48-51-image.png)

A new folder has been created, named **"Translations"** where you will find all the translation files in .xml, at this point you just have to copy them in the translations folder of your project and that's it.

Thanks for reading!
