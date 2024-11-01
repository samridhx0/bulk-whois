import whois
import pandas as pd
import hashlib
import re

def get_domain_from_url(url):
    # Extract domain name from URL
    domain_pattern = re.compile(r'https?://(www\.)?')
    domain = domain_pattern.sub('', url).strip().split('/')[0]
    return domain

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        return {
            "Domain": domain,
            "Registrar": w.registrar,
            "Creation Date": w.creation_date,
            "Expiration Date": w.expiration_date,
            "Last Updated": w.updated_date,
            "Status": w.status,
            "Name Servers": ', '.join(w.name_servers) if w.name_servers else None,
            "Country": w.country,
            "State": w.state,
            "City": w.city,
            "Registrant": w.registrant,
            "Emails": ', '.join(w.emails) if w.emails else None
        }
    except Exception as e:
        return {"Domain": domain, "Error": str(e)}

def perform_whois_lookups(domains):
    results = []
    for domain in domains:
        domain_name = get_domain_from_url(domain)
        info = whois_lookup(domain_name)
        results.append(info)
    return results

def calculate_hash(results):
    # Convert results to a string to generate a hash
    data_str = ''.join(str(results))
    hash_object = hashlib.sha256(data_str.encode())
    return hash_object.hexdigest()

def save_results_to_html(results, output_file='whois_results.html'):
    # Calculate hash for the results
    data_hash = calculate_hash(results)
    
    df = pd.DataFrame(results)
    
    # Generate HTML with inline CSS for full-page layout
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WHOIS Lookup Results</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                color: #333;
                padding: 20px;
                margin: 0;
            }}
            h1 {{
                text-align: center;
                color: #4CAF50;
            }}
            .hash {{
                font-size: 14px;
                color: #888;
                text-align: center;
                margin-bottom: 20px;
                word-break: break-all;
            }}
            .table-container {{
                overflow-x: auto;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }}
            table, th, td {{
                border: 1px solid #ddd;
            }}
            th, td {{
                padding: 10px;
                text-align: center;
                white-space: nowrap; /* Prevents text wrapping for large cells */
            }}
            th {{
                background-color: #4CAF50;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>WHOIS Lookup Results</h1>
        <div class="hash"><strong>SHA-256 Hash:</strong> {data_hash}</div>
        <div class="table-container">
            {df.to_html(index=False, classes='data-table', border=0)}
        </div>
    </body>
    </html>
    """


    with open(output_file, "w") as file:
        file.write(html_content)
    print(f"HTML file has been created successfully: {output_file}")

def load_domains_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]


def main():
    file_path = input("Enter the path to the file containing the list of domains/URLs: ")
    
    # Load domains from the provided file
    domains = load_domains_from_file(file_path)
    
    # Perform WHOIS lookups
    results = perform_whois_lookups(domains)
    
    # Save results to an HTML file
    save_results_to_html(results)

if __name__ == "__main__":
    main()
