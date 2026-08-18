fiction = {
    "To Kill a Mockingbird",
    "1984",
    "The Great Gatsby",
    "Brave New World",
    "Catch-22",
    "Animal Farm",
}
non_fiction = {
    "A Brief History of Time",
    "The Selfish Gene",
    "Guns, Germs, and Steel",
    "The Righteous Mind",
    "Sapiens",
    "1984",
}
biographies = {
    "The Diary of a Young Girl",
    "Long Walk to Freedom",
    "Steve Jobs",
    "Into the Wild",
    "Sapiens",
    "A Beautiful Mind",
}

both_fiction_non_fiction = fiction.intersection(non_fiction)
print("Both fiction and non-fiction:", both_fiction_non_fiction)

unique_fiction = fiction - non_fiction - biographies
unique_non_fiction = non_fiction - fiction - biographies
unique_biographies = biographies - fiction - non_fiction
print("\nUnique books:")
print("Fiction:", unique_fiction)
print("Non-fiction:", unique_non_fiction)
print("Biographies:", unique_biographies)

fiction_non_fiction_excluding_biographies = (fiction | non_fiction) - biographies
print(
    "\nFiction or non-fiction (excluding biographies):",
    fiction_non_fiction_excluding_biographies,
)

must_read = fiction & non_fiction & biographies
print("\nMust-read:", must_read)

is_proper_subset = biographies.issubset(fiction | non_fiction) and biographies != (
    fiction | non_fiction
)
print("\nBiographies subset:", is_proper_subset)

symmetric_difference = (fiction | non_fiction).symmetric_difference(biographies)
symmetric_difference_sorted = sorted(symmetric_difference)
print("\nSymmetric difference:", symmetric_difference_sorted)

print("\nBooks and counts:")
print("Fiction:")
for book in sorted(fiction):
    print(book)
print("Total:", len(fiction))

print("\nNon-fiction:")
for book in sorted(non_fiction):
    print(book)
print("Total:", len(non_fiction))

print("\nBiographies:")
for book in sorted(biographies):
    print(book)
print("Total:", len(biographies))
