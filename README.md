<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

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

Sentinel-Analytic-Rules-Mgm is a tool designed for managing and assessing Microsoft Sentinel Analytic Rules across multiple tenants' workspaces seamlessly. This script streamlines the process of performing various actions on analytic rules while utilizing a single set of authentication credentials. Its functionality enables users to execute actions on a set of selected analytic rules, optimizing the management of them.

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
PS> winget install microsoft.azd
```

On powershell

```bash
# Clone the project
PS> git clone https://github.com/o54ma-4l5h4r1f/Sentinel-Analytic-Rules-Mgm.git

# Go to the project directory
PS> cd Sentinel-Analytic-Rules-Mgm

# Install the requirements
PS> pip install -r requirments.txt
```
And make sure to restart the powershell terminal after the installation ends

## :jack_o_lantern: Lets Run It
