import foxes
import matplotlib.pyplot as plt
import foxes.variables as FV


if __name__ == "__main__":
    # Step 1: Create a ModelBook instance
    mbook = foxes.models.ModelBook()

    # Step 2: Add a turbine model from a CSV file
    # Ensure the file path is correct
    csv_file_path = 'foxes/foxes/data/power_ct_curves/Optimus-20MW-D295-H160.csv'
    mbook.turbine_types["Optimus-20MW"] = foxes.models.turbine_types.PCtFile(csv_file_path)

    # Step 3: Verify the addition by plotting the curves
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))
    o = foxes.output.TurbineTypeCurves(mbook)
    o.plot_curves("Optimus-20MW", [FV.P, FV.CT], axs=axs)
    plt.show()