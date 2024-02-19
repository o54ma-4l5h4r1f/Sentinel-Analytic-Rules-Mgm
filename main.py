# import argparse
from azure.identity import DefaultAzureCredential
from azure.mgmt.securityinsight import SecurityInsights
from Colors import color
import subprocess
import json
import warnings
import uuid

# Suppress all deprecation warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)
warnings.simplefilter(action='ignore', category=SyntaxWarning)

def banner():
    print("""
      ___           ___           ___       ___           ___     
     /\  \         /\__\         /\__\     /\  \         /\  \    
    /::\  \       /:/  /        /:/  /    /::\  \       /::\  \   
   /:/\:\  \     /:/  /        /:/  /    /:/\:\  \     /:/\ \  \  
  /::\~\:\  \   /:/  /  ___   /:/  /    /::\~\:\  \   _\:\~\ \  \ 
 /:/\:\ \:\__\ /:/__/  /\__\ /:/__/    /:/\:\ \:\__\ /\ \:\ \ \__\\
 \/_|::\/:/  / \:\  \ /:/  / \:\  \    \:\~\:\ \/__/ \:\ \:\ \/__/
    |:|::/  /   \:\  /:/  /   \:\  \    \:\ \:\__\    \:\ \:\__\  
    |:|\/__/     \:\/:/  /     \:\  \    \:\ \/__/     \:\/:/  /  
    |:|  |        \::/  /       \:\__\    \:\__\        \::/  /   
     \|__|         \/__/         \/__/     \/__/         \/__/     \n
          
    """ + color['white'] + """Welcome to the Analytic Rules Management & Assessment tool \n\n""" + color['off'])

def Help():
    pass

def Tenants():
    print("""
Please select the associated tenants (comma separated):
""")

# Global variables
#================================================
credential = None
tenants = []
tenants_nums = []
selected_tenants_names = []
clients = []
subscription_ids = []
workspace_names = []
resource_group_names = []
rules = []
selected_rules = []
all_uniqe_rules = []
rules_per_tenant = {}
#================================================

def AreYouSure():
    while True:
        try:
            print("Are you sure you wnat to exit [Y/n] ", end="")
            VerifyInput = input().upper()
            if VerifyInput == "Y" or VerifyInput == "YES":
                print("Bye")
                exit(0)
            else:
                break
        except KeyboardInterrupt:
                print()
                continue    

def GetInput(Range, YN=False, text="\n>>> "):
    while True:
        try:
            if YN:
                Input = input()
            else:
                Input = input(color['white'] + text + color['off'])
                if Input == "":
                    continue

                if Input.lower() == "exit" or Input.lower() == "q":
                    AreYouSure()
                    continue
                
                if not Input.isdigit():
                    print(color['darkred'] + "Not a valid option" + color['off'])
                    continue

                if Input.isdigit() and int(Input) not in range(1, Range+1):
                    print(color['darkred'] + "Not a valid option" + color['off'])
                    continue

            break

        except KeyboardInterrupt:
            print()
            AreYouSure()
            continue
        except ValueError:
            print(color['darkred'] + "Not a valid option" + color['off'])
            continue
        except Exception as e:
            print(e)

    return Input

def GrantAccess():
    print("""Authenticatiion setup:
          
1) Login to Azure
2) Relogin to Azure
3) Logout from Azure""")

    Login = int(GetInput(Range=3))
    if(Login == 1):
        ps_command = 'azd auth login --check-status'
        status = subprocess.run(["powershell", "-Command", ps_command], capture_output=True, text=True)
        if("Logged in to Azure." in status.stdout):
            print(color['darkyellow'] + "[+] Already Logged into Azure." + color['off'])
        else:
            ps_command = 'azd auth login'
            subprocess.run(["powershell", "-Command", ps_command], capture_output=True, text=True)
            print(color['darkyellow'] + '[+] Logged into Azure.' + color['off'])

    elif(Login == 2):
        print(color['darkyellow'] + "[+] Relogging into Azure." + color['off'])
        ps_command = 'azd auth logout'
        subprocess.run(["powershell", "-Command", ps_command], capture_output=True, text=True)
        ps_command = 'azd auth login'
        subprocess.run(["powershell", "-Command", ps_command], capture_output=True, text=True)
        print(color['darkyellow'] + "[+] Logged into Azure." + color['off'])

    elif(Login == 3):
        print(color['darkyellow'] + "[+] Logging out from Azure." + color['off'])
        ps_command = 'azd auth logout'
        subprocess.run(["powershell", "-Command", ps_command], capture_output=True, text=True)
        exit(0)

