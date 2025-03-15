
### **1. Extract All Product Names**

import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = r"(\d+\.\n)(.+)"  # Matches numbered product lines
matches = re.findall(pattern, text)

product_names = [match[1].strip() for match in matches]
print(product_names)

# ✅ **Finds all product names from the receipt.**



### **2. Extract All Prices**

pattern = r"(\d{1,3}(?: \d{3})*,\d{2})"  # Matches formatted prices

prices = re.findall(pattern, text)
print(prices)

# ✅ **Finds all product prices, including thousands separators.**



### **3. Extract Only RX (Prescription) Items**

pattern = r"\[RX\]-(.+)"
rx_items = re.findall(pattern, text)
print(rx_items)

# ✅ **Finds all items labeled as `[RX]`.**



### **4. Extract Date and Time of the Purchase**

pattern = r"Время:\s([\d.]+\s[\d:]+)"
datetime_match = re.search(pattern, text)

if datetime_match:
    print(datetime_match.group(1))

# ✅ **Extracts date and time from the receipt.**



### **5. Extract Store Name and Address**

store_pattern = r"Филиал\s(.+)"
address_pattern = r"г\.\s(.+),(.+)"

store_match = re.search(store_pattern, text)
address_match = re.search(address_pattern, text)

if store_match:
    print("Store:", store_match.group(1))
if address_match:
    print("City:", address_match.group(1).strip())
    print("Address:", address_match.group(2).strip())

# ✅ **Finds store name, city, and address.**



### **6. Extract the Total Amount Paid**

pattern = r"ИТОГО:\s([\d\s,]+)"
total_match = re.search(pattern, text)

if total_match:
    print("Total:", total_match.group(1).strip())

# ✅ **Finds the total amount paid.**



### **7. Extract Cashier Name or ID**

pattern = r"Кассир\s(.+)"
cashier_match = re.search(pattern, text)

if cashier_match:
    print("Cashier:", cashier_match.group(1).strip())

# ✅ **Extracts cashier information.**



### **8. Extract the VAT (НДС) Amount**

pattern = r"в т\.ч\. НДС 12%:\s([\d,]+)"
vat_match = re.search(pattern, text)

if vat_match:
    print("VAT Amount:", vat_match.group(1).strip())

# ✅ **Finds VAT amount.**



### **9. Extract Only Medical Items (Containing 'мл', 'табл', 'амп', 'р-р')**

pattern = r"(.+?(?:мл|табл|амп|р-р).+)"
medical_items = re.findall(pattern, text)
print(medical_items)

# ✅ **Finds all medical products.**



### **10. Find All Items with Quantities More Than 1**

pattern = r"(\d+\.\n)(.+)\n(\d+,\d+)\sx"
matches = re.findall(pattern, text)

multiple_items = [match[1].strip() for match in matches if float(match[2].replace(",", ".")) > 1]
print(multiple_items)

# ✅ **Finds all products with quantity greater than 1.**



### **11. Extract Payment Method (Card or Cash)**

pattern = r"(Банковская карта|Наличные):\s([\d\s,]+)"
payment_match = re.search(pattern, text)

if payment_match:
    print(f"Payment Method: {payment_match.group(1)} - {payment_match.group(2).strip()}")

# ✅ **Identifies if the payment was made via card or cash.**



### **12. Extract the Fiscal Code**

pattern = r"Фискальный признак:\s(\d+)"
fiscal_match = re.search(pattern, text)

if fiscal_match:
    print("Fiscal Code:", fiscal_match.group(1))

# ✅ **Finds the fiscal code from the receipt.**



### **13. Extract All Item Serial Numbers**

pattern = r"№\s(\d+)"
serial_numbers = re.findall(pattern, text)
print(serial_numbers)

# ✅ **Finds all serial numbers from the receipt.**


### **14. Extract Store’s Website or Check Verification Link**

pattern = r"(https?://[^\s]+)"
links = re.findall(pattern, text)
print(links)

# ✅ **Finds any website or verification link mentioned in the receipt.



### **15. Extract the Receipt Number**

pattern = r"Чек\s№(\d+)"
receipt_match = re.search(pattern, text)

if receipt_match:
    print("Receipt Number:", receipt_match.group(1))

# ✅ **Extracts the receipt number.**


### **Final Notes**
