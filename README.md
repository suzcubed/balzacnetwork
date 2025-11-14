# Balzac Character Network
This is a network graph showing the top 50 recurring characters in Balzac's *La Comedie Humaine* by novel appearances, created using Pyvis. 


## View the Graph
[Click here to open the graph](https://suzcubed.github.io/balzacnetwork/balzac_character_network_with_filters.html)

## How to Use
- Click character or novel nodes to see their connections.  
- Drag nodes to reposition them and pull out their links.  
- Zoom with your mouse wheel.

### Filters
- Select **Filters** to narrow the graph: choosing a character or novel highlights all its connections.

### Filter by Node Type
- **Character:** shows all characters. Select a novel in the top menu to highlight who appears in it.  
- **Novel:** shows all novels. Select a character in the top menu to highlight their novels. Select **Novels by Scene from *La Comedie Humaine*** to see which novels belong to each scene in *La Comédie Humaine.*

### Filter by Novel/Character Connections
- **From character:** choose one or more characters to see all their novel appearances and overlaps.  
- **To novel:** choose one or more novels to see which characters appear and overlap.

- Reset filters with the reset button.

### Finding Co-occurrences
- **Option 1:** Select *Filter by novel/character connections*, choose 2+ characters, then drag novel nodes to reveal overlaps.  
- **Option 2:** Select the same filter, pick a character, then choose a second character in the top menu; highlighted novels show where both appear.

## Understanding the Data 
Character mentions were retrieved through a trained spaCy NER model. Raw references were verified against the novel text and used to update patterns to include all aliases and character titles. This ensured all references to each character were counted in the final graph.

The graph captures **any** mention of a character in a novel, whether they actually appear or not. This was an intentional decision to ensure the graph captured characters' relative influence across *La Comedie Humaine*.
- Connection lines between characters and novels are weighted based on the frequency of the character's appearance in the novel. A thinner line denotes minor mentions (e.g., a single appearance at a party or a reference such as "a Nucingen" indicating a wealthy figure), while thicker lines indicate increasing centrality. Zoom in to better see line weights.
- Character nodes are scaled based on character occurrence counts across the corpus.
- Novel nodes are scaled based on the number of characters who appear.

## Planned Updates 
- Add metadata to character tooltips and filters for character attributes (gender, class, occupation).
- Add filters for characters by number of appearances.

## Future Updates
- Continue data cleaning, pattern design, and reference extraction for the next batch of 50 characters.

## Sources
All texts sourced from Project Gutenberg
Character aliases and titles validated with:
Cerfberr, and Christophe (1902): *Repertory of the Comedie Humaine.*

 
