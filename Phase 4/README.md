# **README**

## **Interface**:
* First enter the username and password of your mysql user where the database was dumped.
* Select what type of user you are (as is specified by the list that shows up)
* Enter your choice from the list (denoted by the letter inside brackets).
* After choosing which user you are, another list should show up describing all applications permitted for your user.
* Pick one and enter the choice (denoted by the 1-3 letter code in brackets).
* After you are done with the particular user, you can enter L (when the code asks you to choose a query) to logout and change user.
* After you are done with the program, logout of whatever user you are in and type E to exit (where the code asks for user choice).

## **Commands you can run**:

- #### **Get all space agencies participating in a mission**
    - Prints the names of all the space agencies participating in the mission
- #### **All rockets developed by space agency 1 that have taken space agency 2 payload to the moon**
    - Lists rocket model name,the space agency it belongs to and the country of the space agency
- #### **Get space missions which can support payloads more than N kgs**
    - Lists all the mission names which have current available payload capacity greater than N kgs
- #### **Find all missions that a space agency sent to a celestial body**
    - Lists all the missions names which a space agency participated in which was sent to that celestial body
- #### **Get the success ratio of a particular space agency**
    - Gets the ratio of the successful missions to the total number of missions the space agency participated in
- #### **Get the space agency with the maximum success rate**
    - Gets the agency name and agency country with the maximum success ratio
- #### **Most fuel efficient rocket**
    - Gets the rocket name with the highest fuel efficiency
- #### **Astronaut that has completed the most missions**
    - Gets the astronaut ID and the name 
- #### **Average fuel efficiency of all rockets from a space agency**
    - May be used by UNEP to enforce environmental policies
- #### **Inserting an entry for a mission**
    - Adding a mission, creating a new mission
- #### **Add a space agency and their associated representative**
    - Create a space agency and assign an ambassador for it
- #### **Updating the rocket the payload goes on**
    - Changing the rocket used to send the payload
- #### **A space agency adding resources for a mission**
    - 
- #### **Update the government ambassador for a country**
    - Change the governement ambassador for a country
- #### **Deleting an entry of a planned mission which was scrapped**
- #### **Deleting a rocket if its development is canceled**
- #### **Get a report of all external materials and products acquired for a mission by a space agency, to maybe detect illegal mission payloads( space weapons)**
    - lists all resources acquired and payloads related to a mission
- #### **Number of rockets developed by space agency that are reusable and have completed at least N missions**
    - N is user input
- #### **Partially searching for the purpose of a mission (like mission related to humans being sent to space, or planetary exploration with probes, …etc)**
- #### **Partially search for a payload by experiment name, example: Search for zero gravity** 
