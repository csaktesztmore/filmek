from osztaly import Film as Film


def construct(file, database):
    with open(file, encoding="UTF-8") as f:
        f.readline()
        for line in f:
            line = line.strip().split(";")
            title = line[0]
            title_url = line[1]
            image = line[2]
            rate = int(line[3].strip("."))
            year = int(line[4])
            certificate = line[5]
            time = int(line[6].strip(" min"))
            genre_list = []
            for genre in line[7].strip().split(", "):
                genre_list.append(genre)
            iplratingstar = float(line[8].replace(",", "."))
            content = line[9]
            director_url = line[10]
            director = line[11]
            star1_url = line[12]
            star1 = line[13]
            star2_url = line[14]
            star2 = line[15]
            star3_url = line[16]
            star3 = line[17]
            star4_url = line[18]
            star4 = line[19]
            votes = int("".join(line[20].split()))
            gross = line[21]
            
            obj = Film(title,title_url,image,rate,year,certificate,time,genre_list,iplratingstar,content,director_url,director,star1_url,star1,star2_url,star2,star3_url,star3,star4_url,star4,votes,gross)
            database.append(obj)
            





def mainContrusct():
    file = "filmek/filmek.csv"
    database = []
    construct(file, database)
    return database

mainContrusct()