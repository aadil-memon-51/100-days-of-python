#Nesting list,dictionary in a dictionary
# travel_log={
#     "France":["Paris","Lille","Dijon"],#list nested in dictionary
#     "France2":{"city_visited":["Paris","Lille","Dijon"]} #list nested in a dictionary and dictionary nested in a dictionary
# }
# # Nesting dictionary in a list
# travel_log=[
#     {
#         "country: ":"France2",
#         "city_visited":["Paris","Lille","Dijon"]
#     }
# ]
#day9_2
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(val1,val2,val3):
    travel_log.append(
        {
        "country":val1,
        "visits":val2,
        "cities":val3
        })
add_new_country(val1="Russia", val2=2, val3=["Moscow", "Saint Petersburg"])
print(travel_log)