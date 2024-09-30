from package.catalog_management import addMovie
from package.rentals import rentMovie
from package.earnings import rentalEaring

m_list =[]
rented_movie_list = []

u_details={}
def addUser(u_details,c_name):
    u_details["name"] = c_name
    print(f"user added : {u_details}")

def allRentalMovie(ren):
    print("displaying rented movie list :  ")
    if len(ren) != 0:
        print(ren)
    else:
        print("no one rented any movie ....")
addMovie(m_list,"HP","comedy",120)
addUser(u_details,"Pallab")
rentMovie(m_list,u_details,rented_movie_list,"HP","Pallab")
rentalEaring(m_list,rented_movie_list)
allRentalMovie(rented_movie_list)