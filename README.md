# Test Applicant Module

## Overview
This Odoo module, `test_applicant`, provides a basic applicant tracking system with functionalities such as creating applicants, managing states, and assigning unique reference codes. It also includes access control mechanisms for user permissions.

## Features
- **Custom Model (`test.applicant`)**
  - Fields: `name`, `description`, `active`, `reference_code`, `state`
  - Auto-generated `reference_code` (Unique, Sequential, Reset Daily)
  - State transitions: `draft → confirmed → done`
- **Menu & Views**
  - Accessible under *Settings > Test Applicant*
  - Tree & Form Views
- **Security**
  - Restricted to `test_applicant.group_test_applicant_manager`
- **Confirm Button**
  - Changes state to `confirmed`

## Installation
1. Copy the module folder (`test_applicant`) into your Odoo `addons` directory.
2. Restart the Odoo service:
   ```sh
   sudo service odoo restart
   ```
3. Enable developer mode in Odoo.
4. Navigate to *Apps* and update the module list.
5. Install the **Test Applicant** module.

## Usage
### Creating a Test Applicant
1. Go to *Settings > Test Applicant*.
2. Click *Create* and enter applicant details.
3. Click *Confirm* to move to the `confirmed` state.

### Managing Records
- **Auto-generated Reference Code**
  - The format is `TEST-0001`, `TEST-0002`, etc.
  - Resets daily to start from `TEST-0001`.
- **State Transition**
  - Users can confirm applicants via the *Confirm* button.
  - A cron job automatically marks confirmed applicants as `done` after 30 minutes.

## Security
- Only users in the `Test Applicant Manager` group can access and manage applicants.
- This group is not assigned to any user by default; it must be manually assigned.

## Files and Directories
```
test_applicant/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── test_applicant.py
├── security/
│   ├── ir.model.access.csv
│   ├── security.xml
├── views/
│   ├── test_applicant_views.xml
│   ├── menu.xml
```

## Notes
- Ensure that users have the correct group permissions before using the module.
- The cron job runs every 5 minutes to check for applicants in the `confirmed` state older than 30 minutes and updates them to `done`.

## Troubleshooting
- If the module does not appear, update the app list in *Apps*.
- Ensure `odoo` has the correct permissions for the module files.

For any issues, check the Odoo logs:
```sh
sudo tail -f /var/log/odoo/odoo.log
```

