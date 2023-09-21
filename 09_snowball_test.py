

def compute_best_snowball():
    # Read the number of snowballs
    N = int(input())

    
    max_value = -1
    best_weight = 0
    best_time = 0
    best_quality = 0

   
    for _ in range(N):
        weight = int(input())
        time = int(input())
        quality = int(input())

      
        value = (weight / time) ** quality

        if value > max_value:
            max_value = value
            best_weight = weight
            best_time = time
            best_quality = quality

 
    print(f"{best_weight} : {best_time} = {int(max_value)} ({best_quality})")


compute_best_snowball()
