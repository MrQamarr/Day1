user_name = input("enter your Name:")
batch_name = "Batch LUMA"
batch_timing = "10:00 AM - 12:00 PM"
sender_name = "Data Valley"

batch_info = [
    {
        # "Student name" : "user_name",
        "Batch name" : "Batch LUMA",
        "Batch timing" : "10:00 AM - 12:00 PM"
    }
]

print(f'''
Dear {user_name},
This is a confirmation that you have been enrolled in {batch_info[0]["Batch name"]}
and the timings for the batch are from {batch_info[0]["Batch timing"]} Mon-Sat.

Please make sure you get your required accessories like laptops and required materials.
Also make sure you contact your instructor if you have any questions or concerns regarding the batch.

Best regards,
{sender_name}
''')