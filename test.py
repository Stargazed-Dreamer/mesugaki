from mesugaki import Mesugaki
Mesugaki.use_original_location_hint = True
Mesugaki.use_original_location_hint = False
Mesugaki.test_mode = True


def a():
	def b():
		1/0
	b()

with Mesugaki():
	#a()
	1

from mesugaki import alwaysMesugaki
#from mesugaki import stopMesugaki
#alwaysMesugaki.stop()
a()
'''
1/0'''