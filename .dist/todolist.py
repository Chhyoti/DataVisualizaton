def to_do_list():
    dist = {
        "jan":"HTML CSS ",
        "Feb":"JS",
        "March":"React",
        "April":"python",
        "May":"DJango",
        "June":"Project build"
    }
   
    dist.pop("March")
    
    print(dist)
to_do_list()