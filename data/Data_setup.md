# Data Setup

The Kickstarter dataset is stored in the team's Google Drive rather than committed to GitHub.

## Google Drive location

```text
1C-Kickstarter-recommendation-engine/
└── Raw-data/
    ├── DSI_kickstarterscrape_dataset.csv
    └── DSI_kickstarterscrape_dataset.zip
```

The CSV file used by the project is:

```text
DSI_kickstarterscrape_dataset.csv
```

## Download the dataset

### 1. Set up the Python environment

From the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Set up Google Drive credentials

Ask a team member for the project's Google Cloud OAuth `credentials.json` file.

Place `credentials.json` in the project root:

```text
project-root/
├── credentials.json
├── utils/
├── data/
└── ...
```

Do **not** commit `credentials.json` to GitHub.

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
GOOGLE_DRIVE_DATA_FOLDER_ID=<Raw-data folder ID>
GOOGLE_DRIVE_DATA_FILE_NAME=DSI_kickstarterscrape_dataset.csv
```

The `GOOGLE_DRIVE_DATA_FOLDER_ID` should be the ID of the Google Drive `Raw-data` folder.

Do not commit `.env`.

### 4. Authenticate and download

Run:

```bash
cd utils
python3 get_google_drive_data.py
```

On the first run, Google will open a browser window for OAuth authentication. After successful authentication, a local `token.json` file will be created.

The script searches the configured `Raw-data` folder for the CSV and downloads it to:

```text
data/DSI_kickstarterscrape_dataset.csv
```

### 5. Verify the download

You should see output similar to:

```text
Found file: DSI_kickstarterscrape_dataset.csv
Downloaded file to: .../data/DSI_kickstarterscrape_dataset.csv
```

The downloaded dataset is intentionally excluded from Git with `.gitignore`.

## Files used for Google Drive integration

* `utils/google_drive_client.py` handles Google Drive OAuth authentication.
* `utils/get_google_drive_data.py` finds and downloads the dataset.
* `.env` stores local configuration.
* `credentials.json` and `token.json` store local OAuth credentials/tokens and must not be committed.

If authentication fails, make sure your Google account has access to the team's Google Drive data and that your account is authorized as a test user for the Google Cloud OAuth application.
