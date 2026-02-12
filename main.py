from sweeping import generate_video, sweeping_algorithm
from gift_wrapping import gift_wrapping_algorithm
from utils import visualize_hull
from kirkpatrick_seidel import kirkpatrick_seidel_algorithm
from comparison import execution_time_comparison, hull_comparison, nb_recursive_call_graph
from quick_hull import quick_hull_algorithm



if __name__ == "__main__":
    # visualize_dataset()
    
    # visualize_hull(100, "B")

    # test_sweeping_algorithm_datasetA()
    # test_sweeping_algorithm_datasetD()

    execution_time_comparison("B", gift_wrapping=True, quick_hull=True ) #peut prendre du temps
    
    nb_recursive_call_graph(10000, nb_runs=100, dataset="B")

    hull_comparison(50, "B")
    
    #visualize_hull(100, sweeping_algorithm, dataset="B")

