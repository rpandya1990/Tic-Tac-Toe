from tic_tac_toe.master import Master


class Playroom(object):
	"""Playroom with 2 players."""

	def __init__(self, master):
		"""Create a playroom.

		Start the server and connect client to it
		Args:
	    	master: (TCP_IP, port)
		"""

		self.player1 = Master(master[0], master[1])

obj = Playroom(('127.0.0.1', 64))
