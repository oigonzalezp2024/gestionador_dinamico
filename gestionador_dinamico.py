import webview

def file_open(file_name):
    file_open = open(file_name, "r")
    lines = file_open.readlines()
    file_open.close()
    return lines

def interpretate(line):
    mylist = line.split('|')    
    return mylist

def def_format(repo):
    my_str = "" 
    my_str += repo['name'] + "|"  
    my_str += repo['gestion'] + "|"
    my_str += repo['url']  
    return my_str

def repo_open(repo):
    repo_name = repo['name']
    repo_url = repo['url']
    webview.create_window(repo_name, repo_url)
    webview.start()
    gestion = str(input("gestion:"))
    return gestion

def validate_gestion(lines, line, count):
    if(line[1] == "0"):
        repo = {}
        repo['name'] = line[0]
        repo['url'] = line[2]
        repo['gestion'] = repo_open(repo)
        my_str = def_format(repo)
        lines[count] = my_str
    gest = line[1]
    return lines, gest 

def my_repos(file_name):
    lines = file_open(file_name)
    count = 0
    lines2 = lines
    gestion = []
    for ele in lines2:
        line = interpretate(ele)
        lines, gest = validate_gestion(lines, line, count)
        gestion.append(int(gest))
        count = count + 1
    return lines, gestion

def file_reset(file_name):
    file_open = open(file_name, "w")
    file_open.write("")
    file_open.close()
    
def file_update(file_name, my_list):
    file_open = open(file_name, "a")
    for ele in my_list:
        file_open.write(ele)
    file_open.close()

def control(file_name):
    lines, gestion = my_repos(file_name)
    file_reset(file_name)
    file_update(file_name, lines)
    if 0 in gestion:
       control(file_name)
