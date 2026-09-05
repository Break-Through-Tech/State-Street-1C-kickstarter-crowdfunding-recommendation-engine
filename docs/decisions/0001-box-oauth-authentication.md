# Use OAuth 2.0 with Persistent Token Storage for Box Integration

## Context and Problem Statement

The project needs secure programmatic access to the team's raw Kickstarter dataset stored in Box. Team members should be able to access the shared Box data from Python and Jupyter notebooks without manually managing access tokens or committing credentials to the repository.

The authentication approach should:

* Support the team's Box Platform App using OAuth 2.0.
* Keep client credentials and OAuth tokens out of source control.
* Persist authentication between local development sessions.
* Use the current Box Python SDK.

## Considered Options

* OAuth 2.0 with `FileTokenStorage`
* OAuth 2.0 with in-memory token storage
* Manually storing and providing an access token

## Decision Outcome

Chosen option: **OAuth 2.0 with `FileTokenStorage`**, because

* OAuth 2.0 is the authentication method configured for the project's Box Platform App.
* `FileTokenStorage` provides persistent local token storage, avoiding repeated authorization during development sessions.
* Client credentials are loaded from environment variables rather than being stored in source code.
* Local credential and token files can be excluded from Git through `.gitignore`.
* The implementation uses the current Box Python SDK (`box_sdk_gen`).

## Consequences

### Positive

* Authentication persists across local Python/Jupyter sessions.
* Client credentials and OAuth tokens can remain outside the Git repository.
* The Box authentication logic can be reused across notebooks and project scripts.
* The approach follows the current Box SDK authentication model.

### Negative

* Each developer must configure their own local environment and Box credentials.
* A local token file must be protected and excluded from source control.
* Initial OAuth authorization requires a local callback flow.

## More Information

* [Box Python SDK](https://github.com/box/box-python-sdk)
* [Box OAuth 2.0 and token storage documentation](https://github.com/box/box-python-sdk/blob/main/docs/authentication.md)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