def PaseRange():
    pass

def SelectTenants():
    i = 1
    print(color['white'] + "\nWhich tenants workspaces are you going to work on:" + color['off'])
    print(color['darkcyan'] + "[EX1] 1,2,3,4,5,...\n[EX2] 1-3,6-7,9,..." + color['off'])
    print(color['darkcyan'] + "[NOTE] You can update the tenants list by modifying the 'DataBase.json' file" + color['off'])
    global subscription_ids, workspace_names, resource_group_names, clients,tenants_nums, credential, tenants, tenants_names
    with open('DataBase.json', 'r') as file:
        tenants = json.load(file)
        for key, value in tenants.items():
            if i <= 9:
                space = " "
            else:
                space = ""

            if(len(value["tenant_name"]) > 9):
                print(key + space + ") " + value["tenant_name"] + "\t", end="")
            else:
                print(key + space + ") " + value["tenant_name"] + "\t\t", end="")
            
            if i % 3 == 0 and i != 0:
                print("")
            i += 1

        while True:
            try:
                Inputs = input("\n>>> ").replace(" ", "")
                if Inputs == "":
                    continue

                if Inputs.lower() == "exit" or Inputs.lower() == "q":
                    AreYouSure()
                    continue

                Inputs = Inputs.split(",") 
                tmp = []
                for I in Inputs:
                    if "-" in I:
                        start, end = map(int, I.split("-")) 
                        tmp.append(",".join(map(str,list(range(start, end + 1)))))
                    else:
                        tmp.append(I)

                Inputs = set(map(int, ",".join(tmp).split(',')))
                out = 0
                for I in Inputs:
                    if int(I) not in range(1, i):
                        print(color['darkred'] + "Not a valid option" + color['off'])
                        out = 1
                        break
                if out:
                    continue

                Inputs = ",".join(map(str,Inputs))
                color['yellow'] + f"[+] The selected list of tenants : {Inputs}"  + color['off'] 
                print(color['yellow'] + f"[+] The selected tenants : {Inputs}" + color['off'])
                Inputs = tenants_nums = Inputs.split(",")
                break

            except KeyboardInterrupt:
                print()
                AreYouSure()
                continue
            except ValueError:
                print(color['darkred'] + "Not a valid option" + color['off'])
                continue
            except Exception as e:
                print(e)

        credential = DefaultAzureCredential()
        for Input in Inputs:
            subscription_id = tenants[Input]["subscription_id"]
            subscription_ids.append(tenants[Input]["subscription_id"])
            resource_group_names.append(tenants[Input]["resource_group_name"])
            workspace_names.append(tenants[Input]["workspace_name"])

            clients.append(SecurityInsights(credential, subscription_id))

def ExportRules():
    print("""
1) Exporting into an excel sheet""")
    Input = GetInput(Range=1)
    if Input == "1":
        import pandas as pd
        import re
        pattern_to_delete = r'((\s*)?(-)?(\s*)?\[((\s*)?wc(\s*)?|(\s*)?wb(\s*)?|(\s*)?dev(\s*)?)(\s*)?(-)?(\s*)?.*\](\s*)?)' # r'((\s+)?(-)?(\s+)?\[(wc)?(wb)?(dev)?(\s+)?(-)?(\s+)?.+\](\s+)?)'
        global workspace_names, resource_group_names, clients, tenants, selected_tenants_names, all_uniqe_rules 
        
        rules_per_tenant = {}
        all_uniqe_rules = set()
        for i in range(len(clients)):
            rules_names = []
            selected_tenants_names.append(tenants[str(tenants_nums[i])]['tenant_name'])
            print(color['yellow'] + f"[+] dumping the client #{tenants_nums[i]} ({tenants[str(tenants_nums[i])]['tenant_name']}) rules" + color['off'])
            tmp_rules = list(clients[i].alert_rules.list(resource_group_names[i], workspace_names[i]))
            print(color['darkyellow'] + f"[+] A total of {len(tmp_rules)} rules found" + color['off'])

            
            for tmp in tmp_rules:
                name = tmp.display_name
                name = name.rstrip()
                modified_string = re.sub(pattern_to_delete, '', name.lower())
                # print(modified_string)
                rules_names.append(modified_string)

            all_uniqe_rules.update(rules_names)
            rules_per_tenant[tenants[str(tenants_nums[i])]['tenant_name']] = rules_names

        dict_to_excel = {
            "Rules/Tenants" : selected_tenants_names
        }
        
        for rule in all_uniqe_rules:
            row_per_rule = []
            for name in selected_tenants_names:
                if rule in rules_per_tenant[name]: # it could be bettwe to use (in) instead of (==)
                    row_per_rule.append("✓")
                else:
                    row_per_rule.append("✘")

            dict_to_excel[rule] = row_per_rule

        df = pd.DataFrame(dict_to_excel)
        df_transposed = df.T
        df_transposed.to_excel('comparison.xlsx', header=False, index=True)
        print(color['yellow'] + "[+] Excel file created successfully." + color['off'])

