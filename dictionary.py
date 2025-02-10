


sonal_dictionary = {}


while True:
    gene_name = input("Enter a gene name (or type 'exit' to stop): ")

    if gene_name.lower() == 'exit':
        break

    gene_info = input(f"Enter the description for {gene_name}: ")

    sonal_dictionary[gene_name] = gene_info


print("\nFinal Gene Dictionary:")
print(sonal_dictionary)
print("\nThis dictionary stores gene names as keys and their descriptions as values.")



