Web scraper for the 42Matters platform


This web scraper is capable of querying the API of the 42Matters platform to retrieve metadata related to mobile apps. It is highly parameterized and allows the search of applications by platform (Android and/or iOS), keywords, categories, search field (only in an app’s name or both in an app’s name and its full-description), and by language.   

Python was the selected programming language because its easiness, its prowess, and because it integrates very easily with most databases (i.e., MongoDB), statistical suites (i.e., RStudio) and even with big data processing engines (i.e., Spark), making it an excellent option for Data Science projects.  
 
The web scraper is structured in the following five classes/modules:

1) main: This class, the principal one, is responsible for importing the main system libraries, as well as importing the other four classes of the web scraper: connection, utils, errors and csvExport. In addition, it retrieves the following search parameters (manually input) from the console: platform, keywords, search field, categories, token and language.

2) connection: Creates the HTTP Post call to the API of 42Matters, imports the library errors, uses the previously manually input parameters, and iteratively fetches the pages returned by the API until the query is completed. 

3) utils: This class allows extracting the selected metadata.

4) errors: As its name indicates, this class handles all the possible errors derived from querying the API of 42Matters (inaccessibility of the server, invalidity of the token, maximum allowed request rate exceeded, etc.).

5) csvExport: It stores the results in a CSV file so that they can be easily viewed, analyzed and manipulated by users without a computer-science background.  


Last but not least, I would like to mention that this web scraper is released under the GNU AGPLv3 license.
