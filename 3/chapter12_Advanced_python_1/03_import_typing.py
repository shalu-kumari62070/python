from typing import List, Dict, Tuple, Union

number : List[int] = [14, 78]
print(number, type(number))  # [14, 78] <class 'list'>

person: Tuple[str, int] = ("alice",77, 78,"hello")
print(person)  # ('alice', 77, 78, 'helllo')

scores : Dict[str, int] = {"a":1,"b":5, 87:"hhelo"}
print(scores)  # {'a': 1, 'b': 5, 87: 'hhelo'}

identifier : Union[int, str] = "id78@"
print(identifier) # id78@
