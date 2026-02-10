# wright a program to fill in a letter tamplet given below with name and date .
letter ='''dear name <|name|>,
         you are selected !
         <|date|>'''
print(letter.replace("<|name|>","pratap").replace("<|date|>","24 july 2024"))

# new example
letter ='''dear name <|name|>, 
         you are selected !
        <|date|>'''
print(letter.replace("<|name|>","batman").replace("<|date|>","15 september 2025"))

# new example
letter ='''dear name <|name|>, 
         you are selected on !
         <|date|>'''
print(letter.replace("<|name|>","supeerman").replace("<|date|>","1 january 2026"))


# new example 
letter ='''dear name <|name|>, 
         you are selected on !
         <|date|>'''
print(letter.replace("<|name|>","ironman").replace("<|date|>","10 january 2026"))