def SelectRules():
    print("""
1) Select Rules By Name""")
# 3) Select By kind         4) Select By Sevirity
# 5) Select By Tag
    
    Input = GetInput(Range=1)
    if Input == "1":
        Filter = input(color['white'] + "Rule Name (or part of it) > "  + color['off']) # or multiple ones !
        # Case Sensitive !! 
    global workspace_names, resource_group_names, clients, rules, tenants, selected_rules, rules_per_tenant
    selected_rules = []
    for i in range(len(clients)):
        rules = []
        TenantName = tenants[str(tenants_nums[i])]['tenant_name']
        print(color['yellow'] + f"[+] looking into client #{tenants_nums[i]} ({TenantName})"  + color['off'])
        tmp_rules = list(clients[i].alert_rules.list(resource_group_names[i], workspace_names[i]))
        print(color['darkyellow'] + f"[+] A total of {len(tmp_rules)} rules found" + color['off'])
        if Input == "1":
            count = 0
            rules_per_tenant[TenantName] = []
            for rule in tmp_rules:
                if hasattr(rule, 'display_name') and Filter in rule.display_name:
                    rules.append(rule)
                    selected_rules.append(
                        {
                            "tenant" : TenantName,
                            "name": rule.name,
                            "id": rule.id,
                            "display_name" : rule.display_name,
                            "idx" : i
                            # "resource_group_name" :resource_group_names[i], 
                            # "workspace_name" : workspace_names[i],
                            # "client" : clients[i]
                        }
                    )
                    count += 1
                    rules_per_tenant[TenantName].append(rule.display_name)

            print(color['white'] + "\nThe matched rules" + color['off'])
            print("-"*100)
            for r in rules:
                print(color['darkcyan'] + r.display_name + color['off'])
            print("-"*100)   

def ListRules():
    global selected_rules
    print(color['white'] + "\nThe selected rules" + color['off'])
    print("-"*100)
    for sr in selected_rules:
        if(len(sr['tenant']) > 9):
            print(f"{sr['tenant']}\t{color['darkcyan'] + sr['name'] + color['off']}\t{sr['display_name']}")
        else:
            print(f"{sr['tenant']}\t\t{color['darkcyan'] + sr['name'] + color['off']}\t{sr['display_name']}")
    print("-"*100)

def CopyPaste():
    global workspace_names, resource_group_names, clients, rules, tenants, selected_rules, tenants_nums
    InputID = input(color['white'] + "rule ID >>> " + color['off'])
    print("Are you sure you want to update all the selected rules with this one [Y/n] ? ", end="")
    # updating !!!!
    VerifyInput = GetInput(Range=0, YN=True).upper()
    if VerifyInput == "Y" or VerifyInput == "YES":
        MasterRule = None
        flag = 0

        if len(tenants_nums) == 1: # or len(selected_rules) == 1:
            print(color['yellow'] + f"There must be 2 or more selected tenants for this option to work" + color['off'])
        
        else:
            for sr in selected_rules:
                if sr["name"] == InputID:
                    print(color['yellow'] + f"Copying The rule from {sr['tenant']}" + color['off'])
                    MasterRule = clients[sr["idx"]].alert_rules.get(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], InputID)
                    flag = 1
                    SSMasterRule = MasterRule.serialize()
                    SSMasterRule.pop('etag') # important !! 
                    break

            if flag:
                for sr in selected_rules:
                    if sr["name"] != InputID:    
                        print(color['darkyellow'] + f"Updating the rule on {sr['tenant']} rule" + color['off'])
                        clients[sr["idx"]].alert_rules.create_or_update(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr['name'], SSMasterRule)
            else:
                print(color['red'] + "[!] The analytic rule not found" + color['off'])

