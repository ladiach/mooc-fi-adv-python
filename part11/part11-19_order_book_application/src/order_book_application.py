# Write your solution here
# If you use the classes made in the previous exercise, copy them here
class Task:
    tot_tasks = 0
    
    def __init__(self, descr:str, programmer:str, exp_wl:int):
        self.description = descr
        self.programmer =programmer
        self.workload = exp_wl
        self.__state = "NOT FINISHED"
        Task.tot_tasks +=1
        self.id = Task.tot_tasks 
    
    def is_finished(self):
        return self.__state == "FINISHED"
    
    def mark_finished(self):
        self.__state = "FINISHED"
    
    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.__state}"
    
    
class OrderBook:
    
    def __init__(self):
        self.__orders = []
    
    def add_order(self, description:str, programmer:str, workload:int):
        task = Task(description, programmer, workload)
        self.__orders.append(task)
    
    def all_orders(self):
        return self.__orders
    
    def programmers(self):
        return list(set([order.programmer for order in self.__orders]))
    
    def mark_finished(self, id: int):
        for order in self.__orders:
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError(f"{id} not found")
    
    
    def finished_orders(self):
        return [order for order in self.__orders if order.is_finished()]
    
    def unfinished_orders(self):
        return [order for order in self.__orders if not order.is_finished()]
    
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError
    
        tasks = [order for order in self.__orders if order.programmer == programmer]
        finished_tasks = 0
        unfinished_tasks = 0
        worked_hours = 0
        to_work = 0
    
        for task in tasks:
            if task.is_finished():
                finished_tasks +=1
                worked_hours += task.workload
            else:
                unfinished_tasks += 1
                to_work += task.workload
    
        return (finished_tasks, unfinished_tasks, worked_hours, to_work)
    
    
class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()
    
    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmers")
    
    def add_order(self):
        description = input("description: ")
        programmer_wl = input("programmer and workload estimate: ")
        programmer_wl = programmer_wl.split(" ")
        programmer = programmer_wl[0]
    
        try:
            wl = int(programmer_wl[1])
        except:
            self.error()
            return
    
        self.__orderbook.add_order(description, programmer, wl)
        print("added!")
    
    def finished_tasks(self):
        if len(self.__orderbook.finished_orders()):
            for order in self.__orderbook.finished_orders():
                print(order)
        else:
            print("no finished tasks")
    
    def unfinished_tasks(self):
        for order in self.__orderbook.unfinished_orders():
            print(order)
    
    def mark_as_finished(self):
        try:
            id = int(input("id: "))
        except:
            self.error()
            return
        
        ids = [order.id for order in self.__orderbook.all_orders()]
        if id not in ids:
            self.error()
            return
    
        self.__orderbook.mark_finished(id)
        print("marked as finished")
    
    def programmers(self):
        for programmer in self.__orderbook.programmers():
            print(programmer)
    
    def status(self):
        programmer = input("programmer: ")
    
        if programmer not in self.__orderbook.programmers():
            self.error()
            return
    
        f_tasks, uf_tasks, done, to_do = self.__orderbook.status_of_programmer(programmer)
        print(f"tasks: finished {f_tasks} not finished {uf_tasks}, hours: done {done} scheduled {to_do}")
    
    def error(self):
        print("erroneous input")
    
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.finished_tasks()
            elif command == "3":
                self.unfinished_tasks()
            elif command == "4":
                self.mark_as_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.status()
    
    
    
    
# when testing, no code should be outside application except the following:
application = OrderBookApplication()
application.execute()