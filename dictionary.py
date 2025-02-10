gene_dict = {}

while True:
    gene_name = input("Enter a gene name (or type 'exit' to stop): ").strip()

    if gene_name.lower() == 'exit':
        break

    gene_info = input(f"Enter the description for {gene_name}: ").strip()

    gene_dict[gene_name] = gene_info

print("\nFinal Gene Dictionary:")
for gene, description in gene_dict.items():
    print(f"{gene}: {description}")

print("\nThis dictionary stores gene names as keys and their descriptions as values.")
