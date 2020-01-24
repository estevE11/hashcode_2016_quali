from drone import Drone
from warehouse import Warehouse
from order import Order

# weight <= drone max payload
# 1 torn = 1 cell
# rounded > one 
# xo = id_werehouse 1

# https://storage.googleapis.com/coding-competitions.appspot.com/HC/2016/hashcode2016_qualification_task.pdf

input_file = "inputs/exemple"

max_weight = None
turns = None

drones = []
warehouses = []
items = []
orders = []


rows = None
cols = None





def load_data():
    ipt_file = open(input_file + ".in", "r")
    lines = ipt_file.read().split("\n")
    init_info = lines[0].split(" ")

    rows = int(init_info[0])
    cols = int(init_info[1])
    n_drones = int(init_info[2])
    turns = int(init_info[3])
    max_weight = int(init_info[4])
    
    #Init drones
    drones = [0]*n_drones
    for i in range(n_drones):
        drones[i] = Drone(i)

    #Items
    #n_items = int(lines[1])
    _items = lines[2].split(" ")
    items = [0]*len(_items)
    for i in range(len(_items)):
        items[i] = int(_items[i])

    #Warehouses    
    n_wh = int(lines[3])
    warehouses = [0]*n_wh
    for i in range(n_wh):
        wh_pos = lines[4 + i*2].split(" ")
        wh_items = lines[5 + i*2].split(" ")
        warehouses[i] = Warehouse(i, int(wh_pos[0]), int(wh_pos[1]))
        warehouses[i].items = [0]*len(wh_items)
        for j in range(len(wh_items)):
            warehouses[i].items[j] = int(wh_items[j])
        
    #Orders
    init_idx = 4 + n_wh*2
    n_orders = int(lines[init_idx])
    orders = [0]*n_orders
    for i in range(n_orders):
        orders_pos = lines[init_idx+1 + i*3].split(" ")
        orders_items = lines[init_idx+1 + (i*3)+2].split(" ")
        orders[i] = Order(orders_pos[0], orders_pos[1])
        orders[i].items = [0]*len(orders_items)
        for j in range(len(orders_items)): #convertim a int
            orders[i].items[j] = int(orders_items[j])


def get_commands():
    pass

def main():
    load_data()


    
main()
