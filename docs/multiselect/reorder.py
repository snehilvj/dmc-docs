import dash_mantine_components as dmc

component = dmc.MultiSelect(
    label="Drag pills to reorder",
    description="Selected values can be reordered by dragging pills",
    placeholder="Pick value",
    value=["Pandas", "TensorFlow", "NumPy"],
    data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
    withPillsReorder=True,
    w=400,
    mb=180,
)
