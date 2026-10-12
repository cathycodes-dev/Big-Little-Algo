# Big-Little-Algo

This repository contains the Big-Little matching algorithm used by the Psi Upsilon fraternity (Gamma Tau Chapter). It applies the principles of the **Gale-Shapley (Deferred Acceptance) algorithm** to pair pledges with brothers, prioritizing pledge preferences while ensuring stable matches.

You can run this project locally in Python or directly in the browser via WebAssembly (Pyodide) on the website.

## CSV File Requirements & Formatting

Whether running locally or using the web application, your preference lists must follow these strict rules:

1. **Exact Name Matching:** Ensure spelling and capitalization match *exactly* across both CSV files.
2. **File Naming:** Use the exact filenames `BigListChoices.csv` and `LittleListChoices.csv`.
3. **No Headers:** Do not include a header or title row at the top of either file.
4. **Dropped Pledges:** If a pledge drops or depledges, remove their name entirely from both files.

### 1. `BigListChoices.csv` Format
Each row contains a **Pledge** followed by their ranked **Brother** choices:
```csv
Zendaya,Beyoncé,Leonardo DiCaprio,Keanu Reeves,Pedro Pascal
Timothée Chalamet,Keanu Reeves,Beyoncé,Rihanna,Leonardo DiCaprio

```

### 2. `LittleListChoices.csv` Format

Each row contains a **Brother**, whether they want a little (`Yes`/`No`), followed by their ranked **Pledge** choices:

```csv
Beyoncé,Yes,Zendaya,Sabrina Carpenter,Timothée Chalamet
Keanu Reeves,Yes,Timothée Chalamet,Sabrina Carpenter,Zendaya
Meryl Streep,No

```

## Option 1: Running via the Website

Visit [big-little.cathycodes.com](https://big-little.cathycodes.com) to run the matching algorithm without installing Python:

1. **Run with Sample Data:** Click **"Run with Sample Data"** to execute the demo using built-in sample preference lists loaded from the `./src` folder.
2. **Upload Custom CSVs:** Select your custom `BigListChoices.csv` and `LittleListChoices.csv` files under **Option B** and click **"Upload & Run Custom CSVs"**.
3. **View Results:** Matches will stream directly into the embedded web terminal in the following format:
```text
-Pledge matched with Brother

```

## Option 2: Running Locally via Terminal

### Prerequisites

* Install [Python 3](https://www.python.org/downloads/) on your computer.

### Steps

1. Place `BigListChoices.csv`, `LittleListChoices.csv`, `data.py`, and `main.py` in the same directory (`./src`).
2. Open your terminal in that folder.
3. Run the script:
```bash
python main.py

```


4. Output matches will print to your terminal:
```text
-Pledge matched with Brother

```

## Project Structure

```text
.
├── index.html            # Web interface with Pyodide runtime & xterm.js terminal
├── default_styles.css    # Site design system & global styling
├── terminal_styles.css   # Terminal & controls card styling
├── src/
│   ├── data.py           # Data parser for reading and filtering CSV lists
│   ├── main.py           # Gale-Shapley matching algorithm & execution logic
│   ├── BigListChoices.csv # Sample pledge preferences
│   └── LittleListChoices.csv # Sample brother preferences
└── terraform/           # Infrastructure as Code for AWS S3 & CloudFront deployment

```

## Deployment & CI/CD

This repository uses **GitHub Actions** and **Terraform** for continuous deployment:

* Pushes to the `main` branch trigger Terraform validation, plan, and apply inside the `terraform/` directory.
* Website assets and Python game files in `./src` are synchronized to AWS S3.
* CloudFront cache invalidation is automatically triggered using the `${{ env.PROJECT_NAME }}.${{ env.DOMAIN }}` distribution alias.

## Support

If you encounter errors or need assistance running the algorithm, contact Cathy Lefebvre at me@cathycodes.com.
