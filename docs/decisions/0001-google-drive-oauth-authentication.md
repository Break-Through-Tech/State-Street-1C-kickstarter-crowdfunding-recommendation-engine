# Use OAuth 2.0 with Persistent Token Storage for Google Drive Integration

## Context and Problem Statement

The project needs secure programmatic access to the team's raw Kickstarter dataset stored in Google Drive. Team members should be able to access the shared Google Drive data from Python and Jupyter notebooks without manually managing access tokens or committing credentials to the repository.

The previous implementation used Box OAuth 2.0, but Box access was not practical in the team's current development environment. The project therefore needs an alternative cloud storage integration that:

* Supports secure OAuth 2.0 authentication.
* Allows programmatic access to the team's shared Google Drive data.
* Keeps client credentials and OAuth tokens out of source control.
* Persists authentication between local development sessions.
* Supports downloading the raw CSV dataset directly from Google Drive.

## Considered Options

* Continue using Box OAuth 2.0.
* Use Google Drive API with OAuth 2.0.
* Use Dropbox API with OAuth 2.0.

## Decision Outcome

Chosen option: **Google Drive API with OAuth 2.0 and persistent local token storage**, because

* Google Drive provides access to the team's existing shared raw dataset.
* The Google Drive API supports OAuth 2.0 authentication for local development.
* OAuth tokens can be persisted locally in `token.json`, avoiding repeated authorization during development sessions.
* Client credentials are stored locally in `credentials.json` rather than in source code.
* Environment-specific configuration, including the Google Drive folder ID and dataset filename, is loaded from environment variables.
* The Google Drive API supports programmatic discovery and downloading of the raw Kickstarter CSV file.
* Credential, token, environment, and local data files can be excluded from Git through `.gitignore`.

## Consequences

### Positive

* Team members can programmatically download the raw dataset from Google Drive.
* Authentication persists across local development sessions.
* Client credentials and OAuth tokens remain outside the Git repository.
* The Google Drive integration can be reused across project scripts and notebooks.
* The raw dataset does not need to be committed to GitHub.
* The integration uses the official Google Drive API and Python client libraries.

### Negative

* Each developer must configure their own local Google OAuth environment.
* Developers need access to the team's Google Drive data.
* Initial OAuth authorization requires a browser-based local authentication flow.
* Developers must obtain the project's OAuth client credentials and configure the required environment variables.
* The Google Cloud OAuth application must be configured correctly for authorized users during development.

## More Information

* [Google Drive API Python Quickstart](https://developers.google.com/workspace/drive/api/quickstart/python)
* [Google Drive API Search for Files and Folders](https://developers.google.com/workspace/drive/api/guides/search-files)
* [Google Drive API Download Files](https://developers.google.com/workspace/drive/api/guides/manage-downloads)
* `utils/google_drive_client.py`
* `utils/get_google_drive_data.py`
* Related issue: #12
