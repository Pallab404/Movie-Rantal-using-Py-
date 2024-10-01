
import catalog
import rentals 
import earnings


catalog.addMovie("avatar","action",120)
catalog.addMovie("uri","action",120)
catalog.availableMovies()
# addUser(u_details,"Pallab")
# addUser(u_details,"John")
rentals.rentMovie(catalog.m_list,"avatar","Pallab")
rentals.rentMovie(catalog.m_list,"uri","Pallab")
rentals.displayRentedMovies()
earnings.rentalEaring(rentals.rented_movie_list)