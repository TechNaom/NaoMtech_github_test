projects = [
    {
        "name": "Project 1",
        "folders": [
            {"folder_name": "Folder 1", "size": "10 MB"},
            {"folder_name": "Folder 2", "size": "20 MB"},
            {"folder_name": "Folder 3", "size": "30 MB"},
        ]
    },
    {
        "name": "Project 2",
        "folders": [
            {"folder_name": "Folder A", "size": "15 MB"},
            {"folder_name": "Folder B", "size": "25 MB"},
        ]
    },
    {
        "name": "Project 3",
        "folders": [
            {"folder_name": "Folder X", "size": "40 MB"}
        ]
    }
]


# Function to create the dynamic HTML table
def generate_html_table(projects):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Projects Table</title>
        <style>
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            table, th, td {{
                border: 1px solid black;
            }}
            th, td {{
                padding: 10px;
                text-align: left;
            }}
        </style>
    </head>
    <body>

    <h2>Projects Table</h2>

    <table>
        <thead>
            <tr>
                <th>Project</th>
                <th>Project Folder</th>
                <th>Project Size</th>
            </tr>
        </thead>
        <tbody>
    """

    # Dynamically generate rows for each project and its folders
    for project in projects:
        project_name = project["name"]
        folders = project["folders"]
        html_content += f'<tr><td rowspan="{len(folders)}">{project_name}</td>'

        # Loop through folders and sizes
        for index, folder in enumerate(folders):
            if index > 0:
                html_content += "<tr>"  # Open new row for additional folders
            folder_name = folder["folder_name"]
            size = folder["size"]
            html_content += f"<td>{folder_name}</td><td>{size}</td></tr>"

    # Close the table and body tags
    html_content += """
        </tbody>
    </table>

    </body>
    </html>
    """
    return html_content


# Generate the HTML and save it to a file
html_output = generate_html_table(projects)



# Save to an HTML file
with open("projects_table.html", "w") as file:
    file.write(html_output)

print("HTML file generated successfully.")