def ManualUpdate():
    print(color['white'] + """
What to update : """  + color['off'] + """
1) Enable               2) Disable              3) Display Name         
4) Description          5) Severity             6) KQL Query""")
    global workspace_names, resource_group_names, clients, rules, tenants, selected_rules
    Input = input(color['white'] + "\n>>> " + color['off'])
    if Input == "1":
        print("Are you sure you want to enable all the selected rules [Y/n] ? ", end="")
        # updating !!!!
        VerifyInput = GetInput(Range=0, YN=True).upper()
        if VerifyInput == "Y" or VerifyInput == "YES":
            for sr in selected_rules:
                print(f"Enabling the rule ({sr['name']})")
                MasterRule = clients[sr["idx"]].alert_rules.get(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr["name"])
                MasterRule.enabled = True
                clients[sr["idx"]].alert_rules.create_or_update(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr['name'], MasterRule)
        
    elif Input == "2":
        print("Are you sure you want to disable all the selected rules [Y/n] ? ", end="")
        # updating !!!!
        VerifyInput = GetInput(Range=0, YN=True).upper()
        if VerifyInput == "Y" or VerifyInput == "YES":
            for sr in selected_rules:
                print(f"Disabling the rule ({sr['name']})")
                MasterRule = clients[sr["idx"]].alert_rules.get(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr["name"])
                MasterRule.enabled = False
                clients[sr["idx"]].alert_rules.create_or_update(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr['name'], MasterRule)

    elif Input == "3":
        print(color['white'] + """
Choose an option : """  + color['off'] + """
1) All Whole Name       2) Add Prefix           3) Add Suffix         
4) Remove Prefix        5) Remove Suffix        """)
        
        Input = GetInput(Range=5)
        
        if Input == "1":
            print(color['darkyellow'] + f"[+] NOTE : Write the name between double quotations \"...\"" + color['off'])
            NewName = input(color['white'] + "Write the new disblay name : " + color['off']).strip()[1:-1]
            print("Are you sure you want to change the display name for all the selected rules [Y/n] ? ", end="")
            # updating !!!!
            VerifyInput = GetInput(Range=0, YN=True).upper()
            if VerifyInput == "Y" or VerifyInput == "YES":
                for sr in selected_rules:
                    print(f"Updating the rule ({sr['name']})")
                    MasterRule = clients[sr["idx"]].alert_rules.get(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr["name"])
                    MasterRule.display_name = NewName
                    clients[sr["idx"]].alert_rules.create_or_update(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr['name'], MasterRule)
        
        elif Input == "2":
            print(color['darkyellow'] + f"[+] NOTE : Write the prefix between double quotations \"...\"" + color['off'])
            print(color['darkyellow'] + f"[+] NOTE : you may need to add a space after the prefix" + color['off'])
            NewPrefix = input(color['white'] + "Write the prefix : " + color['off']).strip()[1:-1]
            print("Are you sure you want to change the display name for all the selected rules [Y/n] ? ", end="")
            # updating !!!!
            VerifyInput = GetInput(Range=0, YN=True).upper()
            if VerifyInput == "Y" or VerifyInput == "YES":
                for sr in selected_rules:
                    print(f"Updating the rule ({sr['name']})")
                    MasterRule = clients[sr["idx"]].alert_rules.get(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr["name"])
                    MasterRule.display_name = NewPrefix + MasterRule.display_name
                    clients[sr["idx"]].alert_rules.create_or_update(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr['name'], MasterRule)

        elif Input == "3":
            print(color['darkyellow'] + f"[+] NOTE : Write the suffix between double quotations \"...\"" + color['off'])
            print(color['darkyellow'] + f"[+] NOTE : you may need to add a space before the suffix" + color['off'])
            NewSuffix = input(color['white'] + "Write the suffix : " + color['off']).strip()[1:-1]
            print("Are you sure you want to change the display name for all the selected rules [Y/n] ? ", end="")
            # updating !!!!
            VerifyInput = GetInput(Range=0, YN=True).upper()
            if VerifyInput == "Y" or VerifyInput == "YES":
                for sr in selected_rules:
                    print(f"Updating the rule ({sr['name']})")
                    MasterRule = clients[sr["idx"]].alert_rules.get(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr["name"])
                    MasterRule.display_name = MasterRule.display_name + NewSuffix
                    clients[sr["idx"]].alert_rules.create_or_update(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr['name'], MasterRule)

        elif Input == "4":
            print(color['darkyellow'] + f"[+] NOTE : Write the prefix between double quotations \"...\"" + color['off'])
            print(color['darkyellow'] + f"[+] NOTE : you may need to include the spaces around the prefix" + color['off'])
            Prefix = input(color['white'] + "Write the prefix : " + color['off']).strip()[1:-1]
            print("Are you sure you want to change the display name for all the selected rules [Y/n] ? ", end="")
            # updating !!!!
            VerifyInput = GetInput(Range=0, YN=True).upper()
            if VerifyInput == "Y" or VerifyInput == "YES":
                for sr in selected_rules:
                    print(f"Updating the rule ({sr['name']})")
                    MasterRule = clients[sr["idx"]].alert_rules.get(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr["name"])
                    if MasterRule.display_name.startswith(Prefix):
                        MasterRule.display_name = MasterRule.display_name[len(Prefix):]
                        clients[sr["idx"]].alert_rules.create_or_update(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr['name'], MasterRule)
                    else:
                        print(color['red'] + "[!] Prefix not found" + color['off'])
                    
        elif Input == "5":
            print(color['darkyellow'] + f"[+] NOTE : Write the suffix between double quotations \"...\"" + color['off'])
            print(color['darkyellow'] + f"[+] NOTE : you may need to include the spaces around the suffix" + color['off'])
            Suffix = input(color['white'] + "Write the suffix : " + color['off']).strip()[1:-1]
            print("Are you sure you want to change the display name for all the selected rules [Y/n] ? ", end="")
            # updating !!!!
            VerifyInput = GetInput(Range=0, YN=True).upper()
            if VerifyInput == "Y" or VerifyInput == "YES":
                for sr in selected_rules:
                    print(f"Updating the rule ({sr['name']})")
                    MasterRule = clients[sr["idx"]].alert_rules.get(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr["name"])
                    if MasterRule.display_name.endswith(Suffix):
                        MasterRule.display_name = MasterRule.display_name[:-len(Suffix)]
                        clients[sr["idx"]].alert_rules.create_or_update(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr['name'], MasterRule)
                    else:
                        print(color['red'] + "[!] Suffix not found" + color['off'])
        
    elif Input == "4":
        NewName = input(color['white'] + "Write the new description : " + color['off'])
        print("Are you sure you want to change the description for all the selected rules [Y/n] ? ", end="")
        # updating !!!!
        VerifyInput = GetInput(Range=0, YN=True).upper()
        if VerifyInput == "Y" or VerifyInput == "YES":
            for sr in selected_rules:
                print(f"Updating the rule ({sr['name']})")
                MasterRule = clients[sr["idx"]].alert_rules.get(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr["name"])
                MasterRule.description = NewName
                clients[sr["idx"]].alert_rules.create_or_update(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr['name'], MasterRule)

    elif Input == "5":
        print(color['white'] + """
Choose the severity: """  + color['off'] + """
1) Informational               2) Low              3) Medium         4) High""")    
        SeveritySet = ["Informational", "Low", "Medium", "High"]
        Severity = SeveritySet[int(input(color['white'] + "\n>>> " + color['off']).rstrip())-1]
        print("Are you sure you want to change the Severity for all the selected rules [Y/n] ? ", end="")
        # updating !!!!
        VerifyInput = GetInput(Range=0, YN=True).upper()
        if VerifyInput == "Y" or VerifyInput == "YES":
            for sr in selected_rules:
                print(f"Updating the rule ({sr['name']})")
                MasterRule = clients[sr["idx"]].alert_rules.get(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr["name"])
                MasterRule.severity = Severity
                clients[sr["idx"]].alert_rules.create_or_update(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr['name'], MasterRule)

    elif Input == "6":
        NewName = input(color['white'] + "Update the NewKQL file content [press Enter when you're done] " + color['off'])
        NewQuery = open("NewKQL", "r").read()
        print("Are you sure you want to change the KQL query for all the selected rules [Y/n] ? ", end="")
        # updating !!!!
        VerifyInput = GetInput(Range=0, YN=True).upper()
        if VerifyInput == "Y" or VerifyInput == "YES":
            for sr in selected_rules:
                print(f"Updating the rule ({sr['name']})")
                MasterRule = clients[sr["idx"]].alert_rules.get(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr["name"])
                MasterRule.query = NewQuery
                clients[sr["idx"]].alert_rules.create_or_update(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], sr['name'], MasterRule)

