def reduce_file_path(path):
    path = path.split("/")
    new_path = []
    print(path)
    for ch in range(len(path)):
        if path[ch] != "" and path[ch] != ".":
            new_path.append(path[ch])
    i=0
    while i < len(new_path):
        if new_path[i] == "..":
            if i-1 >= 0:
                del new_path[i-1:i+1]
                i -= 1
            else:
                del new_path[i]
        else:
            i +=1
    reduced_path = ""
    if len(new_path) == 0:
        return "/"
    else:
        return "/".join(new_path)
print(reduce_file_path("gg/ddd/..//////////"))

