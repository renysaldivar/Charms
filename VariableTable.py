from Variable import Variable

class VariableTable:
	def __init__(self, vars, varId):
		self.vars = {
			varId: Variable()
		}