# Balzac Character Network
This is a network graph showing the top 50 recurring characters in Balzac's *La Comedie Humaine* by novel appearances, created using Pyvis. 


## View the Graph
[Click here to open the graph](https://suzcubed.github.io/balzacnetwork/balzac_character_network_with_filters.html)

## How to Use
- **Click character or novel nodes** to easily see their connections.
- **Drag character or novel nodes** to reposition them and pull out their connections.
- **Zoom in on nodes and connections** using your mouse wheel.
- **Select Filters** to narrow down the graph: selecting character or novel highlights all connections to the selected node.
- **Filter the Network** by node type:
    - Character: shows all characters in the graph. Select a novel in the top menu to highlight which characters are         present.
    - Novel: shows all novels in the graph. Select a character in the top menu to highlight which novels they appear in.     Select a "Scene" to see which novels are considered part of that scene in *La Comedie Humaine.*
- **Filter by novel/character connections**:
    -   *"From character":* select 1 or more characters to see all their novel appearances and which novels they appear in     together.
    -   *"To novel":* select 1 or more novels to see which characters are present and which characters overlap.
-   **Reset filters** by clicking the reset filters button.


## Understanding the Data 
Character mentions were retrieved through a trained spaCy NER model. Raw references were verified against novel text and used to update patterns to include all aliases and character titles in the final graph. 

The graph captures any mention of a character in a novel, whether they actually appear or not. This was an intentional decision to ensure the graph captured characters' relative influence across *La Comedie Humaine*.
- Connection lines between characters and novels are weighted based on the frequency of the character's appearance in the novel. A thinner line denotes minor mentions (e.g., a single appearance at a party or a reference such as "a Nucingen" indicating a wealthy figure), while thicker lines indicate increasing centrality.
- Character nodes are scaled based on character occurrence counts across the corpus.
- Novel nodes are scaled based on the number of characters who appear.

## Planned Updates 
Adding metadata to character tool tips & the ability to filter by character attributes (gender, class, occupation). 
Adding the ability to filter characters by number of appearances. 

## Future Updates
Data cleaning, pattern design, and reference extractions of the next batch of 50 characters.

## Sources
All texts sourced from Project Gutenberg
Character aliases and titles validated with:
Cerfberr, and Christophe (1902): *Repertory of the Comedie Humaine.*

 