def JsonUpdate():
    print(color['red'] + "[!] This feature not enable yet" + color['off'])

def CopyPaste2():
    global workspace_names, resource_group_names, clients, rules, tenants, selected_rules, tenants_nums, rules_per_tenant
    InputID = input(color['white'] + "rule ID >>> " + color['off'])
    print("Are you sure you want to create the missing rules on other tenants from the selected one [Y/n] ? ", end="")
    # updating !!!!
    VerifyInput = GetInput(Range=0, YN=True).upper()
    if VerifyInput == "Y" or VerifyInput == "YES":
        MasterRule = None
        flag = 0

        if len(tenants_nums) == 1: # or len(selected_rules) == 1:
            print(color['yellow'] + f"There must be 2 or more selected tenants for this option to work" + color['off'])
        
        else:
            for sr in selected_rules:
                if sr["name"] == InputID:
                    print(color['yellow'] + f"Copying The rule from {sr['tenant']}" + color['off'])
                    MasterRule = clients[sr["idx"]].alert_rules.get(resource_group_names[sr["idx"]], workspace_names[sr["idx"]], InputID)
                    flag = 1
                    selected_rule_display_name = MasterRule.display_name
                    selected_rule_tenant = sr["tenant"]
                    SSMasterRule = MasterRule.serialize()
                    SSMasterRule.pop('etag') # important !! 
                    break

            if flag:
                for i in range(len(clients)):
                    TenantName = tenants[str(tenants_nums[i])]['tenant_name']
                    if selected_rule_tenant != TenantName:
                        if selected_rule_display_name in rules_per_tenant[TenantName]:
                            print(color['red'] + f"[!] The analytic rule already exist in the tenant #{tenants_nums[i]} ({TenantName})" + color['off'])
                        else:
                            print(color['darkyellow'] + f"[+] Creating a new rule into the tenant #{tenants_nums[i]} ({TenantName})"  + color['off'])
                            new_id =  str(uuid.uuid4())
                            print(color['darkyellow'] + f"[+] The new rule ID = {new_id}"  + color['off'])
                            clients[i].alert_rules.create_or_update(resource_group_names[i], workspace_names[i], new_id, SSMasterRule)
            else:
                print(color['red'] + "[!] The analytic rule not found" + color['off'])

