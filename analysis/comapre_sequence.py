reference = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"
mutant = "MVHLTPVEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"
print("Reference length:", len(reference))
print("Mutant length:", len(mutant))
differences = []

for i in range(len(reference)):
    if reference[i] != mutant[i]:
        differences.append((i + 1, reference[i], mutant[i]))

print("Number of differences:", len(differences))

for position, ref, mut in differences:
    print("Position:", position)
    print("Reference:", ref)
    print("Mutant:", mut)
