# Chapters 1 & 2 Recap exercise: Clean Up & Format 
raw_filename = "  user_report_draft.txt\n\t "

# Strip surrounding whitespace and remove extension
trimmed_filename = raw_filename.strip().removesuffix('.txt')
# Format spaces and casing
clean_title = trimmed_filename.replace("_", " ").title()

year = 2026

print(f"Document: {clean_title} | Year: {year}")