def UpdateRules():
    global workspace_names, resource_group_names, clients, rules, tenants
    print(color['white'] + '''
Choose the update method : ''' + color['off'] + '''
1) Update from an Existing Rule                 2) from a JSON file      
3) Manually''')
    
    Input = GetInput(Range=3)
    if Input == "1":
        CopyPaste()
    elif Input == "2":
        JsonUpdate()
    elif Input == "3":
        ManualUpdate()

def CreateRules():
    global workspace_names, resource_group_names, clients, rules, tenants
    print(color['white'] + '''
Choose the creation method : ''' + color['off'] + '''
1) Create from an Existing Rule''')
    
    Input = GetInput(Range=1)
    if Input == "1":
        CopyPaste2()

def Actions():
    print(color['darkcyan'] + '''
Choose the action: ''' + color['off'] + '''    
1) Select Rules         2) List Selected Rules
3) Update Rules         4) Rules Comparison/Assessment    
5) Create Rules         6) help''')
    
    Inputs = GetInput(Range=6)
    match Inputs:
        case '1':
            SelectRules()
        case '2':
            ListRules()
        case '3':
            UpdateRules()
        case '4':
            ExportRules()
        case '5':
            CreateRules()
        case _:
            Help()

def main():

    try:
        banner()
        GrantAccess()
        SelectTenants()
        while True:
            try:
                Actions()
            except KeyboardInterrupt:
                continue

    except KeyboardInterrupt:
        print("\nBye")
    except Exception as e:
        print(f"{e}")
    
if __name__ == "__main__":
    main()
