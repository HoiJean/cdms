import hashlib


class Passwordcommand:

	def hash_password(self, text):
		text = str(text).encode('utf-8')
		return hashlib.md5(text).hexdigest()
