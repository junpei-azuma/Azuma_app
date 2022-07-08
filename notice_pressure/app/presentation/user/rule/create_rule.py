
schema: dict = {
    'email' : {
        'type' : 'string',
        'required': True,
        'regex': "^[a-zA-Z0-9.!#$%&'*+ \\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", 
        'empty' : False
    },
    'password' : {
        'type' : 'string',
        'required' : True,
        'regex': "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[_@\\-%&#+])[a-zA-z\\d_@\\-%&#+]{10,20}$",
        'empty' : False
    }
}