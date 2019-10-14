# Class to store information related to symbols (variables, functions, etc)

class Symbol:
	def __init__(self, symbolId, symbolType, symbolScope, symbolKind):
		self.symbolId = symbolId # unique identifier
		self.symbolType = symbolType # int, char, bool
		self.symbolScope = symbolScope # local or global
		self.symbolKind = symbolKind # var or func (or another kind of symbol)