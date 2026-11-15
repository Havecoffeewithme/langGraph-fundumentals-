from typing import Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    message : str 

def greeting_node(state: AgentState) -> AgentState:
    """simple node that adds greetings message to the state"""

    state['message'] = "hey " + state["message"] + ", how is your evening so far ? "
    
    return state

graph = StateGraph(AgentState)

graph.add_node("greeter", greeting_node)

graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()

result = app.invoke({"message":"Bob"})

result["message"]