from Symbol import Symbol

class SymbolTable:
	def __init__(self, symbols, symbolId):
		self.symbols = {
			symbolId: Symbol()
		}