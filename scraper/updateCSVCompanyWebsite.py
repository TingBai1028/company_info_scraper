import pandas as pd
from searchCompany import get_first_organic_result

def update_company_websites(csv_file, output_csv):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Iterate over the rows of the DataFrame
    for index, row in df.iterrows():
        # Check if the company doesn't have a website
        if pd.isna(row['Company Website']):
            company_name = row['Company Name']
            print(f"Searching for {company_name}...")

            # Use the function to get the first organic result (website)
            website = get_first_organic_result(company_name)

            # Update the 'Company Website' column with the found website
            df.at[index, 'Company Website'] = website
            print(f"Found website for {company_name}: {website}")

    # Save the updated DataFrame back to CSV
    df.to_csv(output_csv, index=False)

    print(f"CSV file has been updated and saved to {output_csv}.")

# Usage example
csv_file = '../data/sydneybuildexpo.csv'  # Input CSV file
output_csv = '../data/sydneybuildexpo copy.csv'  # Output CSV file with updated websites
update_company_websites(csv_file, output_csv)
