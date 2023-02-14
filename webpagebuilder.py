from konstrukt import mainContrusct as getDatabase


def webpage_databuilder(database, file_start, file_mainsample, file_end):
    with open("./new_page.html", "w", encoding="UTF-8"):
        with open("./new_page.html", "a", encoding="UTF-8") as new_page, open(file_start, encoding="UTF-8") as start, open(file_mainsample, encoding="UTF-8") as sample, open(file_end, encoding="UTF-8") as file_end:
            temp = start.read()
            new_page.write(temp) # eleje
            genres = []
            temp = sample.read()
            for genre in database:
                for item in genre.genre:
                    if item not in genres:
                        genres.append(item)
            for item in genres:
                print(item)
            userinput = input("Szeretne szűrni műfajra? Enter ha nem, különben írja be a műfajt:\n")
            def builder(data):
                s = temp
                s = s.replace("kep_helye", data.image)
                s = s.replace("szerzo_helye", data.director)
                s = s.replace("cim_helye", data.title)
                s = s.replace("ev_helye", str(data.year))
                s = s.replace("szineszek_helye", f"{data.star1}, {data.star2}, {data.star3}, {data.star4}")
                s = s.replace("mufajok_helye", str(data.genre).strip())
                s = s.replace("leiras_helye", data.content)
                s = s.replace("href1szerzo", data.director_url)
                s = s.replace("href1cim", data.title_url)
                new_page.write(s) # közepe
            for data in database:
                if userinput == "":
                    builder(data)
                elif userinput in data.genre:
                    builder(data)
                
            
            temp = file_end.read()
            new_page.write(temp) # vége
        
            
        



def main():
    database = getDatabase()
    file_start = "./_start.txt"
    file_mainsample = "./_mainsample.txt"
    file_end = "./_end.txt"
    webpage_databuilder(database, file_start, file_mainsample, file_end)

main()