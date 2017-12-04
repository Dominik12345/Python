# import packages
import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist import Subplot


# simple plot function
def plot2d(data, variables ,filename):
    
    # default vales
    logscale_x = False
    logscale_y = False
    
    grid_bool = False
    
    axistop_bool = False
    axisright_bool = False
    axisbottom_bool = True
    axisleft_bool = True
    
    # intern parameters
    plot_range = 1./10  # means of two data series differ by this factor, 
                        # the scalng is defined ill
    
    # prepare data --->
   
    # check for appropriate format of input
    if (isinstance( variables, list)):
        for i in variables:
            if (not isinstance(i,str)):
                print('second argument must be a list of str')
                return None
    else: 
        print('second argument must be a list')
                
    if (not isinstance(filename, str)):
        print('third argument must be of type str')
        return None
    if (not isinstance(data, list)): 
        print('first argument must be of type list')
        return None

    
    #get number of rows and colums of data
    ncols = len(data)
    nrows = len(data[0])
    
    
    #check wether all rows have the same size and create df
    df = {} # initialize empty dictionary similar to dataframe
    for i in range(0,ncols):
        if not len(data[i]) == nrows:
            print('missing values in data set')
            return None
        else:
            df[ variables[i] ] = data[i]
    
    # <--- prepare data
    
    # ---> analyse data
    
    # get lower and upper bounds of each variable
    bounds = {}
 
    for i in variables:
        [bounds['lower',i] , bounds['upper',i] ] = [min(df[i]) , max(df[i])]
    
    # check whether magnitudes are approximately equal
    means = [0] * (ncols-1)
    
    for i in range(1,ncols):
        means[i-1] = np.mean( df[ variables[i] ] )    
        
    if min(means)/max(means) < plot_range:
        print('ill scaling - use logscale')
        logscale_y = True
        
    # <--- analyse data
    

    # plot --->
    fig = plt.figure(1)
    ax = Subplot(fig,111)
    fig.add_subplot(ax)
    
    for i in variables[1:]:
        ax.scatter( df[variables[0]] , df[i] , label = '$'+i+'$' )
    
    # legend
    ax.legend()
    plt.xlabel('$'+variables[0]+'$')
    
    # logscale
    if logscale_y:
        plt.yscale('log')
    if logscale_x:
        plt.xscale('log')
    # grid
    plt.grid(grid_bool)
    # visible axis
    ax.axis["right"].set_visible(axisright_bool)
    ax.axis["top"].set_visible(axistop_bool)
    ax.axis["bottom"].set_visible(axisbottom_bool)
    ax.axis["left"].set_visible(axisleft_bool)
    
    
    # <--- plot
    
    # save plot --->
    directory = 'C:/Users/kahl/Documents/Images/' + filename + '.pdf'
    fig.savefig(directory)
    # <--- save plot 
    
    
    print('test run successful')
    return None    


############
# TEST RUN #            
############

# get data from json file
file = open("C:/Users/kahl/Documents/Data/data_pythonplottest.txt",'r')
data = json.loads( file.read() )
file.close()
# apply function
for i in range(0,len(data[1])):
    data[1][i] = data[1][i]* 1911.

temp = plot2d(data, ['time', 'y_1','3'] ,'test' )
