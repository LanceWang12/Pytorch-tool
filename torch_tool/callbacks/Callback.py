import torch

class Callback():
    def __init__(
        self,
        callbacks=None,
        add_history=False,
        add_progbar=False,
        model=None,
        **params
    ):
        pass
    
    def on_train_begin(self):
        # progress bar's length, initialization
        # history and ?log?
        raise NotImplementedError('This is virtual member function. Please overwrite!')

    def on_train_end(self):
        raise NotImplementedError('This is virtual member function. Please overwrite!')

    def on_epoch_begin(self):
        # print epoch
        # reset log
        raise NotImplementedError('This is virtual member function. Please overwrite!')

    def on_epoch_end(self):
        # update PB
        # record history
        # callback
        raise NotImplementedError('This is virtual member function. Please overwrite!')

    def on_batch_begin(self):
        # update loss of log
        raise NotImplementedError('This is virtual member function. Please overwrite!')

    def on_batch_end(self):
        # print message 
        raise NotImplementedError('This is virtual member function. Please overwrite!')

    def on_test_begin(self):
        # update log of training acc, validation loss acc
        raise NotImplementedError('This is virtual member function. Please overwrite!')

    def on_test_end(self):
        raise NotImplementedError('This is virtual member function. Please overwrite!')

