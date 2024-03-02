<div align="center">
<img alt="..." src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white">
<img alt="..." src="https://img.shields.io/badge/python-3.11-blue?style=for-the-badge">

<a href="https://github.com/o54ma-4l5h4r1f/Sentinel-Analytic-Rules-Mgm/issues">
  <img alt="..." src="https://img.shields.io/github/issues/o54ma-4l5h4r1f/Sentinel-Analytic-Rules-Mgm.svg?style=for-the-badge">
</a>

<!--
<a href="https://github.com/o54ma-4l5h4r1f/Sentinel-Analytic-Rules-Mgm/graphs/contributors">
  <img alt="GitHub forks" src="https://img.shields.io/github/contributors/o54ma-4l5h4r1f/Sentinel-Analytic-Rules-Mgm.svg?style=for-the-badge">
</a>
-->

<a href="https://github.com/o54ma-4l5h4r1f/Sentinel-Analytic-Rules-Mgm/network/members">
  <img alt="GitHub forks" src="https://img.shields.io/github/forks/o54ma-4l5h4r1f/Sentinel-Analytic-Rules-Mgm?style=for-the-badge">
</a>

<a href="https://github.com/o54ma-4l5h4r1f/Sentinel-Analytic-Rules-Mgm/stargazers">
  <img alt="..." src="https://img.shields.io/github/stars/o54ma-4l5h4r1f/Sentinel-Analytic-Rules-Mgm.svg?style=for-the-badge">
</a>

<a href="https://github.com/o54ma-4l5h4r1f?tab=followers">
  <img alt="..." src="https://img.shields.io/github/followers/o54ma-4l5h4r1f?style=for-the-badge">
</a>

<a href="https://www.linkedin.com/in/osama-alsharif-21153716a">
  <img alt="..." src="https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555">
</a>

</div>

  <h3 align="center">Sentinel-Analytic-Rules-Mgm</h3>
  <h5 align="center">Microsoft Sentinel Analytic Rules Management &amp; Assessment tool</h5>

<!-- PROJECT LOGO -->
<p align="center">
  <a href="#"><pre align="center">
      ___           ___           ___       ___           ___     
     /\  \         /\__\         /\__\     /\  \         /\  \    
    /::\  \       /:/  /        /:/  /    /::\  \       /::\  \   
   /:/\:\  \     /:/  /        /:/  /    /:/\:\  \     /:/\ \  \  
  /::\~\:\  \   /:/  /  ___   /:/  /    /::\~\:\  \   _\:\~\ \  \ 
 /:/\:\ \:\__\ /:/__/  /\__\ /:/__/    /:/\:\ \:\__\ /\ \:\ \ \__\
 \/_|::\/:/  / \:\  \ /:/  / \:\  \    \:\~\:\ \/__/ \:\ \:\ \/__/
    |:|::/  /   \:\  /:/  /   \:\  \    \:\ \:\__\    \:\ \:\__\  
    |:|\/__/     \:\/:/  /     \:\  \    \:\ \/__/     \:\/:/  /  
    |:|  |        \::/  /       \:\__\    \:\__\        \::/  /   
     \|__|         \/__/         \/__/     \/__/         \/__/    
  </pre></a>


</p>

## :star2: About the Tool

Sentinel-Analytic-Rules-Mgm is a tool designed for managing and assessing Microsoft Sentinel Analytic Rules across multiple tenants' workspaces seamlessly. Developed using Azure SDK for Python. This script streamlines the process of performing various actions on analytic rules while utilizing a single set of authentication credentials. Its functionality enables users to execute actions on a set of selected analytic rules, optimizing the management of them.

### Key Features:
#### :one: Tenant Selection:
Allows users to specify the tenants whose analytic rules they intend to target, ensuring focused and efficient rule management.

#### :two: Rule Selection: 
Enables users to select analytic rules either by their names or a partial match, facilitating flexible and precise rule targeting.

#### :three: Actionable Operations:
- _**Listing**_: Provides the ability to list selected rules to view their IDs.
  
