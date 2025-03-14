medical_cause = input("Enter if you have a medical cause Y for yes and N for no")
attendance = int(input("Enter your attendance:"))
if medical_cause == "Y":
    print("Allowed")
else:
    if attendance > 75:
        print("allowed")
    else:
        print("not allowed")