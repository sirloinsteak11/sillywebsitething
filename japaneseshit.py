import random as ran

dayGreeting = "konichiwa!"
nightGreeting = 'konbanwa!'
inquiry = "kyou wa nani shimasu ka?"

responses = ["ecchi ecchi shiyou yo", "oppai hoshii. agenai?", "nee, sekusu agero!!", "tenbatsu, onegaishimasu!!!", "hanii no manko ni ikitai", "motto gyutte shite, oniichan!", "nee-san, karakawanaide kudasai!", "senpai, watashi oshaburi jouzu wa! senpai no chinchin irete kudasai!"]

def dirtyshit():
  return responses[ran.randint(0,7)]