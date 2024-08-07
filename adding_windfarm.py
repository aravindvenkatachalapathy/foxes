import pandas as pd
import numpy as np
import foxes
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # Step 1: Create a DataBook instance
    dbook = foxes.StaticData()

    # Step 2: Add a farm layout from a CSV file
    # Ensure the file path is correct
    csv_file_path = 'foxes/foxes/data/farms/randomized_test_farm_67.csv'
    dbook.add_file('farm', csv_file_path)

    # Step 3: Verify the addition by plotting the farm layout
    farm = foxes.WindFarm()
    foxes.input.farm_layout.add_from_file(
        farm, csv_file_path, turbine_models=[], verbosity=0
    )
    foxes.output.FarmLayoutOutput(farm).get_figure()
    plt.show()
    path = 'foxes/foxes/data/farms/randomized_test_farm_67.csv'
    # Step 4: Add the new file to the DataBook context
    dbook = foxes.StaticData()
    dbook.add_file('farm', path)

    # Verify the file is added to the context
    print(dbook.toc('farm'))

    # Load the new farm layout
    farm = foxes.WindFarm()
    foxes.input.farm_layout.add_from_file(
        farm, 'foxes/foxes/data/farms/randomized_test_farm_67.csv', turbine_models=[], verbosity=0
    )
    foxes.output.FarmLayoutOutput(farm).get_figure()
    plt.show()