customerinfo = [
    {
        "name": "Shaan",
        "age": 28,
        "email": "qamar@datavalley.com",
        "sex": "male",
        "Address":[
            {
                "street": "bla bla 1",
                "city": "Lahore",
                "state": "Punjab",
                "zip": "54000"
            },
            {
                "street": "bla bla 2",
                "city": "Karachi",
                "state": "Sindh",
                "zip": "74000"
            },
            {
                "street": "bla bla 3",
                "city": "Islamabad",
                "state": "ICT",
                "zip": "44000"
            }
        ]
    

    },

    {
        "name": "Tara",
        "age": 23,
        "email": "tara@datavalley.com",
        "sex": "female",
        "Address":[
            {
                "street": "bla bla 1",
                "city": "Lahore",
                "state": "Ap",
                "zip": "500041"
            },
            {
                "street": "bla bla 2",
                "city": "Kakinada",
                "state": "Ap",
                "zip": "500048"
            },
            {
                "street": "bla bla 3",
                "city": "Islamabad",
                "state": "ICT",
                "zip": "450001"
            }
        ]
    }
]

print(customerinfo[0]["Address"][1]["city"])
print(customerinfo[1]["Address"][0]["city"])