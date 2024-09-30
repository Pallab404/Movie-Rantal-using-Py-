
def rentalEaring(m_list,rented_movie_list):
    total_earning = 0
    for mov , r_mov in zip(m_list,rented_movie_list):
        if mov[0] == r_mov[1]:
            total_earning += mov[2]
    print(f"total rental earning is : {total_earning}")