- _**Updating**_:
  - _**Manually**_: Users have the ability to update the selected rules manually, choosing from various options to tailor the rules' configurations, such as:
    - **Display Name**: Modify the display name of the selected rules. including options to update the entire name or parts of it by adding prefixes or suffixes, as well as removing them.
    - **Description**: Update the description of the rules.
    - **Severity**: Adjust the severity level of the rules to reflect the importance of the detections.
    - **Enable/Disable**: Toggle the enabled/disabled status of the rules to control their activation and enforcement.
    - **KQL Query**: Enhance rule tuning by updating the KQL query of the rules, refining their logic for improved detection accuracy.

  - _**Copy and Apply Properties**_: Rather than manually adjusting each property individually, users can make detailed updates to one rule using the Azure Sentinel portal and seamlessly propagate these changes across all other selected rules using the script, streamlining the update process while ensuring consistency and accuracy across the board
- _**Replication**_:  allows users to selectively replicate chosen rule only in tenants' workspaces where they are not exist.
- _**Comparison**_: Offers functionality to compare the existence of analytic rules across different tenants' workspaces, assisting in maintaining uniformity and identifying discrepancies.


:low_brightness: there's room for adding more features to the tool. I'm open to hearing your suggestions and seeing your contributions to make it even better.

<!-- Getting Started -->



## :computer: Getting Started

> [!NOTE]  
> This script can run on a Windows machine for now, so make sure that python & git are installed. 

Install the Azure Developer CLI [Link](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd?tabs=winget-windows%2Cbrew-mac%2Cscript-linux&pivots=os-windows)
```bash
> winget install microsoft.azd
```

On powershell

```bash
# Clone the project
> git clone https://github.com/o54ma-4l5h4r1f/Sentinel-Analytic-Rules-Mgm.git

# Go to the project directory
> cd Sentinel-Analytic-Rules-Mgm

# Install the requirements
> pip install -r requirments.txt
```
And make sure to restart the powershell terminal after the installation ends

## 🩹 Update DataBase.json file
To access related resources, you'll need to update the `DataBase.json` file with your specific information. Follow these steps:

1. Open the `DataBase.json` file located in the root directory of this repository.

2. Add a new entry or update an existing one following the JSON template below:

```json
{
    "1" : {
        "tenant_name" : "Display Name",
        "subscription_id" : "5cfeafdb-fc6b-xxxx-xxxx-xxxxxxxxxxxx",
        "resource_group_name" : "Resourse Group",
        "workspace_name" : "WorkSpace Name"
    },
    "2" : {
        "tenant_name" : "Display Name 2",
        "subscription_id" : "7a3cafdb-fc6b-xxxx-xxxx-xxxxxxxxxxxx",
        "resource_group_name" : "Resourse Group 2",
        "workspace_name" : "WorkSpace Name 2"
    }
}
```
3. Save the changes to the file.
   
## :jack_o_lantern: Lets Run It
```powershell
> python3 .\main.py
```
```        

      ___           ___           ___       ___           ___     
     /\  \         /\__\         /\__\     /\  \         /\  \    
    /::\  \       /:/  /        /:/  /    /::\  \       /::\  \   
   /:/\:\  \     /:/  /        /:/  /    /:/\:\  \     /:/\ \  \  
  /::\~\:\  \   /:/  /  ___   /:/  /    /::\~\:\  \   _\:\~\ \  \ 
 /:/\:\ \:\__\ /:/__/  /\__\ /:/__/    /:/\:\ \:\__\ /\ \:\ \ \__\
 \/_|::\/:/  / \:\  \ /:/  / \:\  \    \:\~\:\ \/__/ \:\ \:\ \/__/
    |:|::/  /   \:\  /:/  /   \:\  \    \:\ \:\__\    \:\ \:\__\  
    |:|\/__/     \:\/:/  /     \:\  \    \:\ \/__/     \:\/:/  /  
    |:|  |        \::/  /       \:\__\    \:\__\        \::/  /   
     \|__|         \/__/         \/__/     \/__/         \/__/     



    Welcome to the Analytic Rules Management & Assessment tool


Authenticatiion setup:

1) Login to Azure
2) Relogin to Azure
3) Logout from Azure

```
A browser tab will open, allowing you to log in with the appropriate account. If you're already logged in, this step will be skipped.
```
>>> 1
[+] Already Logged into Azure.

Which tenants workspaces are you going to work on:
[EX1] 1,2,3,4,5,...
[EX2] 1-3,6-7,9,...
[NOTE] You can update the tenants list by modifying the 'DataBase.json' file
1 ) Company-1           2 ) Company-2           3 ) Company-3
4 ) Company-4           5 ) Company-5           6 ) Company-6
7 ) Company-7           8 ) Company-8           9 ) ...
>>>
```
The list of tenants displayed will be determined by the information you've provided in the DataBase.json file.
```
>>> 1-4
[+] The selected tenants : 1,2,3,4

Choose the action:
1) Select Rules         2) List Selected Rules
3) Update Rules         4) Rules Comparison/Assessment
5) Create Rules         6) help
```


