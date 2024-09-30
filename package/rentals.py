
def rentMovie(m_list,u_details,rented_movie_list,m_name,c_name):
    for mov in m_list:
        if mov[0] == m_name: 
            if c_name in u_details.values():
                rented_mov_lis=(c_name,m_name)
                rented_movie_list.append(rented_mov_lis)
                print(f"rent details for {c_name} : {rented_movie_list}")
            else:
                print(f"user is not registered ....")
            print(m_list)
        else:
            print(f"{m_name} is not available in the list ....")
            return