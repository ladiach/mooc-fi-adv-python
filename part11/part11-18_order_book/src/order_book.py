# Write your solution here:
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
    
if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    
    orders.mark_finished(1)
    orders.mark_finished(2)
    
    status = orders.status_of_programmer("Eric")
    print(status)