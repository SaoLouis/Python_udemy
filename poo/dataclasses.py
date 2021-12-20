from dataclasses import dataclass

@dataclass
class Users:
	first_name: str
	last_name: str =""
patrick = Users(first_name="Patrick", last_name="Smith")
print(repr(patrick))


# from dataclasses import dataclass
# from typing import ClassVar
#
# @dataclass
# class Users:
# 	first_name: str
# 	last_name: str
# 	c: ClassVar[int]
# patrick = Users(first_name="Patrick", last_name="Smith")
# print(patrick.__dict__)
