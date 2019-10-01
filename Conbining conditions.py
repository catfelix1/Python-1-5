country = input("What is your country ").lower()
total = float(input("What is your total "))
grandtotal = total
if country == "canada" :
    province = input("What province are you from ")
if not country == "canada" : total = total and print("You have no tax for your country")
if country == "canada" and province == "alberta" :
        grandtotal = (total*1.05)
        print(grandtotal)
if country == "canada" and (province == "ontario" or province == "new brunswick" \
        or province == "nova scotia") :
        grandtotal = (total*1.13)
        print(grandtotal)
if country == "canada" and (province == "british cloumbia" or province == "saskatchwan" \
   or province == "prince edward island" or province == "nunavut" or province == "youkon" \
   or province == "north west territories" \
   or province == "newfoundland laboudor" or province == "manatobia" or province == "quebec") :
   grandtotal = (total*1.11) 
print(grandtotal)





