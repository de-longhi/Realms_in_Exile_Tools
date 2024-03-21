# Realms_in_Exile_Tools
This repository has the purpose of serving as a universal place for all the small tools I write for my mate @Jaco-Daan who is working on the Realms in Exile mod for the Steam game: Crusader Kings 3. 

filter.py: This script has the purpose of filtering through history texts and filtering for certain attributes. The script is written to have a resemblance to a deterministic finite automata for seamless integration and it uses regular expressions for filtering. It has a linear order of growth to the amount of characters in the history file.

Note for filter.py: As of now, much of the functionality that the script should have isn't there. The reason for this is that there isn't a big need for this functionality. The primary purpose of the script at the moment is to filter for "add_trait_xp: trait = blood_of_numenor" and the script isn't optimized for anything different. For queries or requests for extra functionality, you may email me. 