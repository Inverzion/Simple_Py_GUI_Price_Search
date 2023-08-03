import pyautogui as pag
import sys

# User Validation
first_verification = pag.confirm(text="You have opened a file for REDACTED USER.\nIf you are USER, or have their permissions, please continue.\nIf not, please seek a supervisor for assistance.", buttons=["Continue", "Cancel"])
if first_verification == "Cancel":
    sys.exit()
else:
    user_name = pag.prompt(text="Input User Name:", title="User Validation", default="jesse")
    password = pag.password(text="Input Password:", title="User Validation", default="password", mask='*')
    users_name = "USER NAME"
    user_password = "PASSWORD01"

if user_name == users_name and password == user_password:
    sku = pag.prompt(text="Please input the SKU: ", title="REDACTED USER's Personal Price Finder", default="")
    shop = pag.confirm(text = "Select Which Site you wish to search: ", title="REDACTED USER's Personal Price Finder", buttons=['COMPANY_WEBSITE1', 'COMPANY_WEBSITE2', 'COMPANY_WEBSITE3', 'Cancel'])
    search_for = pag.confirm(text="Select which item you are searching for: ", title="REDACTED USER's Personal Price Finder", buttons=['Price', 'Cancel'])
    try:
        if shop != "Cancel" or search_for != "Cancel":
            if shop == 'COMPANY_WEBSITE1':
                snap_on_url_base = "https://shop.COMPANY_WEBSITE1.com/product/"
                url = snap_on_url_base+sku
                print("Shop Name: "+shop+"\nSKU: "+sku+"\nTest URL: "+url)
            elif shop == 'COMPANY_WEBSITE2':
                sku = sku.lower()
                mac_url_base = "https://www.COMPANY_WEBSITE2.com/products/"
                url = mac_url_base+sku
                print("Shop Name: "+shop+"\nSKU: "+sku+"\nTest URL: "+url)
            elif shop == 'COMPANY_WEBSITE3':
                sp_url_base = "https://COMPANY_WEBSITE3.com/products/"
                url = sp_url_base+sku
                print("Shop Name: "+shop+"\nSKU: "+sku+"\nTest URL: "+url)
            else:
                print("How did you mess this up?")
        else:
            pag.alert(text="This action has been canceled. Please run this file again if necessary.", title="Price Finder")
    except Exception as exc:
        print(exc)
