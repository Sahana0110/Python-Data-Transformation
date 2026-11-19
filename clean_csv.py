
import csv


# Function to read CSV file
def load_csv_rows(input_file):
    try:
        with open(input_file, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        print("File not found!")
        return []

    except (OSError, csv.Error) as error:
        print("Reading error:", error)
        return []


# Function to clean data
def clean_record(row):
    try:
        name = row["name"].strip().title()
        amount = float(row["amount"].strip())

        if name == "" or amount < 0:
            return None

        return {
            "name": name,
            "amount": round(amount, 2)
        }

    except (ValueError, TypeError, KeyError):
        return None


# Function to transform and save CSV
def transform_csv(input_file, output_file):

    rows = load_csv_rows(input_file)

    cleaned_rows = []
    skipped = 0

    for row in rows:
        result = clean_record(row)

        if result is not None:
            cleaned_rows.append(result)
        else:
            skipped += 1

    try:
        with open(output_file, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["name", "amount"]
            )

            writer.writeheader()
            writer.writerows(cleaned_rows)

        print("CSV cleaning completed successfully!")
        print("Valid records:", len(cleaned_rows))
        print("Skipped records:", skipped)
        print("Output file:", output_file)

    except OSError as error:
        print("Writing error:", error)


# Main program
if __name__ == "__main__":
    transform_csv("raw_sales.csv", "cleaned_sales.csv")
