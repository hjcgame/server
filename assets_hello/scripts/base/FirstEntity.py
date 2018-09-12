# -*- coding: utf-8 -*-
import KBEngine
import KBEDebug

class FirstEntity(KBEngine.Entity):
	"""docstring for ClassName"""
	def __init__(self):
		KBEngine.Entity.__init__(self)

	def hello(self, content):
		"""say hello"""
		INFO_MSG("hello%s___%s" % (self.name, content))
