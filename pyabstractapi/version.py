VERSION = (0, 0, 1)


def get_version(version=VERSION):
	return ".".join(map(lambda x: str(x), version))