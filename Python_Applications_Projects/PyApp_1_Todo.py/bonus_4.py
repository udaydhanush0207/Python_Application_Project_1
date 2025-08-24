filenames = ["1.Raw Data.txt", "2.Reports.txt","3.Presentations.txt"]      #lists are mutable, they cna be changed whereas strings cannot be changed

for filename in filenames:
    filename = filename.replace(".","-",1)  #by using replace() method we can replace thew string by overwriting on the previous string
    print(filename)