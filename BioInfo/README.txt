BioInfo API

A simple API end point that retrieves the data from an ElasticSearch index

## Table of Contents

[Project Description] (#project-description)
[Getting Started] (#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)


## Project Description
BioInfo API is a small application designed to leverage the "dgnplus_gene_disease_assoc_summary_janet" Elasticsearch Index.
to deliver essential functionalities. These functionalities include:

#Listing Relevant Data:

It accesses the index and retrieves specific fields:
"gene_symbol," represented as "geneSymbol_text" in the index.
"disease_name," identified as "diseaseName" in the index.
"score," which is presented as a normalised numeric range (0–1) with the same name in the index.

#Data Export in CSV Format:

It unables the user to download the data in CSV format.
Our application caters to users who prefer data in a tabular format.

Filtering by Score:

It provides the ability to filter data based on the "score" field.




## Getting Started

Getting Started with the Project:

Step 1 (optional):
To begin, activate your virtual environment using the following command:

your_virtual_environment_name/bin/activate

Step 2:
Install the project's dependencies by running:

pip install -r requirements.txt

Step 3:
Navigate to the "BioInfo" directory and launch your local server with the command:

python manage.py runserver

Note: If you intend to run the programme on a live server, make sure to add the server's IP address to the allowed hosts list in the "settings.py" file. For detailed instructions, refer to the official documentation: Django Official Documentation.

Step 4:
Once your server is up and running, you will be presented with three main options:
Download CSV: Obtain the data in CSV format.
- Download JSON data: Access the data in JSON format.
View Available Routes: Explore the various API endpoints and routes.

This streamlined process will help you quickly set up and navigate through the project.

 
### Prerequisites
Python == 3.x.x
Django==4.2.5
djangorestframework==3.14.0
djangorestframework-csv==2.1.1
elastic-transport==8.4.0
elasticsearch==8.9.0
elasticsearch-dsl==7.4.1


