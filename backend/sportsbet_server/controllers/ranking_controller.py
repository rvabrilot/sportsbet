import connexion, uuid
from flask import make_response
from sportsbet_server.config import db

def get_ranking():
    sql = """
select 
	u.nickname as nickname,
	SUM(case
		when b.goals = fe.goals and b.`result`= fe.`result` then 15
		when b.`result`=fe.`result` then 5 
		else 0
	end) as points	
from 
(select id, nickname from `user`) u
left join bet b 
	on u.id = b.user_id 
left join 
( select id, goals, `result` from event where event_end < now()) fe
	on b.event_id = fe.id
WHERE 
	b.id IS NOT NULL
group by u.nickname
order by points desc;"""

    results = db.engine.execute(sql)
    output = "<table class='ranking-table'><tr><th>nickname</th><th>points</th></tr>"
    if results.rowcount > 0 :
        for i, result in enumerate(results):
            output += f"<tr><td>{result[0]}</td><td>{result[1]}</td></tr>"
        output += "</table>"
        
        return output
    else:
        return "no se pudo generar el ranking."