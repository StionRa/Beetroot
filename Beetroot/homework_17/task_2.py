class Boss:
    def __init__(self, id_: int, name: str, company: str):
        # Initializes a new instance of the Boss class.
        #
        # Args:
        #     id_ (int): Unique ID for the boss.
        #     name (str): Name of the boss.
        #     company (str): Name of the company the boss works for.
        #
        # Attributes:
        #     id_ (int): Unique ID for the boss.
        #     name (str): Name of the boss.
        #     company (str): Name of the company the boss works for.
        #     _workers (list): List of workers that work for the boss.
        self.id_ = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        # Returns a copy of the list of workers that work for the boss.
        #
        # Returns:
        #     list: A copy of the list of workers that work for the boss.
        return self._workers.copy()

    def add_worker(self, worker):
        # Adds a new worker to the boss's list of workers.
        #
        # Args:
        #     worker (Worker): The worker to be added.
        #
        # Raises:
        #     ValueError: If the argument is not an instance of the Worker class.
        #     ValueError: If the worker already has a different boss.
        if not isinstance(worker, Worker):
            raise ValueError("Only instances of the Worker class can be added as workers.")
        if worker.boss is not None and worker.boss != self:
            raise ValueError("Worker already has a different boss.")
        if worker not in self._workers:
            self._workers.append(worker)
            worker.boss = self

    def remove_worker(self, worker):
        # Removes a worker from the boss's list of workers.
        # Args:
        #     worker (Worker): The worker to be removed.
        # Raises:
        #      ValueError: If the worker is not in the boss's list of workers.
        if worker in self._workers:
            self._workers.remove(worker)
        else:
            raise ValueError("This worker is not in the boss's workers list.")

    @workers.deleter
    def workers(self):
        # Deletes the list of workers that work for the boss.
        del self._workers


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss=None):

        Initializes a new instance of the Worker class.
        # Args:
        #     id_ (int): Unique ID for the worker.
        #     name (str): Name of the worker.
        #     company (str): Name of the company the worker works for.
        #     boss (Boss, optional): The boss of the worker. Defaults to None.
        #
        # Attributes:
        #     id_ (int): Unique ID for the worker.
        #     name (str): Name of the worker.
        #     company (str): Name of the company the worker works for.
        #     _boss (Boss): The boss of the worker.
        self.id_ = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        # Returns the boss of the worker.
        #
        # Returns:
        #     Boss: The boss of the worker.
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        # Sets the boss of the worker.
        # Args:
        #     new_boss (Boss): The new boss of the worker.
        # Raises:
        #     ValueError: If the argument is not an instance of the Boss class or None.
        if new_boss is None or isinstance(new_boss, Boss):
            if self._boss is not None:
                self._boss.workers.remove(self)
            if new_boss is not None:
                new_boss.add_worker(self)
            self._boss = new_boss
        else:
            raise ValueError("The 'boss' property must be an instance of Boss or None.")
