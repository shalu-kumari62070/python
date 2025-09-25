def status(num):
    match num:
        case 100:
            print("ok")
        case "hello":
            print("hii, nice to meet you")

        case 455:
            return "yes find"
        
        case  _:
            return "unknown status"
        
status("hello")     # hii, nice to meet you
status(100)         # ok
print(status(455))  # yes find     
print(status(22))   # unknown status