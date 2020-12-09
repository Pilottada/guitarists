#This is the README file for the Pillotada Project of Software project development
--------------------------------------------------------------------------------
I honestly don't know if i'm doing well, but nevermind, i'll try to do it anyway 

let's go! 

The aim of the project is to create a database containing all the most famous guitarists associated with their respective bands.  
Once the name of a guitarist (e.g. Brian May) has been entered as input, the program controls if the name of the guitarist or of the band is already present in the dataset. 
if it is not, the progranm will kindly ask you if you wanna add the couple (guitarist + band).

On the other hand, if the name is already present (input ex. "Brian May"), the "get_band" function will return the name of the character's respective band. (Queen in this case).
Of course, it also works the other way around. (entering the band name, it will return the guitarist's name of that band) 

To increase the speed of interaction, the user can access the shortcut -a.
This command allows you to skip a step and add a new component or band name directly to the database by simply writing the -a keyword next to the new name to add.

ex. --> John -a .

The program will then ask the user to specify whether the name entered concerns a band or the guitarist. When you reach this point, to add a guitarist the input command is -g, for a band -b.

The functions `guitarists.py`, `get_guitarist`and `get_band` are all stored in the `main.py` file.

 If you run the program, executing the main file with: ```python main.py``` it will give you the following results:

```
Kirk Hammet plays for Metallica
Sorry, Young Signorino does not seem to be a known guitarist
The guitar hero of Guns'n Roses is Slash
Sorry, we don't know who is the guitar hero of Ricchi e Poveri
```
To do so, we preferred storing the guitarists' and band's names into a csv file in order to keep it neat and tidy. 

