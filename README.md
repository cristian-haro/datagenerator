# Datagenerator
### Languages
![Python.](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue "Python.")

>This Python script is a tool to generate dummy data for testing, simulation, or prototyping. Users can customize the type of data they want to generate (e.g. names, addresses, dates, etc.) and the number of records. It also allows users to save this generated data to a CSV file for later use.

## Requirements:

The script requires the following libraries to work correctly:

- Faker: To generate realistic random data such as names, addresses, emails, etc..
- pandas: To manage and manipulate the generated data, and save this data in a CSV file.
- tkcalendar: To select dates visually through an interactive calendar.
- tkinter: To create the graphical user interface (GUI) that allows you to interact with the script.

If you don't have these libraries installed, you can install them using pip::

`pip install -r requirements.txt`

Where the requirements.txt file contains the following dependencies:

- Faker
- pandas
- tkcalendar

## Main Features:
**1.	Generation of Custom Data**: The script allows users to choose what types of data they want to generate for each column, including:

- Names (first, last)
- Emails
- Addresses
- Dates (specific range)
- Numbers (specific range)
- And more...

**2.	Graphical User Interface (GUI)**: The script has a simple interface developed with tkinter. This interface allows users to:

- Define the number of records to generate.
- Specify the name of the output file (in .csv format).
- Add and customize columns with different data types (number, string, date).
- Set column properties (for example, the value range for numbers or the string pattern).

**3.	Save to CSV**: The generated data can be saved to a CSV file with a single click, making it easy to use later for testing or analysis..

## How It Works
**1.	Initial Configuration**: The script starts by displaying the main window, where the user can enter the number of records to generate and the name of the output file. Additionally, the user can add new custom columns.

**2.	Add Columns**: Clicking on "Add Column" opens a window where the user can define:

- The name of the column.
- The type of data it should contain (number, string, or date).
- If "number" is selected, the minimum and maximum values for the range are requested.
- If "date" is selected, the start and end dates are requested.
- If "string" is selected, a pattern for the string is requested (for example, a username or email address).

**3.	Data Generation**: Once the user has defined all the columns, he can click on "Generate Data". The script generates the records according to the selected settings.

**4.	Save CSV File**: The generated data is saved to the specified CSV file, and a success message is displayed once the process is complete.

## Example of Use
Imagine you want to generate 100 records with the following columns:

- Name
- Email
- Date of Birth
    
1.  Start the script and set that you want to generate 100 records.
2.	Add the columns:
- Name: Select the "string" type.
- Email: Select the "string" type.
- Date of Birth: Select the "date" type and define the date range between 1990-01-01 and 2005-12-31.
3.	Click "Generate Data" and then "Save" to create the CSV file.

The generated file will have 100 rows with dummy data for the selected columns.

## Installation and Execution
1.	Install dependencies: If you don't have the required dependencies yet, you can install them with:
	
`pip install -r requirements.txt`

2.	Run the script: If you have Python installed on your system, simply run the script from the terminal or command line:

`python generador_datos.py`

This will open the graphical user interface (GUI), where you can configure the data generator and generate the CSV file.
