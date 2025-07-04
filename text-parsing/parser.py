import re
import csv
import os

def extract_table_data(html_string):
    """
    Extracts data from the HTML table using regular expressions.

    Args:
      html_string: The HTML string containing the table.

    Returns:
      A list of lists, where each inner list represents a row in the table.
    """

    rows = re.findall(r'<tr.*?>(.*?)</tr>', html_string, re.DOTALL)
    data = []

    for row in rows:
        cells = re.findall(r'<td.*?>(.*?)</td>', row, re.DOTALL)

        if cells:
            cleaned_cells = []
            for cell in cells:
                # Use regex to remove span tags and extract text content
                text = re.sub(r'<[^>]+>', '', cell).strip()

                # Remove double quotes
                text = text.replace('"', '')
                cleaned_cells.append(text)
            data.append(cleaned_cells)
    # print(data)
    return data


def main():
    """
    Reads HTML from a file, extracts data, and writes it to a CSV file.
    """
    data_dir = "data"
    output_csv = "iit-closing-ranks.csv"

    all_data = []
    header = ["College","Branch","Category","Gender","OpeningRank","ClosingRank","Year", "Round"]

    file_list = [f for f in os.listdir(data_dir) if f.endswith(".aspx")]

    for filename in file_list:
        try:

            match = re.match(r"(\d{4})-IIT-(\d+)\.aspx", filename)
            if match:
                year = match.group(1)
                round_num = match.group(2)

                with open(os.path.join(data_dir, filename), "r", encoding="utf-8") as f:
                    html_string = f.read()

                data = extract_table_data(html_string)

                for row in data:
                    new_row = [year, round_num] + row
                    all_data.append(new_row)

            else:
                print(f"Skipping file {filename}: Filename format incorrect.")

        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
        except Exception as e:
            print(f"Error processing file {filename}: {e}")

    try:
        with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(header)
            csv_writer.writerows(all_data)

        print(f"Data extracted and saved to {output_csv}")

    except Exception as e:
        print(f"Error writing to CSV file: {e}")


if __name__ == "__main__":
    main()