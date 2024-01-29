class Experiment:
    
    running_status = None

    def __new__(cls, *args, **kwargs):
        if Experiment.running_status:
            raise Exception("Exception is already running hence new experiment can not be created")
        return super(Experiment, cls).__new__(cls, *args, **kwargs)
    
    def __init__(self, experiment_id) -> None:
        self.experiment_id = experiment_id
        self.running_status = Experiment.running_status