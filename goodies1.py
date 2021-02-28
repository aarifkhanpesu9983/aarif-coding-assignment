import sys 
p_list = []
my_input_file = sys.argv[1]
my_output_file = sys.argv[2]


# the create_price_list function will create a list of price
def create_price_list():
    input_file = open(my_input_file)
    file_content = input_file.readlines()

    for price in file_content:
        colon =price.find(":")
        c = price[colon+2:].rstrip("\n") 
        if(c != ""):
            p_list.append(int(c))
    size = p_list[0]
    p_list.remove(p_list[0])
    print("p_list --> ",p_list)
    return size
    
size = create_price_list()
# max_p function will return the maximun price from the provided list 
def max_p(p_list):
  max_val = p_list[0] 
  for flag in p_list: 
    if flag > max_val: 
      max_val = flag 
  return max_val

print("max in p_list ",max_p(p_list))

# min_p function will return the minimum price from the provided list
def min_p(p_list):
  min_val = p_list[0] 
  for flag in p_list: 
    if flag < min_val: 
      min_val = flag 
  return min_val

def max_min_diff(max,min):
    return max-min

print("max - min --> ",max_min_diff(max_p(p_list),min_p(p_list)))

diff = max_min_diff(max_p(p_list),min_p(p_list))

def write_output():

  with open(my_output_file, "a") as file1: 
      input_file = open(my_input_file)
      file_content = input_file.readlines()
      n =4 
      file1.write("Number of the employees: "+str(size)+"\n")
      file1.write("\n")
      file1.write("Here the goodies that are selected for distribution are:\n")
      count = 0
      for i in file_content:
        #   print(i)
          count+=1
          if count >4:
              file1.write(i)
    
      file1.write("\n")
      file1.write("\n")
      file1.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(diff))
      
write_output()