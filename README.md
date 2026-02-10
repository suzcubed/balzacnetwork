# Balzac Character Network
This is a network graph showing the top 50 recurring characters in Balzac's *La Comedie Humaine* by novel appearances, created using Pyvis. 


## View the Graph
[Click here to open the graph](https://suzcubed.github.io/balzacnetwork/balzac_character_network_with_filters.html)

# 01 - How to Use
- Click character or novel nodes to see their connections.  
- Drag nodes to reposition them and pull out their links.  
- Zoom with your mouse wheel.

### Filters
- Select **Filters** to narrow the graph: choosing a character or novel highlights all its connections.
- Select a novel in the top menu to highlight the characters who appear in it.

### Filter by Node Type
- **Character:** shows all characters. *UPDATE 02-09-26* - Added gender and social class character filters. 
- **Novel:** shows all novels. Select a character in the top menu to highlight their novels. Select **Novels by Scene from *La Comedie Humaine*** to see which novels belong to each scene in *La Comédie Humaine.*

### Filter by Novel/Character Connections
- **From character:** choose one or more characters to see all their novel appearances and overlaps.  
- **To novel:** choose one or more novels to see which characters appear and overlap.

- Reset filters with the reset button.

### Finding Character Co-occurrences
- **Option 1:** Select *Filter by novel/character connections*, choose 2+ characters, then drag novel nodes to reveal overlaps.  
- **Option 2:** Select the same filter, pick a character, then choose a second character in the top menu; highlighted novels show where both appear.

# 02 - Understanding the Data 
Character mentions were retrieved through a trained spaCy NER model. Raw references were verified against the novel text and used to update patterns to include all aliases and character titles. This ensured all references to each character were counted in the final graph.

The graph captures **any** mention of a character in a novel, whether they actually appear or not. This was an intentional decision to ensure the graph captured characters' relative influence across *La Comedie Humaine*.
- Connection lines between characters and novels are weighted based on the frequency of the character's appearance in the novel. A thinner line denotes minor mentions (e.g., a single appearance at a party or a reference such as "a Nucingen" indicating a wealthy figure), while thicker lines indicate increasing centrality. Zoom in to better see line weights.
- Character nodes are scaled based on character occurrence counts across the corpus.
- Novel nodes are scaled based on the number of characters who appear.

### Methodological Notes and Entity Matching

Designing the variant names required both pattern design and a bit of research. Balzac is remarkably consistent in referring to characters: nobles are almost always cited by their titles and last name (e.g., Comtesse de Montcornet, Madame/Mme de Montcornet). Regular expressions handled the common patterns, but they did not capture earlier names and titles, aliases, or marital name changes (e.g., Madame de Montcornet was previously Mlle. Virginie de Troisville and later Madame Blondet). 

To capture these, I relied on Cerfberr and Christophe’s *Repertory of the Comédie Humaine*, which provided maiden names and aliases for building a variant dictionary. Each variant name was labeled “PERSON” in spaCy’s entity ruler, and a supplementary fuzzy name dictionary was created to catch close variations (e.g., “Felix” or “Vandanesse” for “Felix de Vandanesse”).

With the entity ruler in place, exact matches for 50 central characters were extracted across all novels. Rapidfuzz was then used to identify near matches. Each captured match was manually verified against the text to ensure accuracy—a feasible process given Balzac’s consistent naming and the small set of characters.

### Reflection on Findings

One way to explore the network is through key figures like Lucien de Rubempré and Eugène de Rastignac. From a purely data-driven perspective, these characters are mentioned most often and appear as our largest nodes. Both had similar starting points: modest wealth but supportive families and tenuous ties to the *monde brillante.* 

We can visually trace their trajectories. Lucien rises and then falls, and we see his central prominence in the *Lost Illusions* works taper off into minor mentions in other works (thin lines). Meanwhile Rastignac steadily ascends, and we see his prominence throughout the corpus through gradations of line thickness. The goal of entity mapping was to create a foundation for exploring character recurrence and create reading pathways to track these sorts of rises and falls. 

## Sources
All texts sourced from Project Gutenberg
Character aliases and titles validated with:
Cerfberr, and Christophe (1902): *Repertory of the Comedie Humaine.*


## 02-09-26 - UPDATES
- Updated graph HTML:
  - Added gender and social class data and filters
  - Added character descriptions as hover-over tooltips
- Added CSV with character metadata
- Updated CSV of nodes for the pyvis graph


## Planned Updates
- Add filters for characters by number of appearances.
- Continue data cleaning, pattern design, and reference extraction for the next batch of 50 characters.


 
