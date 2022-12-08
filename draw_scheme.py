from PIL import Image,ImageDraw
import numpy as np
flat_weights=[]
def get_flat_weights_abss(array):
    for i in array:
        if type(i)==list or type(i)==np.ndarray:
            get_flat_weights_abss(i)
        else:
            flat_weights.append(abs(i))
    return flat_weights 
def draw_neural_network_scheme(arch,weights,gor_gap=40, vert_gap=20):
    width=500
    height=500
    image= Image.new("RGBA",(width,height))
    draw = ImageDraw.Draw(image)
    start_coor_of_all_layers=[]
    max_neurons_count=max(max(arch),len(arch))
    m=max_neurons_count
    diametr_gor=(image.height-gor_gap*(len(arch)-1))/len(arch)
    diametr_vert=(image.height-vert_gap*(max(arch)-1))/max(arch)
    diametr=min(diametr_gor,diametr_vert)
    for z in range(len(arch)):#draw layers
        whole_space=arch[z]*diametr+vert_gap*(arch[z]-1)
        start_coor=(diametr*z+gor_gap*z,(image.height-whole_space)/2)
        start_coor_of_all_layers.append([])
        for i in range(arch[z]):
            start_coor=(start_coor[0],(diametr+vert_gap)*i+(image.height-whole_space)/2)
            start_coor_of_all_layers[z].append(start_coor)
            end_coor=tuple(map(lambda x:x+diametr,start_coor))
            draw.ellipse(([start_coor,end_coor]),width=3) 
    #find max_weight <lol>
    max_weight=max(get_flat_weights_abss(weights))
    for i in range(len(start_coor_of_all_layers)-1):#draw weights(connections between neurons)
        for j in range(len(start_coor_of_all_layers[i])):
            for k in range(len(start_coor_of_all_layers[i+1])):
                draw.line([(start_coor_of_all_layers[i][j][0]+diametr,start_coor_of_all_layers[i][j][1]+diametr/2),
                         (start_coor_of_all_layers[i+1][k][0],start_coor_of_all_layers[i+1][k][1]+diametr/2)],width=round(weights[i][k][j]/abs(max_weight)*8) ,fill="white" if weights[i][k][j]>=0 else "black")

    image.save("neural_network.png")
