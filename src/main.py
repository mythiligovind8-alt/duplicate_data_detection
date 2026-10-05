import pandas as pd
data=pd.read_csv("data/input_data.csv")
#clean the data
data["name"]=data["name"].str.strip().str.lower()
data["email"]=data["email"].str.strip().str.lower()
data["city"]=data["city"].str.strip().str.lower()
duplicates=data[data.duplicated(subset=["name","email","phone","city"],keep=False)]
print("\n======EXACT DUPLICATES=====")
print(duplicates)
print("Number of Duplicate Records:",len(duplicates))

#missing values
missing_values=data.isnull().sum()
print("\n=====MISSING VALUES=====")
print(missing_values)
#total records
total_records=len(data)
#exact duplicate records
duplicates=data[data.duplicated(subset=["name","email","phone","city"],keep=False)]
duplicate_count=len(duplicates)
#detect duplicate emails
email_duplicates=data[data.duplicated("email",keep=False)]
print("\n======DUPLICATE EMAIL RECORDS====")
print(email_duplicates)
print("Number OF Duplicate Email Records:",len(email_duplicates))
# detect duplicate phone 
phone_duplicates=data[data.duplicated("phone",keep=False)]
print("\n=====DUPLICATE PHONE RECORDS:")
print(phone_duplicates)
print("Number of Duplicate phone Records:",len(phone_duplicates)) #unique records
unique_count=total_records - duplicate_count
print("=====DUPLICATE DATA DETECTION=====")
print("Total Records:",total_records)
print("Exact Duplicate Records:",duplicate_count)
print("Unique Records:",unique_count)
#email_duplicates
print("\n=====DUPLICATE EMAILS=====")
email_duplicates=data[data.duplicated("email",keep=False)]
print(email_duplicates)
#duplicate phn no
print("\n=====DUPLICATE PHONES=====")
phone_duplicates=data[data.duplicated("phone",keep=False)]
print(phone_duplicates)
#summary of email and phn
total_records=len(data)
exact_duplicates=data[data.duplicated(keep=False)]
duplicate_count=len(exact_duplicates)
print("\n=====DUPLICATE SUMMARY=====")
print("Total Records:",total_records)
print("Duplicate Records:",duplicate_count)
#remove exact duplicate records
cleaned_data=data.drop_duplicates(subset=["name","email","phone","city"],keep="first")
print("\n=====CLEANED DATA=====")
print(cleaned_data)
print("\nOringinal Records",len(data))
print("Cleaned Records:",len(cleaned_data))
#save duplicate data to reports and cleaned data
duplicates.to_csv("reports/duplicate_records.csv",index=False)
print("\nduplicate report saved succesfully!")
cleaned_data.to_csv("reports/cleaned_data.csv",index=False)
print("\nCleaned data saved successfully!")
#data summary
print("\n=====DATA QUALITY SUMMARY=====:")
print("total Records:",len(data))
print("Cleaned Records:",len(cleaned_data))
print("Duplicate Records:",len(duplicates))
print("Record removed:",len(data)-len(cleaned_data))
#missing values
missing_values=data.isnull().sum()
print("\n=====MISSING VALUES=====")
print(missing_values)
#validate email
invalid_emails=data[~data["email"].str.contains("@",na=False)]
print("\n====INVALID EMAILS====")
print(invalid_emails)
print("Invalid Email Count:",len(invalid_emails))
#validate ph no
invalid_phones=data[~data["phone"].astype(str).str.match(r"^\d{10}$",na=False)]
print("\n===INVALID PHONE NUMBERS====")
print(invalid_phones)
print("invallid Phone Count:",len(invalid_phones))
#create the final cleaned data
final_data=data.drop_duplicates(subset=["name","email","phone","city"],keep="first")
print("\n=====FINAL CLEANED DATA====")
print(final_data)


#save the final cleaned data
final_data.to_csv("reports/final_cleaned_data.csv",index=False)
print("\nFinal Cleaned data saved successfully")


#save the final duplicate data
duplicates.to_csv("reports/duplicate_records.csv",index=False)
print("Duplicate report saved sucessfully!")
#final summary
print("\n===== FINAL PROJECT SUMMARY =====")
print("Total Records:", len(data))
print("Final Cleaned Records:", len(final_data))
print("Duplicate Records:", len(duplicates))
print("Records Removed:", len(data) - len(final_data))
print("Invalid Email Count:", len(invalid_emails))
print("Invalid Phone Count:", len(invalid_phones))