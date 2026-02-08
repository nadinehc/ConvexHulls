from sweeping import generate_video, sweeping_algorithm
from gift_wrapping import gift_wrapping_algorithm
from utils import visualize_hull
from output_sensitive import output_sensitive_hull
from quick_hull import quick_hull


if __name__ == "__main__":
    # visualize_dataset()
    
    # visualize_hull(100, "B")

    # test_sweeping_algorithm_datasetA()
    # test_sweeping_algorithm_datasetD()

    
    visualize_hull(100, quick_hull, dataset="B")

