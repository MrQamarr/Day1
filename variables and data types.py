

 # create variable in python with different data types

string_variable_1 = "Qamar Aka shaan"
string_variable_2 = 'Qamar Aka shaan'
string_variable_3 = '''Qamar Aka shaan
                    i'm called my many names... some call me qamar and some call me qamaru and some call me mrQ and 
                    some go by Qamar Ali'''
int_variable_2 = 1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 60, 69.
float_variable_2 = 10.2, 20.3, 30, 40.5, 55.9, 69.69, 420.420
Boolean_variable = True, False

List_variables = [10, "a good heart", "Temptations", "Risk and Reward", 'Life & Death', "Supercalifragilisticexpialidocious"]

Dictionary_variables = [
    
    {
        'Name' : 'John Doe',
        'Age' : 30,
        'address' : {
            'address1':'pobox number, bla bla bi bl;a blab  blu, hitech city, bla blu',
            'address2':'pobox number, bla bla bi bl;a blab  blu, hitech city, bli blu',
            'address3':'pobox number, bla bla bi bl;a blab  blu, hitech city, blu blu'
        }

    },

    {
        'Name' : 'John roe',
        'Age' : 28,
        'address' : {
            'address1':'pobox number, blu bla bi bl;a blab  blu, hitech city, bla blu',
            'address2':'pobox number, blo bla bi bl;a blab  blu, hitech city, bli blu',
            'address3':'pobox number, bls bla bi bl;a blab  blu, hitech city, blu blu'
        }

    },



    {
        'Name' : 'John Goe',
        'Age' : 28,
        'address' : {
            'address1':'pobox number, blo bla bi bl;a blab  blu, hitech city, bla blu',
            'address2':'pobox number, blk bla bi bl;a blab  blu, hitech city, bli blu',
            'address3':'pobox number, blm bla bi bl;a blab  blu, hitech city, blu blu'
        }

    }

]

print(Dictionary_variables[2])
print(Dictionary_variables[2]['address'])
print(Dictionary_variables[2]['address']['address2'])