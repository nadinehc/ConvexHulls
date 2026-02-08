from sweeping import generate_video, sweeping_algorithm
from gift_wrapping import gift_wrapping_algorithm
from utils import visualize_hull
from test_sweeping import test_sweeping_algorithm_datasetA, test_sweeping_algorithm_datasetD
from output_sensitive import output_sensitive_hull


if __name__ == "__main__":
    # visualize_dataset()
    
    # visualize_hull(100, "B")

    # test_sweeping_algorithm_datasetA()
    # test_sweeping_algorithm_datasetD()

    
    visualize_hull(100, "D", output_sensitive_hull)

