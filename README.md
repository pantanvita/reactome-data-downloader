# **Day 06 assignment**

## **About REACTOME [https://reactome.org/]**
![reactome-logo](reactome-logo.png)

* Reactome is an open-source, open access, manually curated and peer-reviewed pathway database.
* Further details about Reactome, project inspiration, project structure in version 1.0, what was done previously etc. can be viewed on [Day-04-README](https://github.com/pantanvita/wis-python-2025/blob/main/day04/README-day-04.md)



# **REACTOME DATA DOWNLOADER v2.0**

The REACTOME DATA DOWNLOADER v2.0 is an upgrade over its previous version 1.0

## **Upgrades in version 2.0**

**Features added**

* Version 2.0 can now also download .pdf and .png files of the pathway ID entered by the user in addition to the .json file
* This provides further details about the pathway and sub-pathways involved in a more readble format (pdf) and with diagramtic representation (png).

## **Bugs fixed from previous version**

* My reviewer in Day04 assignment Shoshana Sernik @shoshisernik had pointed out that she could not store her email in a separate config file for API calls.
* Liron Hoffman @liroh99 had suggested to remove the config.json file from .gitignore
* Following her suggestion, I removed the config.json file from .gitignore
* The users can now view it when cloning this repository and add their email address for API calls.


## **Project Structure**

reactome_downloader/

├── main.py              # User Interface (CLI)

├── reactome_service.py  # Business logic

├── config.json          # User email / API key

├── .gitignore


## **How the code works**

1. User can edit the config.json file and provide their email address.
2. User must also provide their email address when prompted.
3. User then provides the Reactome Stable Identifier (e.g. R-HSA-199420).
4. The program fetches the files from Reactome’s Content Service API or download server.
5. The program creates a new parent folder on the user's desktop- "Reactome_Downloads" with folders for each Reactome Stable Identifier 
6. This is followed by sub-folders for .json, .pdf and .png files.

# Dependencies required
Python version = 3.8.2
Package = requests
