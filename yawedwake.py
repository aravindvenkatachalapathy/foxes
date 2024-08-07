import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import foxes
import foxes.variables as FV
import foxes.constants as FC

if __name__ == "__main__":
    # Initialize a ModelBook object
    mbook = foxes.models.ModelBook()

    # Add the Optimus-20MW model to the ModelBook
    csv_file_path = 'foxes/foxes/data/power_ct_curves/Optimus-20MW-D295-H160.csv'
    mbook.turbine_types["Optimus-20MW"] = foxes.models.turbine_types.PCtFile(csv_file_path)

    # Prepare state data
    sdata = pd.DataFrame(index=range(3))
    sdata[FV.WS] = 8.0
    sdata[FV.WD] = 270.0
    states = foxes.input.states.StatesTable(
        data_source=sdata,
        output_vars=[FV.WS, FV.WD, FV.TI, FV.RHO],
        fixed_vars={FV.RHO: 1.225, FV.TI: 0.05},
    )

    # Define yaw misalignment
    yawm = np.array([
        [30.0, 0.0], [0.0, 0.0], [-30.0, 0.0]
    ])

    # Add the set_yawm model to the same ModelBook instance
    mbook.turbine_models["set_yawm"] = foxes.models.turbine_models.SetFarmVars()
    mbook.turbine_models["set_yawm"].add_var(FV.YAWM, yawm)

    # Initialize the WindFarm object and add turbines
    farm = foxes.WindFarm()
    farm.add_turbine(
        foxes.Turbine(
            xy=[0.0, 0.0],
            turbine_models=["set_yawm", "yawm2yaw", "Optimus-20MW", "kTI_05"],
        )
    )
    farm.add_turbine(
        foxes.Turbine(
            xy=[1000.0, 0.0],
            turbine_models=["set_yawm", "yawm2yaw", "Optimus-20MW", "kTI_05"],
        )
    )

    # Initialize the algorithm with the single ModelBook instance
    algo = foxes.algorithms.Downwind(
        farm,
        states,
        rotor_model="centre",
        wake_models=["Bastankhah2016_linear", "IECTI2019_max"],
        wake_frame="yawed",
        mbook=mbook,  # Use the same ModelBook instance
        chunks=None,
        verbosity=0,
    )

    # Calculate farm results
    farm_results = algo.calc_farm()