Selecting analytic rules that containes `DEV` in their names

> [!NOTE]  
> The script does not currently support NRT anallytic rules.

```
>>> 1

1) Select Rules By Name

>>> 1
Rule Name (or part of it) > DEV
[+] looking into client #1 (Company-1)
[+] A total of 1 rules found

The matched rules
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
[+] looking into client #2 (Company-2)
[+] A total of 302 rules found

The matched rules
----------------------------------------------------------------------------------------------------
[DEV] | Pulse Connect Secure VPN-CVE_2021_22893_Exploit
[DEV] | Known Malware Detected
[DEV] | Shadow Copy Deletion
----------------------------------------------------------------------------------------------------
[+] looking into client #3 (Company-3)
[+] A total of 260 rules found

The matched rules
----------------------------------------------------------------------------------------------------
User Login from Different Countries Within 3 Hours [DEV]
Suspicious Url Clicked [DEV]
----------------------------------------------------------------------------------------------------
[+] looking into client #4 (Company-4)
[+] A total of 335 rules found

The matched rules
----------------------------------------------------------------------------------------------------
[DEV] Anomalous Sign-in Detected by a User
[DEV] User Login from Different Countries Within 3 Hours
[DEV] Suspicious Url Clicked
----------------------------------------------------------------------------------------------------

Choose the action:
1) Select Rules         2) List Selected Rules
3) Update Rules         4) Rules Comparison/Assessment
5) Create Rules         6) help
```
List the selected rules 
```
>>> 2

The selected rules
----------------------------------------------------------------------------------------------------
Company-2               d8dcfbbb-e914-4622-a96e-68907d61c9f9    [DEV] | Pulse Connect Secure VPN-CVE_2021_22893_Exploit
Company-2               9d15b6b7-3289-48a0-b7d2-f72266277ddd    [DEV] | Known Malware Detected
Company-2               5759e9ec-df80-4cd2-82bd-083d796bbd30    [DEV] | Shadow Copy Deletion
Company-3               42718c04-51b3-4b7f-8511-0c19252ea44b    User Login from Different Countries Within 3 Hours [DEV]
Company-3               28810579-a6d6-4e13-aecb-396941cfa5dd    Suspicious Url Clicked [DEV]
Company-4               224b8b16-0de2-4bd7-8da1-4b7d578de58b    [DEV] Anomalous Sign-in Detected by a User
Company-4               80255886-e3b8-495e-88d3-05f1c571aada    [DEV] User Login from Different Countries Within 3 Hours      
Company-4               28910579-a6d6-4e13-aecb-396941cfa5dd    [DEV] Suspicious Url Clicked
----------------------------------------------------------------------------------------------------

Choose the action:
1) Select Rules         2) List Selected Rules
3) Update Rules         4) Rules Comparison/Assessment
5) Create Rules         6) help
```
Update the selected rules manually
```
>>> 3

Choose the update method : 
1) Update from an Existing Rule                 2) from a JSON file
3) Manually

>>> 3

What to update : 
1) Enable               2) Disable              3) Display Name
4) Description          5) Severity             6) KQL Query

>>> 1
Are you sure you want to enable all the selected rules [Y/n] ? Y
Enabling the rule (d8dcfbbb-e914-4622-a96e-68907d61c9f9)
Enabling the rule (9d15b6b7-3289-48a0-b7d2-f72266277ddd)
Enabling the rule (5759e9ec-df80-4cd2-82bd-083d796bbd30)
Enabling the rule (42718c04-51b3-4b7f-8511-0c19252ea44b)
Enabling the rule (28810579-a6d6-4e13-aecb-396941cfa5dd)
Enabling the rule (224b8b16-0de2-4bd7-8da1-4b7d578de58b)
Enabling the rule (80255886-e3b8-495e-88d3-05f1c571aada)
Enabling the rule (28910579-a6d6-4e13-aecb-396941cfa5dd)

Choose the action:
1) Select Rules         2) List Selected Rules
3) Update Rules         4) Rules Comparison/Assessment
5) Create Rules         6) help
```

