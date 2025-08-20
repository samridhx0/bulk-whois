# WHOIS Lookup Tool

![TURNTOGIF (1)](https://github.com/user-attachments/assets/373adba8-d6a7-4684-a0a3-a46c155d96b8)


A Python tool for bulk WHOIS lookups, with output formatted in a clean, full-page HTML report.

## Overview

This tool performs WHOIS lookups on a list of domains or URLs provided in a text file, and generates a well-formatted HTML file with the results. Designed for clarity and functionality, the output includes essential WHOIS data in a scrollable table for easy viewing, even with large datasets.

## Features

- **Bulk WHOIS Lookup**: Process a list of domains/URLs with a single command.
- **Full-Page HTML Report**: Generates a scrollable, responsive HTML table with WHOIS data.
- **Data Integrity**: Includes a SHA-256 hash of the WHOIS results at the top of the report.
- **Comprehensive WHOIS Data**: Retrieves additional fields like country, state, city, registrant, and email when available.

---

## Installation

Clone this repository and install the required dependencies.

```bash
git clone https://github.com/samridhx0/whois-lookup-tool.git
cd whois-lookup-tool
pip install -r requirements.txt
```

Dependencies:

- `python-whois`
- `pandas`

Or install directly:

```bash
pip install python-whois pandas
```

---

## Usage

1. Prepare a text file with a list of domains or URLs, one per line. Example:

   ```
   https://example.com
   openai.com
   https://github.com
   ```

2. Run the Python script:

   ```bash
   python whois_bulk_lookup.py
   ```

3. When prompted, enter the path to your text file (e.g., `domains.txt`):

   ```plaintext
   Enter the path to the file containing the list of domains/URLs: domains.txt
   ```

4. The tool will output an HTML file named `whois_results.html`, containing a full-page layout with WHOIS results.

### Sample Output

The HTML report includes:

- **Domain Details**: Registrar, creation date, expiration date, last updated, status, and name servers.
- **Registrant Information**: Country, state, city, registrant, and emails (when available).
- **SHA-256 Hash**: A hash at the top for result verification.


## License

This project is licensed under the MIT License.

---

## Contributing

Contributions are welcome. Open an issue, submit a pull request, or reach out with feedback.
