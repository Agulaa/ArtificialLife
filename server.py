from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter


from agents import Snail, Greenfly, Salad, Tomato, Fermon
from model import Garden

COLORS = {"Greenfly": "#00AA00", "Snail": "#880000", "Salad": "#003330","Tomato": "#330000" }



class VegetablesElement(TextElement):
    """
    Display a text count of how many happy agents there are.
    """

    def __init__(self):
        pass

    def render(self, model):
        return "Tomatoes: " + str(model.tomato) +"\n  Salads: " + str(model.salad)




def garden_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is Greenfly:
        portrayal["Shape"] = "images/greenfly.svg"
        #https://www.flaticon.com/svg/static/icons/svg/3209/3209941.svg
        portrayal["Layer"] = 0


    elif type(agent) is Snail:
        portrayal["Shape"] = "images/snail.svg"
        #https://www.flaticon.com/svg/static/icons/svg/2174/2174096.svg
        portrayal["Layer"] = 1


    elif type(agent) is Salad:
        portrayal["Shape"] = "images/salad.svg"
        #https://www.flaticon.com/svg/static/icons/svg/1155/1155281.svg
        portrayal["scale"] = 0.8
        portrayal["Layer"] = 2
        #portrayal["Filled"]="true"
        #portrayal["Color"] = ["#003330", "#003330"]

    elif type(agent) is Tomato:
        portrayal["Shape"] = "images/tomato.svg"
        #https://www.flaticon.com/svg/static/icons/svg/1202/1202125.svg
        portrayal["scale"] = 0.8
        portrayal["Layer"] = 4

    elif type(agent) is Fermon:
        portrayal["Shape"] = "circle"
        portrayal["r"] = 0.1
        portrayal["Layer"] = 5
        if agent.type =="Tomato":
            portrayal["Color"] =["#330000", '#330000']
        else:
            portrayal["Color"] = ["#013300", '#013300']



    return portrayal


vegetables_element = VegetablesElement()
canvas_element = CanvasGrid(garden_portrayal, 20, 20, 500, 500)
chart = ChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)

model_params = {
    "height": 20,
    "width": 20,

    "initial_tomato": UserSettableParameter(
        "slider", "Initial Tomato Population", 100, 10, 300
    ),
    "initial_salad": UserSettableParameter(
        "slider", "Initial Salad Population", 100, 10, 300
    ),
    "initial_snail": UserSettableParameter(
        "slider", "Initial Snail Population", 100, 10, 300
    ),
    "initial_greenfly": UserSettableParameter(
        "slider", "Initial Greenfly Population", 100, 10, 300
    ),
    "preparation_1": UserSettableParameter(
        "slider", "Preparation_1", 20, 1, 50
    ),
    "preparation_2": UserSettableParameter(
        "slider", "Preparation_2", 20, 1, 50
    ),
    "fermon": UserSettableParameter(
        "slider", "Fermon", 1, 1, 20
    ),
    "steps": UserSettableParameter(
        "slider", "Steps", 20, 1, 50
    ),
    "target": UserSettableParameter(
        "slider", "Target", 20, 1, 50
    )

}
server = ModularServer(
    Garden, [canvas_element,vegetables_element ,chart], "Garden", model_params
)
server.port = 8521