Updating the selected rules using one of them after editing it using sentinel.  

<img width="874" alt="image" src="https://github.com/o54ma-4l5h4r1f/Sentinel-Analytic-Rules-Mgm/assets/90612145/e7510d62-ac8f-4e74-9130-34d258f05092">


> [!WARNING]  
> Ensure that you select one rule from each tenant to avoid overwriting multiple rules with the same one in the same workspace, which could lead to errors.

```
>>> 1

1) Select Rules By Name

>>> 1
Rule Name (or part of it) > User Login from Different Countries Within 3 Hours
[+] looking into client #1 (Company-1)
[+] A total of 1 rules found

The matched rules
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
[+] looking into client #2 (Company-2)
[+] A total of 302 rules found

The matched rules
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
[+] looking into client #3 (Company-3)
[+] A total of 260 rules found

The matched rules
----------------------------------------------------------------------------------------------------
User Login from Different Countries Within 3 Hours [DEV]
----------------------------------------------------------------------------------------------------
[+] looking into client #4 (Company-4)
[+] A total of 335 rules found

The matched rules
----------------------------------------------------------------------------------------------------
[DEV] User Login from Different Countries Within 3 Hours
----------------------------------------------------------------------------------------------------

Choose the action:
1) Select Rules         2) List Selected Rules
3) Update Rules         4) Rules Comparison/Assessment
5) Create Rules         6) help

>>> 2

The selected rules
----------------------------------------------------------------------------------------------------
Company-3               42718c04-51b3-4b7f-8511-0c19252ea44b    User Login from Different Countries Within 3 Hours [DEV]      
Company-4               80255886-e3b8-495e-88d3-05f1c571aada    [DEV] User Login from Different Countries Within 3 Hours      
----------------------------------------------------------------------------------------------------

Choose the action:
1) Select Rules         2) List Selected Rules
3) Update Rules         4) Rules Comparison/Assessment
5) Create Rules         6) help

>>> 3

Choose the update method : 
1) Update from an Existing Rule                 2) from a JSON file
3) Manually

>>> 1
rule ID >>> 42718c04-51b3-4b7f-8511-0c19252ea44b
Are you sure you want to update all the selected rules with this one [Y/n] ? Y
Copying The rule from Company-3
Updating the rule on Company-4 rule

Choose the action:
1) Select Rules         2) List Selected Rules
3) Update Rules         4) Rules Comparison/Assessment
5) Create Rules         6) help
```
In the same way, you can create the rules if they are missing in the other tenants using the 5th option. 

And finally if you wanted to compare the existence of analytic rules across different selected tenants
```
>>> 4   

1) Exporting into an excel sheet

>>> 1
[+] dumping the client #1 (Company-1) rules
[+] A total of 1 rules found
[+] dumping the client #2 (Company-2) rules
[+] A total of 302 rules found
[+] dumping the client #3 (Company-3) rules
[+] A total of 260 rules found
[+] dumping the client #4 (Company-4) rules
[+] A total of 335 rules found
[+] Excel file created successfully.

Choose the action:
1) Select Rules         2) List Selected Rules
3) Update Rules         4) Rules Comparison/Assessment
5) Create Rules         6) help
```
this will generate an excel sheet named comparison.xlsx as shown below

<img width="70%" alt="image" src="https://github.com/o54ma-4l5h4r1f/Sentinel-Analytic-Rules-Mgm/assets/90612145/1e5b8b39-e579-4d70-a14e-eaf759c6ca39">

You can keep going and discovere new featues from here.
Good luck ^^ 
