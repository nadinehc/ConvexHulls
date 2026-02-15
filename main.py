from datasets import datasetB, datasetC, visualize_dataset
from sweeping import generate_video_sweeping, sweeping_algorithm
from gift_wrapping import gift_wrapping_algorithm
from utils import visualize_hull
from kirkpatrick_seidel import kirkpatrick_seidel_algorithm
from comparison import execution_time_comparison, hull_comparison, nb_recursive_call_graph1, nb_recursive_call_graph2
from quick_hull import quick_hull_algorithm
from image import image


if __name__ == "__main__":
    ###################################################################
    ###################### Dataset visualization ######################
    ####################################################################

    # visualize_dataset()

    ###################################################################
    ###################### Convex Hull visualization ##################
    ###################################################################
    
    
    # generate_video_sweeping(100, "B")
    # visualize_hull(100, "A", kirkpatrick_seidel_algorithm)
    # visualize_hull(100, "B", gift_wrapping_algorithm)
    # quick_hull_algorithm(datasetC(40), visualize=True)


    ###################################################################
    ###################### All algorithms at once #####################
    ###################################################################

    # hull_comparison(50, "C")


    ###################################################################
    ###################### Execution time comparison ##################
    ###################################################################

    execution_time_comparison("C", gift_wrapping=True, quick_hull=True)
    
    # nb_recursive_call_graph1(10000, nb_runs=100, dataset="B")
    # nb_recursive_call_graph2()