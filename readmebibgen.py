import bibtexparser

def bibtex_to_markdown(bibtex_file, output_md_file):
    # Load the .bib file
    with open(bibtex_file, 'r', encoding='utf-8') as bibfile:
        bib_database = bibtexparser.load(bibfile)
    
    entries = bib_database.entries

    markdown_entries = []
    for entry in entries:
        title = entry.get('title', 'No Title').replace('{', '').replace('}', '')
        author = entry.get('author', 'No Author').replace('\n', ' ')
        year = entry.get('year', 'n.d.')
        journal = entry.get('journal') or entry.get('booktitle') or 'No Journal'
        doi = entry.get('doi')
        url = entry.get('url')

        # Format the Markdown entry
        markdown_entry = f"- **{title}**. {author}. *{journal}*, {year}."
        if doi:
            markdown_entry += f" [DOI](https://doi.org/{doi})"
        elif url:
            markdown_entry += f" [Link]({url})"
        
        markdown_entries.append(markdown_entry)

    # Save to README markdown file
    with open(output_md_file, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(markdown_entries))
    
    print(f"Successfully created: {output_md_file}")

# Example usage
bibtex_to_markdown('references.bib', 'references.md')