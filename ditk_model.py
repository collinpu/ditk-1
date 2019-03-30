import abc

class DITKModel(abc.ABC):

	@staticmethod
	@abc.abstractmethod
	def load_train_dataset(*args, **kwargs):
		pass

	@staticmethod
	@abc.abstractmethod
	def load_test_dataset(*args, **kwargs):
		pass

	@staticmethod
	@abc.abstractmethod
	def train(*args, **kwargs):
		pass

	@staticmethod
	@abc.abstractmethod
	def predict(*args, **kwargs):
		pass

	@staticmethod
	@abc.abstractmethod
	def evaluate(*args, **kwargs):
		pass
