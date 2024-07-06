def enumerate_stanzas_and_save(file_path_in, file_path_out):
    # Read the poem text from the input file
    with open(file_path_in, 'r') as file:
        lines = file.readlines()
    
    # Extract the title and stanzas
    title = lines[0].strip()
    stanzas = ''.join(lines[1:]).split('\n\n')
    
    # Prepare to write to the output file
    with open(file_path_out, 'w') as file:
        # Write the title surrounded by ==
        file.write(f"== {title} ==\n\n")
        
        for i, stanza in enumerate(stanzas, start=1):
            # Add stanza number before each stanza
            file.write(f"[Stanza {i}]\n")
            file.write(stanza.strip() + "\n\n")  # Add an extra newline for separation
    
    print(f"Stanzas enumerated and saved to '{file_path_out}'")

# File paths
file_path_in = './Lyrical_Verses/GreenEggsAndHam.txt'
file_path_out = './Lyrical_Verses/Enumerated_GreenEggsAndHam.txt'

# Call the function to enumerate stanzas and save to a file
enumerate_stanzas_and_save(file_path_in, file_path_out)
