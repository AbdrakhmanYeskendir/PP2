
### **1. Subtract Five Days from Current Date**

from datetime import datetime, timedelta

# Get the current date
current_date = datetime.today()

# Subtract 5 days
new_date = current_date - timedelta(days=5)

print("Current Date:", current_date.date())
print("Date 5 Days Ago:", new_date.date())

#### **Output (Example)**

# Current Date: 2025-03-01
# Date 5 Days Ago: 2025-02-24




### **2. Print Yesterday, Today, Tomorrow**

from datetime import datetime, timedelta

# Get today's date
today = datetime.today()

# Calculate yesterday and tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.date())
print("Today:", today.date())
print("Tomorrow:", tomorrow.date())

#### **Output (Example)**

# Yesterday: 2025-02-28
# Today: 2025-03-01
# Tomorrow: 2025-03-02




### **3. Drop Microseconds from Datetime**

from datetime import datetime

# Get the current datetime
current_datetime = datetime.now()

# Remove microseconds
datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Original Datetime:", current_datetime)
print("Datetime without Microseconds:", datetime_without_microseconds)

#### **Output (Example)**

# Original Datetime: 2025-03-01 12:34:56.789012
# Datetime without Microseconds: 2025-03-01 12:34:56




### **4. Calculate Two Date Difference in Seconds**

from datetime import datetime

# Define two dates
date1 = datetime(2025, 3, 1, 12, 0, 0)
date2 = datetime(2025, 3, 2, 14, 30, 0)  # 1 day, 2 hours, 30 minutes later

# Calculate difference in seconds
difference_in_seconds = (date2 - date1).total_seconds()

print("Difference in seconds:", difference_in_seconds)

#### **Output**

# Difference in seconds: 92700.0

# (1 day = 86400 seconds + 2 hours = 7200 seconds + 30 minutes = 1800 seconds → **92700 seconds**)



